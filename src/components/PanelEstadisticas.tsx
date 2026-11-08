'use client';

import React, { useState, useEffect, useMemo } from 'react';
import { 
  calcularEstadisticasGlobales, 
  obtenerHistorial, 
  limpiarHistorial, 
  exportarDatos, 
  importarDatos, 
  EstadisticasGlobales 
} from '@/lib/storage';
import { TemaInfo, ResultadoExamen, OposicionId } from '@/types';
import { formatearTiempo } from '@/lib/utils';
import { 
  BarChart3, 
  TrendingUp, 
  Award, 
  AlertTriangle, 
  Clock, 
  Calendar, 
  Download, 
  Upload, 
  Trash2, 
  Play, 
  BookOpen, 
  CheckCircle,
  HelpCircle,
  Sparkles
} from 'lucide-react';

interface PanelEstadisticasProps {
  temas: TemaInfo[];
  onIniciarTestConTemas: (temasIds: number[]) => void;
  onIniciarModoFallos: () => void;
  onNuevoTest: () => void;
  oposicionId: OposicionId;
}

export const PanelEstadisticas: React.FC<PanelEstadisticasProps> = ({
  temas,
  onIniciarTestConTemas,
  onIniciarModoFallos,
  onNuevoTest,
  oposicionId,
}) => {
  const esAndalucia = oposicionId === 'andalucia';
  const [stats, setStats] = useState<EstadisticasGlobales | null>(null);
  const [historialExamenes, setHistorialExamenes] = useState<ResultadoExamen[]>([]);
  const [mensajeExport, setMensajeExport] = useState<string | null>(null);

  const cargarDatos = () => {
    const s = calcularEstadisticasGlobales(oposicionId);
    const h = obtenerHistorial(oposicionId);
    setStats(s);
    setHistorialExamenes(h.examenes);
  };

  useEffect(() => {
    cargarDatos();
  }, [oposicionId]);

  const mapaTemas = useMemo(() => {
    const m = new Map<number, TemaInfo>();
    for (const t of temas) m.set(t.id, t);
    return m;
  }, [temas]);

  const handleLimpiar = () => {
    if (confirm('¿Estás seguro de que deseas borrar todo tu historial de exámenes y bolsa de fallos de esta oposición? Esta acción no se puede deshacer.')) {
      limpiarHistorial(oposicionId);
      cargarDatos();
    }
  };

  const handleExportar = () => {
    const json = exportarDatos(oposicionId);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `oposiciones_${oposicionId}_backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    setMensajeExport('Copia de seguridad descargada correctamente.');
    setTimeout(() => setMensajeExport(null), 3000);
  };

  const handleImportar = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const content = event.target?.result as string;
      if (content) {
        const ok = importarDatos(content, oposicionId);
        if (ok) {
          cargarDatos();
          alert('¡Historial restaurado con éxito!');
        } else {
          alert('El archivo seleccionado no tiene el formato válido de copia de seguridad.');
        }
      }
    };
    reader.readAsText(file);
    e.target.value = '';
  };

  if (!stats) return null;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-8">
      {/* Cabecera */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2.5">
            <BarChart3 className={`h-7 w-7 ${esAndalucia ? 'text-emerald-600' : 'text-blue-600'}`} />
            <span>Estadísticas · {esAndalucia ? 'Junta de Andalucía' : 'Ayto. de Utrera'}</span>
          </h1>
          <p className="mt-1 text-xs sm:text-sm text-slate-600">
            Analiza tu histórico de exámenes, identifica tus temas débiles y entrena tus preguntas falladas.
          </p>
        </div>

        <button
          onClick={onNuevoTest}
          className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-bold bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20 active:scale-95 transition-all self-start sm:self-auto"
        >
          <Sparkles className="h-4 w-4" />
          <span>Realizar Test</span>
        </button>
      </div>

      {mensajeExport && (
        <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-semibold flex items-center gap-2 animate-in fade-in">
          <CheckCircle className="h-4 w-4 text-emerald-600" />
          <span>{mensajeExport}</span>
        </div>
      )}

      {/* 1. Tarjetas de Resumen General */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 text-xs font-semibold uppercase">
            <span>Nota Media</span>
            <Award className="h-4 w-4 text-blue-600" />
          </div>
          <div className="text-3xl font-black text-slate-900 mt-2">
            {stats.totalExamenes > 0 ? stats.notaMedia.toFixed(2) : '—'}
          </div>
          <span className="text-[11px] text-slate-500 mt-1 block">
            {stats.totalExamenes} simulacros completados
          </span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 text-xs font-semibold uppercase">
            <span>Tasa de Aprobados</span>
            <TrendingUp className="h-4 w-4 text-emerald-600" />
          </div>
          <div className="text-3xl font-black text-slate-900 mt-2">
            {stats.totalExamenes > 0 ? `${stats.tasaAprobados}%` : '—'}
          </div>
          <span className="text-[11px] text-slate-500 mt-1 block">
            Criterio de corte: ≥ 5,00
          </span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 text-xs font-semibold uppercase">
            <span>Preguntas Respondidas</span>
            <BookOpen className="h-4 w-4 text-indigo-600" />
          </div>
          <div className="text-3xl font-black text-slate-900 mt-2">
            {stats.totalPreguntasRespondidas}
          </div>
          <span className="text-[11px] text-slate-500 mt-1 block">
            {stats.aciertosTotales} aciertos · {stats.erroresTotales} errores
          </span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 text-xs font-semibold uppercase">
            <span>Bolsa de Fallos</span>
            <AlertTriangle className="h-4 w-4 text-amber-600" />
          </div>
          <div className="text-3xl font-black text-amber-600 mt-2">
            {stats.totalFalladasPendientes}
          </div>
          <span className="text-[11px] text-slate-500 mt-1 block">
            Preguntas pendientes de repasar
          </span>
        </div>
      </div>

      {/* 2. Banner de Acción Rápida: Bolsa de Fallos */}
      {stats.totalFalladasPendientes > 0 && (
        <div className="bg-gradient-to-r from-amber-500 to-amber-600 rounded-2xl p-5 sm:p-6 text-white shadow-md flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="space-y-1 text-center sm:text-left">
            <h3 className="font-extrabold text-base sm:text-lg flex items-center justify-center sm:justify-start gap-2">
              <AlertTriangle className="h-5 w-5" />
              Tienes {stats.totalFalladasPendientes} preguntas en tu bolsa de fallos
            </h3>
            <p className="text-xs sm:text-sm text-amber-100 max-w-xl">
              Entrenar específicamente los fallos recurrentes es la estrategia más eficaz para no cometer penalizaciones de -0,33 en la prueba oficial.
            </p>
          </div>

          <button
            onClick={onIniciarModoFallos}
            className="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-white text-amber-900 hover:bg-amber-50 active:scale-95 shadow transition-all shrink-0 flex items-center gap-2"
          >
            <Play className="h-4 w-4 fill-current" />
            <span>Repasar Fallos Ahora</span>
          </button>
        </div>
      )}

      {/* 3. Radar de Temas Flojos (Recomendaciones de Estudio) */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
            <AlertTriangle className="h-5 w-5 text-amber-500" />
            Radar de Temas a Reforzar
          </h2>
          <span className="text-xs text-slate-400">
            Temas con mayor porcentaje de error
          </span>
        </div>

        {stats.temasFlojos.length === 0 ? (
          <p className="text-xs sm:text-sm text-slate-500 py-4 text-center">
            {stats.totalExamenes === 0
              ? 'Realiza tus primeros exámenes para que el sistema detecte qué temas necesitas reforzar.'
              : '¡Excelente! No tienes temas con tasa de error significativa acumulada.'}
          </p>
        ) : (
          <div className="space-y-3 pt-1">
            {stats.temasFlojos.slice(0, 5).map((tf) => {
              const temaObj = mapaTemas.get(tf.temaId);
              const titulo = temaObj?.titulo || `Tema ${tf.temaId}`;
              return (
                <div
                  key={tf.temaId}
                  className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3.5 rounded-xl border border-slate-200 bg-slate-50/70 hover:bg-slate-50 transition-colors"
                >
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-900">
                        Tema {tf.temaId}
                      </span>
                      <span className="text-xs font-semibold text-slate-800 truncate">
                        {titulo}
                      </span>
                    </div>
                    <div className="flex items-center gap-3 text-[11px] text-slate-500 mt-1">
                      <span>{tf.errores} fallos de {tf.total} preguntas evaluadas</span>
                      <span className="font-bold text-red-600">{tf.porcentajeError}% de tasa de error</span>
                    </div>
                  </div>

                  <button
                    onClick={() => onIniciarTestConTemas([tf.temaId])}
                    className="self-end sm:self-auto px-3 py-1.5 rounded-lg text-xs font-bold bg-blue-50 text-blue-700 hover:bg-blue-100 border border-blue-200 transition-colors flex items-center gap-1.5"
                  >
                    <Play className="h-3 w-3 fill-current" />
                    <span>Hacer test de este tema</span>
                  </button>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* 4. Histórico de Exámenes Realizados */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
            <Calendar className="h-5 w-5 text-blue-600" />
            Histórico de Exámenes ({historialExamenes.length})
          </h2>
        </div>

        {historialExamenes.length === 0 ? (
          <p className="text-xs sm:text-sm text-slate-500 py-6 text-center">
            Aún no has completado ningún simulacro. Comienza uno en la pestaña &quot;Nuevo Test&quot;.
          </p>
        ) : (
          <div className="divide-y divide-slate-100 max-h-[380px] overflow-y-auto">
            {historialExamenes.map((ex) => {
              const fechaStr = new Date(ex.fecha).toLocaleString('es-ES', {
                dateStyle: 'short',
                timeStyle: 'short',
              });

              return (
                <div
                  key={ex.id}
                  className="py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs"
                >
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-bold text-slate-900">
                        {ex.preguntas.length} preguntas
                      </span>
                      <span className="text-slate-400">·</span>
                      <span className="text-slate-500">{fechaStr}</span>
                      <span className="text-slate-400">·</span>
                      <span className="capitalize text-slate-600 font-medium">
                        {ex.config.modo === 'examen' ? 'Simulacro' : ex.config.modo === 'estudio' ? 'Estudio' : 'Bolsa fallos'}
                      </span>
                    </div>
                    <div className="text-[11px] text-slate-500 flex items-center gap-2">
                      <span className="text-emerald-700 font-medium">{ex.aciertos} aciertos</span>
                      <span>·</span>
                      <span className="text-red-600 font-medium">{ex.errores} fallos</span>
                      <span>·</span>
                      <span className="text-slate-400">{ex.enBlanco} blanco</span>
                      <span>·</span>
                      <span>{formatearTiempo(ex.tiempoEmpleadoSegundos)}</span>
                    </div>
                  </div>

                  <div className="flex items-center gap-3">
                    <div className="text-right">
                      <div className="text-base font-black text-slate-900">
                        {ex.notaSobre10.toFixed(2)}{' '}
                        <span className="text-xs text-slate-400 font-normal">/ 10</span>
                      </div>
                      <span
                        className={`text-[10px] font-bold uppercase px-1.5 py-0.2 rounded ${
                          ex.aprobado
                            ? 'bg-emerald-100 text-emerald-800'
                            : 'bg-red-100 text-red-800'
                        }`}
                      >
                        {ex.aprobado ? 'Apto' : 'No Apto'}
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* 5. Gestión de Datos y Copias de Seguridad */}
      <div className="bg-slate-50 rounded-2xl border border-slate-200 p-5 flex flex-wrap items-center justify-between gap-4">
        <div>
          <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider">
            Almacenamiento Local del Navegador
          </h4>
          <p className="text-xs text-slate-500 mt-0.5">
            Tus datos se guardan exclusivamente en tu navegador (sin necesidad de cuentas ni servidores).
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <button
            onClick={handleExportar}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 transition-colors shadow-sm"
            title="Descargar copia de seguridad en JSON"
          >
            <Download className="h-3.5 w-3.5 text-blue-600" />
            <span>Exportar Copia</span>
          </button>

          <label className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 transition-colors shadow-sm cursor-pointer">
            <Upload className="h-3.5 w-3.5 text-indigo-600" />
            <span>Restaurar Copia</span>
            <input
              type="file"
              accept=".json"
              onChange={handleImportar}
              className="hidden"
            />
          </label>

          <button
            onClick={handleLimpiar}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold text-red-600 hover:bg-red-50 border border-transparent hover:border-red-200 transition-colors"
            title="Borrar todo el historial"
          >
            <Trash2 className="h-3.5 w-3.5" />
            <span>Limpiar Datos</span>
          </button>
        </div>
      </div>
    </div>
  );
};
