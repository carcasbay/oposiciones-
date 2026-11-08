import { ResultadoExamen, HistorialUsuario, PreguntaFalladaInfo, OposicionId } from '@/types';

function getStorageKey(oposicionId: OposicionId = 'utrera'): string {
  return oposicionId === 'andalucia'
    ? 'oposiciones_andalucia_historial_v1'
    : 'oposiciones_utrera_historial_v1';
}

export function obtenerHistorial(oposicionId: OposicionId = 'utrera'): HistorialUsuario {
  if (typeof window === 'undefined') {
    return { examenes: [], preguntasFalladas: {} };
  }

  try {
    const key = getStorageKey(oposicionId);
    const raw = localStorage.getItem(key);
    if (!raw) {
      return { examenes: [], preguntasFalladas: {} };
    }
    return JSON.parse(raw);
  } catch (error) {
    console.error(`Error al leer el historial (${oposicionId}) de localStorage:`, error);
    return { examenes: [], preguntasFalladas: {} };
  }
}

export function guardarResultadoExamen(resultado: ResultadoExamen): HistorialUsuario {
  const oposicionId: OposicionId = resultado.oposicionId || 'utrera';

  if (typeof window === 'undefined') {
    return { examenes: [resultado], preguntasFalladas: {} };
  }

  const historial = obtenerHistorial(oposicionId);

  // Añadir examen al principio
  historial.examenes.unshift(resultado);

  // Actualizar bolsa de preguntas falladas
  const ahora = new Date().toISOString();
  for (const [preguntaId, respuesta] of Object.entries(resultado.respuestas)) {
    if (respuesta.respuestaSeleccionada && !respuesta.esCorrecta) {
      // Ha fallado
      const infoActual = historial.preguntasFalladas[preguntaId];
      // Buscar temaId en las preguntas del resultado
      const pregObj = resultado.preguntas.find((p) => p.id === preguntaId);
      const temaId = pregObj?.temaId || 1;

      historial.preguntasFalladas[preguntaId] = {
        preguntaId,
        vecesFallada: (infoActual?.vecesFallada || 0) + 1,
        ultimaFecha: ahora,
        temaId,
        oposicionId,
      };
    } else if (respuesta.esCorrecta) {
      // Si la ha acertado, disminuimos o eliminamos si ya no es recurrente
      const infoActual = historial.preguntasFalladas[preguntaId];
      if (infoActual) {
        if (infoActual.vecesFallada <= 1) {
          delete historial.preguntasFalladas[preguntaId];
        } else {
          infoActual.vecesFallada -= 1;
        }
      }
    }
  }

  try {
    const key = getStorageKey(oposicionId);
    localStorage.setItem(key, JSON.stringify(historial));
  } catch (error) {
    console.error(`Error al guardar el examen (${oposicionId}) en localStorage:`, error);
  }

  return historial;
}

export function obtenerPreguntasFalladasIds(oposicionId: OposicionId = 'utrera'): string[] {
  const historial = obtenerHistorial(oposicionId);
  return Object.keys(historial.preguntasFalladas);
}

export interface EstadisticasGlobales {
  totalExamenes: number;
  totalPreguntasRespondidas: number;
  aciertosTotales: number;
  erroresTotales: number;
  enBlancoTotales: number;
  notaMedia: number;
  tasaAprobados: number; // Porcentaje de exámenes aprobados
  temasFlojos: { temaId: number; errores: number; total: number; porcentajeError: number }[];
  totalFalladasPendientes: number;
}

export function calcularEstadisticasGlobales(oposicionId: OposicionId = 'utrera'): EstadisticasGlobales {
  const historial = obtenerHistorial(oposicionId);
  const examenes = historial.examenes;

  if (examenes.length === 0) {
    return {
      totalExamenes: 0,
      totalPreguntasRespondidas: 0,
      aciertosTotales: 0,
      erroresTotales: 0,
      enBlancoTotales: 0,
      notaMedia: 0,
      tasaAprobados: 0,
      temasFlojos: [],
      totalFalladasPendientes: Object.keys(historial.preguntasFalladas).length,
    };
  }

  let aciertos = 0;
  let errores = 0;
  let enBlanco = 0;
  let sumaNotas = 0;
  let aprobadosCount = 0;

  const temaRendimiento = new Map<number, { errores: number; total: number }>();

  for (const ex of examenes) {
    aciertos += ex.aciertos;
    errores += ex.errores;
    enBlanco += ex.enBlanco;
    sumaNotas += ex.notaSobre10;
    if (ex.aprobado) aprobadosCount++;

    for (const d of ex.desglosePorTema) {
      if (!temaRendimiento.has(d.temaId)) {
        temaRendimiento.set(d.temaId, { errores: 0, total: 0 });
      }
      const t = temaRendimiento.get(d.temaId)!;
      t.errores += d.errores;
      t.total += d.total;
    }
  }

  const temasFlojos = Array.from(temaRendimiento.entries())
    .map(([temaId, data]) => ({
      temaId,
      errores: data.errores,
      total: data.total,
      porcentajeError: data.total > 0 ? Math.round((data.errores / data.total) * 100) : 0,
    }))
    .filter((t) => t.total >= 3) // Solo temas con al menos 3 preguntas evaluadas
    .sort((a, b) => b.porcentajeError - a.porcentajeError);

  const totalEx = examenes.length;
  return {
    totalExamenes: totalEx,
    totalPreguntasRespondidas: aciertos + errores,
    aciertosTotales: aciertos,
    erroresTotales: errores,
    enBlancoTotales: enBlanco,
    notaMedia: Math.round((sumaNotas / totalEx) * 100) / 100,
    tasaAprobados: Math.round((aprobadosCount / totalEx) * 100),
    temasFlojos,
    totalFalladasPendientes: Object.keys(historial.preguntasFalladas).length,
  };
}

export function limpiarHistorial(oposicionId: OposicionId = 'utrera'): void {
  if (typeof window !== 'undefined') {
    const key = getStorageKey(oposicionId);
    localStorage.removeItem(key);
  }
}

export function exportarDatos(oposicionId: OposicionId = 'utrera'): string {
  const historial = obtenerHistorial(oposicionId);
  return JSON.stringify(historial, null, 2);
}

export function importarDatos(jsonStr: string, oposicionId: OposicionId = 'utrera'): boolean {
  try {
    const data = JSON.parse(jsonStr);
    if (data && Array.isArray(data.examenes) && typeof data.preguntasFalladas === 'object') {
      const key = getStorageKey(oposicionId);
      localStorage.setItem(key, JSON.stringify(data));
      return true;
    }
    return false;
  } catch (err) {
    console.error(`Error importando datos (${oposicionId}):`, err);
    return false;
  }
}
