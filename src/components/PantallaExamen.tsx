'use client';

import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { 
  Pregunta, 
  ConfiguracionTest, 
  RespuestaExamen, 
  OpcionLetra, 
  ResultadoExamen 
} from '@/types';
import { calcularCalificacion } from '@/lib/scoring';
import { formatearTiempo } from '@/lib/utils';
import { 
  Timer, 
  Flag, 
  ChevronLeft, 
  ChevronRight, 
  CheckCircle2, 
  XCircle, 
  AlertCircle, 
  Grid, 
  X, 
  Send,
  HelpCircle,
  RotateCcw
} from 'lucide-react';

interface PantallaExamenProps {
  preguntas: Pregunta[];
  config: ConfiguracionTest;
  onFinalizarExamen: (resultado: ResultadoExamen) => void;
  onCancelarExamen: () => void;
}

export const PantallaExamen: React.FC<PantallaExamenProps> = ({
  preguntas,
  config,
  onFinalizarExamen,
  onCancelarExamen,
}) => {
  const [indiceActual, setIndiceActual] = useState<number>(0);
  const [respuestas, setRespuestas] = useState<Record<string, RespuestaExamen>>(() => {
    const init: Record<string, RespuestaExamen> = {};
    for (const p of preguntas) {
      init[p.id] = {
        preguntaId: p.id,
        respuestaSeleccionada: null,
        esCorrecta: null,
        marcadaDuda: false,
      };
    }
    return init;
  });

  // En modo estudio, preguntas cuya solución ya ha sido consultada/comprobada
  const [comprobadasEstudio, setComprobadasEstudio] = useState<Record<string, boolean>>({});

  // Temporizador
  const [segundosRestantes, setSegundosRestantes] = useState<number>(config.tiempoTotalSegundos);
  const [tiempoEmpleado, setTiempoEmpleado] = useState<number>(0);

  // Modales
  const [mostrarModalEntrega, setMostrarModalEntrega] = useState<boolean>(false);
  const [mostrarCuadricula, setMostrarCuadricula] = useState<boolean>(false);

  const preguntaActual = preguntas[indiceActual];
  const respuestaActual = respuestas[preguntaActual.id];

  // Conteo de respuestas
  const estadisticasProgreso = useMemo(() => {
    let respondidas = 0;
    let dudas = 0;
    for (const r of Object.values(respuestas)) {
      if (r.respuestaSeleccionada !== null) respondidas++;
      if (r.marcadaDuda) dudas++;
    }
    const enBlanco = preguntas.length - respondidas;
    return { respondidas, dudas, enBlanco, total: preguntas.length };
  }, [respuestas, preguntas.length]);

  // Manejo de finalización
  const entregarExamen = useCallback(() => {
    const ahora = new Date().toISOString();
    const resumen = calcularCalificacion(preguntas, respuestas, config.penalizacion || 'tercio');

    const resultado: ResultadoExamen = {
      id: `exam_${Date.now()}`,
      fecha: ahora,
      config,
      respuestas,
      preguntas,
      aciertos: resumen.aciertos,
      errores: resumen.errores,
      enBlanco: resumen.enBlanco,
      puntuacionNeta: resumen.puntuacionNeta,
      notaSobre10: resumen.notaSobre10,
      aprobado: resumen.aprobado,
      tiempoTotalSegundos: config.tiempoTotalSegundos,
      tiempoEmpleadoSegundos: tiempoEmpleado,
      desglosePorTema: resumen.desglosePorTema,
      oposicionId: config.oposicionId,
    };

    onFinalizarExamen(resultado);
  }, [preguntas, respuestas, config, tiempoEmpleado, onFinalizarExamen]);

  // Intervalo de temporizador
  useEffect(() => {
    const timer = setInterval(() => {
      setTiempoEmpleado((prev) => prev + 1);

      if (config.temporizadorActivo) {
        setSegundosRestantes((prev) => {
          if (prev <= 1) {
            clearInterval(timer);
            entregarExamen();
            return 0;
          }
          return prev - 1;
        });
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [config.temporizadorActivo, entregarExamen]);

  // Selección de respuesta
  const seleccionarRespuesta = (letra: OpcionLetra) => {
    setRespuestas((prev) => {
      const actual = prev[preguntaActual.id];
      const nuevaLetra = actual.respuestaSeleccionada === letra ? null : letra;
      const esCorrecta = nuevaLetra ? nuevaLetra === preguntaActual.solucion : null;

      return {
        ...prev,
        [preguntaActual.id]: {
          ...actual,
          respuestaSeleccionada: nuevaLetra,
          esCorrecta,
        },
      };
    });
  };

  const desmarcarRespuesta = () => {
    setRespuestas((prev) => ({
      ...prev,
      [preguntaActual.id]: {
        ...prev[preguntaActual.id],
        respuestaSeleccionada: null,
        esCorrecta: null,
      },
    }));
  };

  const toggleDuda = () => {
    setRespuestas((prev) => ({
      ...prev,
      [preguntaActual.id]: {
        ...prev[preguntaActual.id],
        marcadaDuda: !prev[preguntaActual.id].marcadaDuda,
      },
    }));
  };

  const comprobarRespuestaEstudio = () => {
    setComprobadasEstudio((prev) => ({
      ...prev,
      [preguntaActual.id]: true,
    }));
  };

  // Atajos de teclado
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignorar si hay modales abiertos o inputs activos
      if (mostrarModalEntrega || mostrarCuadricula) return;
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement)?.tagName)) return;

      const key = e.key.toLowerCase();
      if (key === '1' || key === 'a') seleccionarRespuesta('a');
      else if (key === '2' || key === 'b') seleccionarRespuesta('b');
      else if (key === '3' || key === 'c') seleccionarRespuesta('c');
      else if (key === '4' || key === 'd') seleccionarRespuesta('d');
      else if (key === '0' || key === ' ') desmarcarRespuesta();
      else if (key === 'f') toggleDuda();
      else if (key === 'arrowright') {
        if (indiceActual < preguntas.length - 1) setIndiceActual((prev) => prev + 1);
      } else if (key === 'arrowleft') {
        if (indiceActual > 0) setIndiceActual((prev) => prev - 1);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [preguntaActual, indiceActual, preguntas.length, mostrarModalEntrega, mostrarCuadricula]);

  const esEstudioComprobada = config.modo === 'estudio' && !!comprobadasEstudio[preguntaActual.id];

  return (
    <div className="min-h-[calc(100vh-4rem)] flex flex-col bg-slate-100">
      {/* Barra superior de control del examen */}
      <div className="sticky top-16 z-30 bg-white border-b border-slate-200 px-4 sm:px-6 py-3 shadow-sm">
        <div className="max-w-5xl mx-auto flex items-center justify-between gap-3">
          {/* Navegación y progreso */}
          <div className="flex items-center gap-3">
            <button
              onClick={() => setMostrarCuadricula(true)}
              className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold bg-slate-100 hover:bg-slate-200 text-slate-800 rounded-lg transition-colors border border-slate-200"
              title="Abrir mapa de preguntas"
            >
              <Grid className="h-4 w-4 text-blue-600" />
              <span>Preguntas</span>
            </button>
            <span className="text-sm font-bold text-slate-900">
              #{indiceActual + 1}{' '}
              <span className="text-slate-400 font-normal">/ {preguntas.length}</span>
            </span>
          </div>

          {/* Estadísticas rápidas en el centro */}
          <div className="hidden sm:flex items-center gap-4 text-xs font-medium text-slate-600">
            <div className="flex items-center gap-1.5">
              <span className="h-2.5 w-2.5 rounded-full bg-blue-600"></span>
              <span>{estadisticasProgreso.respondidas} respondidas</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="h-2.5 w-2.5 rounded-full bg-amber-400"></span>
              <span>{estadisticasProgreso.dudas} en duda</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
              <span>{estadisticasProgreso.enBlanco} en blanco</span>
            </div>
          </div>

          {/* Temporizador y botón entregar */}
          <div className="flex items-center gap-3">
            {config.temporizadorActivo ? (
              <div
                className={`flex items-center gap-2 px-3 py-1.5 rounded-lg font-mono text-sm font-bold border transition-colors ${
                  segundosRestantes < 60
                    ? 'bg-red-50 text-red-700 border-red-200 animate-pulse'
                    : segundosRestantes < 300
                    ? 'bg-amber-50 text-amber-700 border-amber-200'
                    : 'bg-slate-50 text-slate-800 border-slate-200'
                }`}
              >
                <Timer className="h-4 w-4 text-blue-600" />
                <span>{formatearTiempo(segundosRestantes)}</span>
              </div>
            ) : (
              <div className="text-xs text-slate-500 font-medium hidden sm:block">
                Tiempo: {formatearTiempo(tiempoEmpleado)}
              </div>
            )}

            <button
              onClick={() => setMostrarModalEntrega(true)}
              className="flex items-center gap-1.5 px-3.5 py-1.5 text-xs sm:text-sm font-bold bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-sm transition-all active:scale-95"
            >
              <Send className="h-4 w-4" />
              <span>Entregar</span>
            </button>
          </div>
        </div>

        {/* Barra de progreso lineal inferior */}
        <div className="w-full bg-slate-100 h-1.5 mt-3 rounded-full overflow-hidden">
          <div
            className="bg-blue-600 h-full transition-all duration-300 ease-out"
            style={{ width: `${((indiceActual + 1) / preguntas.length) * 100}%` }}
          />
        </div>
      </div>

      {/* Cuerpo principal de la pregunta */}
      <div className="flex-1 max-w-4xl w-full mx-auto px-4 sm:px-6 py-6 flex flex-col justify-between">
        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-5 sm:p-8 space-y-6">
          {/* Cabecera del tema y acciones de duda */}
          <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="px-2.5 py-1 rounded-md text-xs font-bold bg-blue-50 text-blue-800 border border-blue-200">
                Tema {preguntaActual.temaId}
              </span>
              {preguntaActual.origen === 'red_opositor' ? (
                <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-100 text-purple-800 border border-purple-200">
                  Simulacro Red Opositor #{preguntaActual.numero}
                </span>
              ) : (
                <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-700 border border-slate-200">
                  Temario Propio #{preguntaActual.numero}
                </span>
              )}
              <span className="text-xs text-slate-500 truncate max-w-[200px] sm:max-w-md font-medium">
                {preguntaActual.temaTitulo}
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={toggleDuda}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold border transition-all ${
                  respuestaActual.marcadaDuda
                    ? 'bg-amber-100 text-amber-900 border-amber-300'
                    : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50'
                }`}
                title="Marcar pregunta con bandera para revisar luego"
              >
                <Flag className={`h-3.5 w-3.5 ${respuestaActual.marcadaDuda ? 'fill-current text-amber-600' : 'text-slate-400'}`} />
                <span>{respuestaActual.marcadaDuda ? 'En duda' : 'Dudar'}</span>
              </button>

              {respuestaActual.respuestaSeleccionada && (
                <button
                  type="button"
                  onClick={desmarcarRespuesta}
                  className="flex items-center gap-1 px-2 py-1 rounded-lg text-xs text-slate-500 hover:text-red-600 hover:bg-red-50 border border-transparent hover:border-red-100 transition-colors"
                  title="Dejar en blanco (tecla Espacio o 0)"
                >
                  <RotateCcw className="h-3 w-3" />
                  <span>Blanco</span>
                </button>
              )}
            </div>
          </div>

          {/* Enunciado */}
          <div>
            <h2 className="text-base sm:text-lg font-semibold text-slate-900 leading-relaxed">
              <span className="text-blue-600 font-bold mr-2">{preguntaActual.numero}.</span>
              {preguntaActual.enunciado}
            </h2>
          </div>

          {/* Opciones de respuesta */}
          <div className="space-y-3 pt-2">
            {(['a', 'b', 'c', 'd'] as OpcionLetra[]).map((letra) => {
              const textoOpcion = preguntaActual.opciones[letra];
              const estaSeleccionada = respuestaActual.respuestaSeleccionada === letra;

              // En modo estudio tras comprobar:
              const esLaCorrecta = esEstudioComprobada && letra === preguntaActual.solucion;
              const esErrorMarcado = esEstudioComprobada && estaSeleccionada && !esLaCorrecta;

              let estiloCaja = 'border-slate-200 hover:border-slate-300 bg-white text-slate-800';
              let estiloLetra = 'bg-slate-100 text-slate-700 border-slate-300';

              if (esLaCorrecta) {
                estiloCaja = 'border-emerald-500 bg-emerald-50/70 text-emerald-950 font-medium shadow-sm';
                estiloLetra = 'bg-emerald-600 text-white border-emerald-600';
              } else if (esErrorMarcado) {
                estiloCaja = 'border-red-400 bg-red-50/70 text-red-950 shadow-sm';
                estiloLetra = 'bg-red-600 text-white border-red-600';
              } else if (estaSeleccionada) {
                estiloCaja = 'border-blue-600 bg-blue-50/70 text-blue-950 font-medium shadow-sm ring-1 ring-blue-500';
                estiloLetra = 'bg-blue-600 text-white border-blue-600';
              }

              return (
                <button
                  key={letra}
                  type="button"
                  onClick={() => seleccionarRespuesta(letra)}
                  className={`w-full flex items-start gap-3.5 p-3.5 sm:p-4 rounded-xl border-2 text-left transition-all ${estiloCaja}`}
                >
                  <span
                    className={`h-7 w-7 rounded-lg font-bold text-xs flex items-center justify-center uppercase shrink-0 border mt-0.5 transition-colors ${estiloLetra}`}
                  >
                    {letra}
                  </span>
                  <span className="flex-1 text-sm sm:text-base leading-snug pt-0.5">
                    {textoOpcion}
                  </span>
                  {esLaCorrecta && <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0 mt-0.5" />}
                  {esErrorMarcado && <XCircle className="h-5 w-5 text-red-600 shrink-0 mt-0.5" />}
                </button>
              );
            })}
          </div>

          {/* Bloque de Modo Estudio: botón comprobar y justificación */}
          {config.modo === 'estudio' && (
            <div className="pt-4 border-t border-slate-100">
              {!esEstudioComprobada ? (
                <button
                  type="button"
                  onClick={comprobarRespuestaEstudio}
                  className="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm flex items-center gap-2 transition-all"
                >
                  <HelpCircle className="h-4 w-4" />
                  <span>Comprobar respuesta y ver justificación</span>
                </button>
              ) : (
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
                      Solución Oficial:
                    </span>
                    <span className="text-xs font-extrabold uppercase px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-200">
                      Opción {preguntaActual.solucion}
                    </span>
                  </div>
                  <p className="text-xs sm:text-sm text-slate-700 leading-relaxed font-normal">
                    {preguntaActual.justificacion || 'Sin justificación adicional.'}
                  </p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Barra de navegación inferior (Anterior / Siguiente) */}
        <div className="flex items-center justify-between gap-4 mt-6">
          <button
            type="button"
            disabled={indiceActual === 0}
            onClick={() => setIndiceActual((prev) => prev - 1)}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold border transition-all ${
              indiceActual === 0
                ? 'opacity-40 cursor-not-allowed bg-slate-100 text-slate-400 border-slate-200'
                : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50 active:scale-95 shadow-sm'
            }`}
          >
            <ChevronLeft className="h-4 w-4" />
            <span>Anterior</span>
          </button>

          <div className="text-xs text-slate-500 hidden sm:flex items-center gap-2">
            <span>Atajos:</span>
            <kbd className="px-1.5 py-0.5 bg-white border border-slate-300 rounded text-[10px] font-mono">1-4 / A-D</kbd>
            <span>elegir</span>
            <kbd className="px-1.5 py-0.5 bg-white border border-slate-300 rounded text-[10px] font-mono">Espacio</kbd>
            <span>blanco</span>
            <kbd className="px-1.5 py-0.5 bg-white border border-slate-300 rounded text-[10px] font-mono">F</kbd>
            <span>duda</span>
          </div>

          {indiceActual < preguntas.length - 1 ? (
            <button
              type="button"
              onClick={() => setIndiceActual((prev) => prev + 1)}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-bold bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/10 active:scale-95 transition-all"
            >
              <span>Siguiente</span>
              <ChevronRight className="h-4 w-4" />
            </button>
          ) : (
            <button
              type="button"
              onClick={() => setMostrarModalEntrega(true)}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-bold bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-500/10 active:scale-95 transition-all"
            >
              <Send className="h-4 w-4" />
              <span>Finalizar Examen</span>
            </button>
          )}
        </div>
      </div>

      {/* MODAL 1: Cuadrícula de Preguntas */}
      {mostrarCuadricula && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
          <div className="bg-white rounded-2xl border border-slate-200 max-w-2xl w-full p-6 shadow-2xl space-y-5 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-bold text-slate-900 text-base flex items-center gap-2">
                <Grid className="h-5 w-5 text-blue-600" />
                Mapa de Preguntas ({preguntas.length})
              </h3>
              <button
                onClick={() => setMostrarCuadricula(false)}
                className="p-1 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            {/* Leyenda */}
            <div className="flex flex-wrap items-center gap-4 text-xs text-slate-600 bg-slate-50 p-2.5 rounded-xl">
              <div className="flex items-center gap-1.5">
                <span className="h-3 w-3 rounded-full bg-blue-600"></span>
                <span>Respondida</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="h-3 w-3 rounded-full bg-amber-400"></span>
                <span>En duda</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="h-3 w-3 rounded-full bg-slate-200 border border-slate-300"></span>
                <span>En blanco</span>
              </div>
            </div>

            {/* Cuadrícula de botones */}
            <div className="grid grid-cols-6 sm:grid-cols-10 gap-2 max-h-[360px] overflow-y-auto p-1">
              {preguntas.map((p, idx) => {
                const r = respuestas[p.id];
                const estaActiva = idx === indiceActual;
                const tieneRespuesta = r?.respuestaSeleccionada !== null;
                const tieneDuda = r?.marcadaDuda;

                let estilo = 'bg-slate-100 text-slate-700 border-slate-200 hover:bg-slate-200';
                if (tieneDuda) {
                  estilo = 'bg-amber-100 text-amber-900 border-amber-300 font-bold';
                } else if (tieneRespuesta) {
                  estilo = 'bg-blue-600 text-white border-blue-600 font-bold';
                }

                return (
                  <button
                    key={p.id}
                    onClick={() => {
                      setIndiceActual(idx);
                      setMostrarCuadricula(false);
                    }}
                    className={`h-9 rounded-lg text-xs font-semibold border flex items-center justify-center transition-all ${estilo} ${
                      estaActiva ? 'ring-2 ring-blue-500 ring-offset-2' : ''
                    }`}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>

            <div className="pt-2 flex justify-end">
              <button
                onClick={() => setMostrarCuadricula(false)}
                className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold"
              >
                Cerrar mapa
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL 2: Confirmación de Entrega */}
      {mostrarModalEntrega && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
          <div className="bg-white rounded-2xl border border-slate-200 max-w-md w-full p-6 shadow-2xl space-y-5 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center gap-3 text-amber-600">
              <div className="p-2.5 rounded-xl bg-amber-50 border border-amber-200">
                <AlertCircle className="h-6 w-6 text-amber-600" />
              </div>
              <div>
                <h3 className="font-bold text-slate-900 text-base">¿Deseas entregar el examen?</h3>
                <p className="text-xs text-slate-500">Se procederá a la calificación oficial inmediata.</p>
              </div>
            </div>

            {/* Resumen de respuestas */}
            <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 space-y-2 text-xs">
              <div className="flex justify-between">
                <span className="text-slate-600">Preguntas contestadas:</span>
                <span className="font-bold text-blue-700">{estadisticasProgreso.respondidas}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-600">Preguntas en blanco:</span>
                <span className="font-bold text-slate-700">{estadisticasProgreso.enBlanco}</span>
              </div>
              {estadisticasProgreso.dudas > 0 && (
                <div className="flex justify-between">
                  <span className="text-slate-600">Marcadas para revisar:</span>
                  <span className="font-bold text-amber-700">{estadisticasProgreso.dudas}</span>
                </div>
              )}
              {config.temporizadorActivo && (
                <div className="flex justify-between pt-2 border-t border-slate-200">
                  <span className="text-slate-600">Tiempo restante:</span>
                  <span className="font-mono font-bold text-slate-900">
                    {formatearTiempo(segundosRestantes)}
                  </span>
                </div>
              )}
            </div>

            <p className="text-xs text-slate-500 leading-relaxed">
              <strong>Recordatorio de las bases:</strong> Cada acierto sumará 1 punto neto y cada fallo penalizará -0,33 puntos netos (E / 3). Las preguntas no contestadas computan 0 puntos y no restan.
            </p>

            <div className="flex items-center justify-end gap-3 pt-2">
              <button
                type="button"
                onClick={() => setMostrarModalEntrega(false)}
                className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-700 hover:bg-slate-100 transition-colors"
              >
                Seguir respondiendo
              </button>
              <button
                type="button"
                onClick={() => {
                  setMostrarModalEntrega(false);
                  entregarExamen();
                }}
                className="px-5 py-2.5 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20 active:scale-95 transition-all"
              >
                Sí, entregar y calificar
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
