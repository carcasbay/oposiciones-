'use client';

import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { ResultadoExamen, OpcionLetra } from '@/types';
import { formatearTiempo } from '@/lib/utils';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  Award, 
  RotateCcw, 
  PlusCircle, 
  BarChart3, 
  Filter, 
  BookOpen, 
  Clock, 
  Percent,
  Check,
  X
} from 'lucide-react';

interface PantallaResultadosProps {
  resultado: ResultadoExamen;
  onRepetirTest: () => void;
  onNuevoTest: () => void;
  onVerEstadisticas: () => void;
}

type FiltroRevision = 'todas' | 'errores' | 'aciertos' | 'blanco';

export const PantallaResultados: React.FC<PantallaResultadosProps> = ({
  resultado,
  onRepetirTest,
  onNuevoTest,
  onVerEstadisticas,
}) => {
  const [filtro, setFiltro] = useState<FiltroRevision>('todas');

  // Lanzar confeti si está aprobado
  useEffect(() => {
    if (resultado.aprobado) {
      try {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 },
        });
      } catch {
        // En caso de que no esté disponible canvas
      }
    }
  }, [resultado.aprobado]);

  // Filtrado de preguntas para la revisión
  const preguntasFiltradas = resultado.preguntas.filter((p) => {
    const r = resultado.respuestas[p.id];
    if (filtro === 'errores') {
      return r?.respuestaSeleccionada !== null && !r?.esCorrecta;
    }
    if (filtro === 'aciertos') {
      return !!r?.esCorrecta;
    }
    if (filtro === 'blanco') {
      return !r?.respuestaSeleccionada;
    }
    return true;
  });

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-8">
      {/* 1. Tarjeta de Calificación Oficial */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-10 relative overflow-hidden">
        {/* Fondo decorativo según aprobado/suspenso */}
        <div
          className={`absolute top-0 right-0 w-80 h-80 rounded-full blur-3xl -mr-20 -mt-20 pointer-events-none opacity-40 ${
            resultado.aprobado ? 'bg-emerald-200' : 'bg-red-200'
          }`}
        />

        <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="space-y-2 text-center md:text-left">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-slate-100 text-slate-700">
              <Award className={`h-3.5 w-3.5 ${resultado.oposicionId === 'andalucia' ? 'text-emerald-600' : 'text-blue-600'}`} />
              <span>
                {resultado.oposicionId === 'andalucia'
                  ? 'Calificación Oficial · Junta de Andalucía (A2.2018)'
                  : 'Calificación Convocatoria Oficial · Ayuntamiento de Utrera'}
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
              Resultado del Simulacro
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 max-w-lg leading-relaxed">
              {resultado.config.penalizacion === 'ninguna' ? (
                <>Fórmula aplicada: <strong>Sin penalización por errores</strong> (Puntuación = Aciertos). Las no contestadas no penalizan.</>
              ) : resultado.config.penalizacion === 'cuarto' ? (
                <>Fórmula aplicada: <strong>Puntuación = Aciertos - (Errores / 4)</strong>. Cada fallo descuenta 0,25 puntos netos. Las no contestadas no penalizan.</>
              ) : (
                <>Fórmula aplicada: <strong>Puntuación = Aciertos - (Errores / 3)</strong>. Cada fallo descuenta 0,33 puntos netos. Las no contestadas no penalizan.</>
              )}
            </p>
          </div>

          {/* Calificación Numérica e Insignia */}
          <div className="flex flex-col items-center justify-center p-6 rounded-2xl bg-slate-50 border border-slate-200 min-w-[220px] text-center shadow-inner">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
              Nota Final (sobre 10)
            </span>
            <div className="my-1 flex items-baseline gap-1">
              <span
                className={`text-5xl font-black tracking-tight ${
                  resultado.aprobado ? 'text-emerald-600' : 'text-red-600'
                }`}
              >
                {resultado.notaSobre10.toFixed(2)}
              </span>
              <span className="text-slate-400 font-bold text-lg">/ 10</span>
            </div>

            <span
              className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider mt-1 ${
                resultado.aprobado
                  ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                  : 'bg-red-100 text-red-800 border border-red-300'
              }`}
            >
              {resultado.aprobado ? 'Apto (Aprobado)' : 'No Apto'}
            </span>
          </div>
        </div>

        {/* 2. Cuadrícula de Métricas Clave */}
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 mt-8 pt-8 border-t border-slate-100">
          <div className="bg-emerald-50/70 border border-emerald-200/80 rounded-2xl p-4 text-center">
            <span className="text-xs font-bold text-emerald-700 uppercase">Aciertos (+1,0)</span>
            <div className="text-2xl font-black text-emerald-900 mt-1">{resultado.aciertos}</div>
            <span className="text-[11px] text-emerald-600 font-medium">
              +{resultado.aciertos.toFixed(2)} pts
            </span>
          </div>

          <div className="bg-red-50/70 border border-red-200/80 rounded-2xl p-4 text-center">
            <span className="text-xs font-bold text-red-700 uppercase">Errores (-0,33)</span>
            <div className="text-2xl font-black text-red-900 mt-1">{resultado.errores}</div>
            <span className="text-[11px] text-red-600 font-medium">
              -{(resultado.errores / 3).toFixed(2)} pts
            </span>
          </div>

          <div className="bg-slate-100/80 border border-slate-200 rounded-2xl p-4 text-center">
            <span className="text-xs font-bold text-slate-600 uppercase">En Blanco (0,0)</span>
            <div className="text-2xl font-black text-slate-800 mt-1">{resultado.enBlanco}</div>
            <span className="text-[11px] text-slate-500 font-medium">Sin penalizar</span>
          </div>

          <div className="bg-blue-50/70 border border-blue-200/80 rounded-2xl p-4 text-center">
            <span className="text-xs font-bold text-blue-700 uppercase">Aciertos Netos</span>
            <div className="text-2xl font-black text-blue-900 mt-1">
              {resultado.puntuacionNeta.toFixed(2)}
            </div>
            <span className="text-[11px] text-blue-600 font-medium">
              de {resultado.preguntas.length} preg.
            </span>
          </div>

          <div className="bg-slate-100/80 border border-slate-200 rounded-2xl p-4 text-center col-span-2 sm:col-span-1">
            <span className="text-xs font-bold text-slate-600 uppercase flex items-center justify-center gap-1">
              <Clock className="h-3 w-3" /> Tiempo
            </span>
            <div className="text-2xl font-black text-slate-800 mt-1">
              {formatearTiempo(resultado.tiempoEmpleadoSegundos)}
            </div>
            <span className="text-[11px] text-slate-500 font-medium">
              {Math.round(resultado.tiempoEmpleadoSegundos / resultado.preguntas.length)}s / preg
            </span>
          </div>
        </div>
      </div>

      {/* 3. Desglose de Rendimiento por Tema */}
      {resultado.desglosePorTema.length > 0 && (
        <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
              <BookOpen className="h-5 w-5 text-blue-600" />
              Desglose de Rendimiento por Tema
            </h2>
            <span className="text-xs text-slate-500 font-medium">
              {resultado.desglosePorTema.length} temas evaluados
            </span>
          </div>

          <div className="space-y-3">
            {resultado.desglosePorTema.map((d) => (
              <div
                key={d.temaId}
                className="p-3.5 rounded-xl border border-slate-100 bg-slate-50/60 hover:bg-slate-50 transition-colors"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">
                      Tema {d.temaId}
                    </span>
                    <span className="text-xs font-semibold text-slate-800 truncate max-w-xs sm:max-w-md">
                      {d.temaTitulo}
                    </span>
                  </div>
                  <div className="flex items-center gap-3 text-xs">
                    <span className="text-emerald-700 font-bold">{d.aciertos} aciertos</span>
                    <span className="text-red-600 font-bold">{d.errores} fallos</span>
                    <span className="text-slate-500">{d.enBlanco} blanco</span>
                    <span
                      className={`font-black px-2 py-0.5 rounded text-xs ${
                        d.porcentajeAcierto >= 50
                          ? 'bg-emerald-100 text-emerald-800'
                          : 'bg-red-100 text-red-800'
                      }`}
                    >
                      {d.porcentajeAcierto}% neto
                    </span>
                  </div>
                </div>

                {/* Barra de progreso por tema */}
                <div className="w-full bg-slate-200 h-2 rounded-full overflow-hidden flex">
                  <div
                    className="bg-emerald-500 h-full"
                    style={{ width: `${(d.aciertos / d.total) * 100}%` }}
                    title={`${d.aciertos} aciertos`}
                  />
                  <div
                    className="bg-red-500 h-full"
                    style={{ width: `${(d.errores / d.total) * 100}%` }}
                    title={`${d.errores} fallos`}
                  />
                  <div
                    className="bg-slate-300 h-full"
                    style={{ width: `${(d.enBlanco / d.total) * 100}%` }}
                    title={`${d.enBlanco} en blanco`}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 4. Revisión Detallada de Preguntas */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-5">
          <div>
            <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
              <Filter className="h-5 w-5 text-blue-600" />
              Revisión Detallada de Preguntas
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Consulta tus respuestas y el fundamento jurídico oficial de cada una.
            </p>
          </div>

          {/* Filtros de revisión */}
          <div className="flex flex-wrap gap-1.5 bg-slate-100 p-1 rounded-xl">
            <button
              onClick={() => setFiltro('todas')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filtro === 'todas'
                  ? 'bg-white text-slate-900 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Todas ({resultado.preguntas.length})
            </button>
            <button
              onClick={() => setFiltro('errores')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filtro === 'errores'
                  ? 'bg-white text-red-700 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Fallos ({resultado.errores})
            </button>
            <button
              onClick={() => setFiltro('aciertos')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filtro === 'aciertos'
                  ? 'bg-white text-emerald-700 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Aciertos ({resultado.aciertos})
            </button>
            <button
              onClick={() => setFiltro('blanco')}
              className={`px-3 py-1 text-xs font-semibold rounded-lg transition-all ${
                filtro === 'blanco'
                  ? 'bg-white text-slate-700 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              En Blanco ({resultado.enBlanco})
            </button>
          </div>
        </div>

        {/* Lista de preguntas */}
        <div className="space-y-6">
          {preguntasFiltradas.length === 0 ? (
            <p className="text-center py-8 text-sm text-slate-400">
              No hay preguntas con el filtro seleccionado.
            </p>
          ) : (
            preguntasFiltradas.map((preg, idx) => {
              const resp = resultado.respuestas[preg.id];
              const respondida = resp?.respuestaSeleccionada !== null;
              const acertada = resp?.esCorrecta === true;
              const fallada = respondida && !acertada;

              return (
                <div
                  key={preg.id}
                  className={`p-5 sm:p-6 rounded-2xl border-2 transition-all space-y-4 ${
                    acertada
                      ? 'border-emerald-200 bg-emerald-50/20'
                      : fallada
                      ? 'border-red-200 bg-red-50/20'
                      : 'border-slate-200 bg-slate-50/30'
                  }`}
                >
                  {/* Encabezado de la pregunta */}
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 rounded text-xs font-bold bg-slate-200 text-slate-800">
                        #{idx + 1}
                      </span>
                      <span className="px-2 py-0.5 rounded text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200">
                        Tema {preg.temaId}
                      </span>
                      {preg.origen === 'red_opositor' ? (
                        <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-100 text-purple-800 border border-purple-200">
                          Red Opositor
                        </span>
                      ) : (
                        <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 text-slate-700 border border-slate-200">
                          Temario Propio
                        </span>
                      )}
                    </div>

                    <div>
                      {acertada && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">
                          <Check className="h-3.5 w-3.5" /> Acertada (+1)
                        </span>
                      )}
                      {fallada && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold bg-red-100 text-red-800">
                          <X className="h-3.5 w-3.5" /> Fallada (-0,33)
                        </span>
                      )}
                      {!respondida && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-medium bg-slate-200 text-slate-700">
                          En Blanco (0)
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Enunciado */}
                  <p className="text-sm sm:text-base font-semibold text-slate-900 leading-snug">
                    {preg.numero}. {preg.enunciado}
                  </p>

                  {/* Opciones */}
                  <div className="space-y-2 pt-1">
                    {(['a', 'b', 'c', 'd'] as OpcionLetra[]).map((letra) => {
                      const esSolucionOficial = letra === preg.solucion;
                      const esLaQueMarcoElUsuario = resp?.respuestaSeleccionada === letra;

                      let estiloOpcion = 'border-slate-200 bg-white text-slate-700';
                      let estiloBadge = 'bg-slate-100 text-slate-700 border-slate-300';

                      if (esSolucionOficial) {
                        estiloOpcion = 'border-emerald-500 bg-emerald-50 text-emerald-950 font-medium ring-1 ring-emerald-500';
                        estiloBadge = 'bg-emerald-600 text-white border-emerald-600';
                      } else if (esLaQueMarcoElUsuario && !esSolucionOficial) {
                        estiloOpcion = 'border-red-400 bg-red-50 text-red-950 ring-1 ring-red-400 line-through';
                        estiloBadge = 'bg-red-600 text-white border-red-600';
                      }

                      return (
                        <div
                          key={letra}
                          className={`flex items-start gap-3 p-3 rounded-xl border text-xs sm:text-sm ${estiloOpcion}`}
                        >
                          <span
                            className={`h-6 w-6 rounded-md font-bold text-xs flex items-center justify-center uppercase shrink-0 border mt-0.5 ${estiloBadge}`}
                          >
                            {letra}
                          </span>
                          <span className="flex-1 pt-0.5">{preg.opciones[letra]}</span>
                          {esSolucionOficial && (
                            <span className="text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded shrink-0">
                              Correcta
                            </span>
                          )}
                          {esLaQueMarcoElUsuario && !esSolucionOficial && (
                            <span className="text-xs font-bold text-red-700 bg-red-100 px-2 py-0.5 rounded shrink-0">
                              Tu respuesta
                            </span>
                          )}
                        </div>
                      );
                    })}
                  </div>

                  {/* Justificación y fundamento legal */}
                  {preg.justificacion && (
                    <div className="bg-slate-100/90 border border-slate-200 rounded-xl p-3.5 space-y-1 text-xs sm:text-sm">
                      <span className="font-bold text-slate-900 block text-xs uppercase tracking-wider">
                        Justificación y Fundamentación Legal Oficial:
                      </span>
                      <p className="text-slate-700 leading-relaxed font-normal">
                        {preg.justificacion}
                      </p>
                    </div>
                  )}
                </div>
              );
            })
          )}
        </div>
      </div>

      {/* 5. Barra de Acciones Finales */}
      <div className="flex flex-wrap items-center justify-center sm:justify-end gap-3 pt-4">
        <button
          onClick={onRepetirTest}
          className="flex items-center gap-2 px-5 py-3 rounded-xl font-bold text-sm bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 shadow-sm transition-all"
        >
          <RotateCcw className="h-4 w-4 text-blue-600" />
          <span>Repetir con estos mismos temas</span>
        </button>

        <button
          onClick={onVerEstadisticas}
          className="flex items-center gap-2 px-5 py-3 rounded-xl font-bold text-sm bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 shadow-sm transition-all"
        >
          <BarChart3 className="h-4 w-4 text-indigo-600" />
          <span>Ver Historial y Estadísticas</span>
        </button>

        <button
          onClick={onNuevoTest}
          className="flex items-center gap-2 px-6 py-3 rounded-xl font-bold text-sm bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20 active:scale-95 transition-all"
        >
          <PlusCircle className="h-4 w-4" />
          <span>Configurar Nuevo Test</span>
        </button>
      </div>
    </div>
  );
};
