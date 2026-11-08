import { Pregunta, RespuestaExamen, DesgloseTemaResultado, TipoPenalizacion } from '@/types';

export interface ResumenCalificacion {
  aciertos: number;
  errores: number;
  enBlanco: number;
  totalPreguntas: number;
  puntuacionNeta: number;
  notaSobre10: number;
  porcentajeEfectividad: number;
  aprobado: boolean;
  desglosePorTema: DesgloseTemaResultado[];
}

export function calcularCalificacion(
  preguntas: Pregunta[],
  respuestas: Record<string, RespuestaExamen>,
  penalizacion: TipoPenalizacion = 'tercio'
): ResumenCalificacion {
  let aciertos = 0;
  let errores = 0;
  let enBlanco = 0;

  // Mapa para desglose por tema
  const temaStatsMap = new Map<number, {
    temaId: number;
    temaTitulo: string;
    total: number;
    aciertos: number;
    errores: number;
    enBlanco: number;
  }>();

  for (const preg of preguntas) {
    const r = respuestas[preg.id];
    const respuestaDada = r?.respuestaSeleccionada || null;

    if (!temaStatsMap.has(preg.temaId)) {
      temaStatsMap.set(preg.temaId, {
        temaId: preg.temaId,
        temaTitulo: preg.temaTitulo,
        total: 0,
        aciertos: 0,
        errores: 0,
        enBlanco: 0,
      });
    }
    const tStat = temaStatsMap.get(preg.temaId)!;
    tStat.total += 1;

    if (!respuestaDada) {
      enBlanco += 1;
      tStat.enBlanco += 1;
    } else if (respuestaDada.toLowerCase() === preg.solucion.toLowerCase()) {
      aciertos += 1;
      tStat.aciertos += 1;
    } else {
      errores += 1;
      tStat.errores += 1;
    }
  }

  const totalPreguntas = preguntas.length;
  const calcularResta = (err: number): number => {
    if (penalizacion === 'ninguna') return 0;
    if (penalizacion === 'cuarto') return err / 4;
    return err / 3;
  };

  const penalizacionPorError = calcularResta(errores);
  const puntuacionNetaBruta = aciertos - penalizacionPorError;
  const puntuacionNeta = Math.round(puntuacionNetaBruta * 100) / 100;

  // Nota sobre 10: (puntuacionNeta / total) * 10
  const notaCalculada = totalPreguntas > 0 ? (puntuacionNetaBruta / totalPreguntas) * 10 : 0;
  // Acotamos entre 0 y 10 (las notas oficiales no pueden ser negativas)
  const notaSobre10 = Math.max(0, Math.min(10, Math.round(notaCalculada * 100) / 100));

  const porcentajeEfectividad = totalPreguntas > 0 ? Math.round((aciertos / totalPreguntas) * 100) : 0;
  const aprobado = notaSobre10 >= 5.0;

  const desglosePorTema: DesgloseTemaResultado[] = Array.from(temaStatsMap.values())
    .map((t) => {
      const netoTema = t.aciertos - calcularResta(t.errores);
      const pct = t.total > 0 ? Math.max(0, Math.round((netoTema / t.total) * 100)) : 0;
      return {
        temaId: t.temaId,
        temaTitulo: t.temaTitulo,
        total: t.total,
        aciertos: t.aciertos,
        errores: t.errores,
        enBlanco: t.enBlanco,
        porcentajeAcierto: pct,
      };
    })
    .sort((a, b) => a.temaId - b.temaId);

  return {
    aciertos,
    errores,
    enBlanco,
    totalPreguntas,
    puntuacionNeta,
    notaSobre10,
    porcentajeEfectividad,
    aprobado,
    desglosePorTema,
  };
}
