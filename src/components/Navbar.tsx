'use client';

import React from 'react';
import { BookOpen, BarChart3, AlertCircle, Sparkles, Building2, Landmark } from 'lucide-react';
import { OposicionId } from '@/types';

interface NavbarProps {
  vistaActual: 'configurador' | 'examen' | 'resultados' | 'estadisticas';
  onCambiarVista: (vista: 'configurador' | 'estadisticas') => void;
  enExamen: boolean;
  totalTemas: number;
  totalPreguntas: number;
  falladasCount: number;
  onIniciarModoFallos?: () => void;
  oposicionActiva: OposicionId;
  onCambiarOposicion: (op: OposicionId) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  vistaActual,
  onCambiarVista,
  enExamen,
  totalTemas,
  totalPreguntas,
  falladasCount,
  onIniciarModoFallos,
  oposicionActiva,
  onCambiarOposicion,
}) => {
  const esAndalucia = oposicionActiva === 'andalucia';

  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-200 bg-white/95 backdrop-blur shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-2">
        {/* Identidad */}
        <div className="flex items-center gap-3">
          <div
            className={`h-10 w-10 rounded-lg flex items-center justify-center text-white shadow-md transition-colors ${
              esAndalucia
                ? 'bg-emerald-600 shadow-emerald-500/20'
                : 'bg-blue-600 shadow-blue-500/20'
            }`}
          >
            <BookOpen className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold text-slate-900 tracking-tight text-base sm:text-lg">
                {esAndalucia ? 'Oposiciones Andalucía' : 'Oposiciones Utrera'}
              </span>
              <span
                className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold border ${
                  esAndalucia
                    ? 'bg-emerald-50 text-emerald-800 border-emerald-200'
                    : 'bg-blue-50 text-blue-700 border-blue-200'
                }`}
              >
                {esAndalucia ? 'Junta · A2.2018' : 'Ayto. · A2'}
              </span>
            </div>
            <p className="text-xs text-slate-500 hidden sm:block">
              {totalTemas} temas · {totalPreguntas} preguntas oficiales
            </p>
          </div>
        </div>

        {/* Selector de Oposición (Pestañas directas) */}
        {!enExamen && (
          <div className="flex items-center bg-slate-100 p-1 rounded-xl border border-slate-200 text-xs font-semibold">
            <button
              onClick={() => onCambiarOposicion('andalucia')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg transition-all ${
                esAndalucia
                  ? 'bg-white text-emerald-800 shadow-sm font-bold border border-emerald-200'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-200/60'
              }`}
            >
              <Landmark className={`h-3.5 w-3.5 ${esAndalucia ? 'text-emerald-600' : 'text-slate-500'}`} />
              <span>Andalucía (70)</span>
            </button>
            <button
              onClick={() => onCambiarOposicion('utrera')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg transition-all ${
                !esAndalucia
                  ? 'bg-white text-blue-800 shadow-sm font-bold border border-blue-200'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-200/60'
              }`}
            >
              <Building2 className={`h-3.5 w-3.5 ${!esAndalucia ? 'text-blue-600' : 'text-slate-500'}`} />
              <span>Utrera (60)</span>
            </button>
          </div>
        )}

        {/* Acciones y navegación (si no estamos en mitad de un examen activo) */}
        {!enExamen ? (
          <nav className="flex items-center gap-2">
            <button
              onClick={() => onCambiarVista('configurador')}
              className={`flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                vistaActual === 'configurador'
                  ? esAndalucia
                    ? 'bg-emerald-600 text-white shadow-sm'
                    : 'bg-blue-600 text-white shadow-sm'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
              }`}
            >
              <Sparkles className="h-4 w-4" />
              <span className="hidden sm:inline">Nuevo Test</span>
            </button>

            {falladasCount > 0 && onIniciarModoFallos && (
              <button
                onClick={onIniciarModoFallos}
                className="hidden md:flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium text-amber-700 bg-amber-50 hover:bg-amber-100 border border-amber-200 transition-colors"
                title="Hacer test solo con preguntas que has fallado"
              >
                <AlertCircle className="h-4 w-4 text-amber-600" />
                <span>Fallos ({falladasCount})</span>
              </button>
            )}

            <button
              onClick={() => onCambiarVista('estadisticas')}
              className={`flex items-center gap-2 px-3 sm:px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                vistaActual === 'estadisticas'
                  ? esAndalucia
                    ? 'bg-emerald-600 text-white shadow-sm'
                    : 'bg-blue-600 text-white shadow-sm'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
              }`}
            >
              <BarChart3 className="h-4 w-4" />
              <span className="hidden sm:inline">Estadísticas</span>
            </button>
          </nav>
        ) : (
          <div className="flex items-center gap-2 text-xs font-medium text-amber-700 bg-amber-50 border border-amber-200 px-3 py-1.5 rounded-full">
            <span className="h-2 w-2 rounded-full bg-amber-500 animate-ping"></span>
            <span>Examen en curso</span>
          </div>
        )}
      </div>
    </header>
  );
};
