'use client';

import React, { useState, useMemo, useEffect } from 'react';
import { TemaInfo, ConfiguracionTest, ModoExamen, OrigenPreguntas, OposicionId, TipoPenalizacion } from '@/types';
import { 
  CheckSquare, 
  Square, 
  Timer, 
  BookOpen, 
  AlertTriangle, 
  Play, 
  Layers, 
  Filter, 
  Shuffle, 
  Clock,
  Sparkles,
  Database,
  Landmark,
  Building2
} from 'lucide-react';

interface ConfiguradorTestProps {
  temas: TemaInfo[];
  totalPreguntasDisponibles: number;
  preguntasFalladasCount: number;
  onIniciarTest: (config: ConfiguracionTest) => void;
  configInicial?: Partial<ConfiguracionTest>;
  oposicionId: OposicionId;
}

export const ConfiguradorTest: React.FC<ConfiguradorTestProps> = ({
  temas,
  totalPreguntasDisponibles,
  preguntasFalladasCount,
  onIniciarTest,
  configInicial,
  oposicionId,
}) => {
  const esAndalucia = oposicionId === 'andalucia';

  // Estado de temas seleccionados
  const [temasSeleccionados, setTemasSeleccionados] = useState<number[]>(() => {
    if (configInicial?.temasSeleccionados && configInicial.temasSeleccionados.length > 0) {
      return configInicial.temasSeleccionados;
    }
    return temas.map((t) => t.id);
  });

  // Modo
  const [modo, setModo] = useState<ModoExamen>(configInicial?.modo || 'examen');

  // Banco de preguntas
  const [origenPreguntas, setOrigenPreguntas] = useState<OrigenPreguntas>(
    configInicial?.origenPreguntas || 'todos'
  );

  // Opciones de preguntas
  const [numeroPreguntas, setNumeroPreguntas] = useState<number>(() => {
    return configInicial?.numeroPreguntas || (esAndalucia ? 20 : 20);
  });

  const [temporizadorActivo, setTemporizadorActivo] = useState<boolean>(true);
  const [segundosPorPregunta, setSegundosPorPregunta] = useState<number>(54); // 54s oficial (90 min / 100 preg)
  const [aleatorizar, setAleatorizar] = useState<boolean>(true);
  const [aleatorizarOpciones, setAleatorizarOpciones] = useState<boolean>(
    configInicial?.aleatorizarOpciones ?? true
  );
  const [penalizacion, setPenalizacion] = useState<TipoPenalizacion>(
    configInicial?.penalizacion || 'tercio'
  );

  // Filtro de búsqueda de temas en la lista
  const [busquedaTema, setBusquedaTema] = useState<string>('');

  // Reiniciar selección de temas y filtros al cambiar de oposición
  useEffect(() => {
    if (configInicial?.temasSeleccionados && configInicial.temasSeleccionados.length > 0) {
      setTemasSeleccionados(configInicial.temasSeleccionados);
    } else {
      setTemasSeleccionados(temas.map((t) => t.id));
    }
    setOrigenPreguntas('todos');
    setBusquedaTema('');
  }, [oposicionId, temas, configInicial]);

  // Preguntas totales de los temas seleccionados
  const preguntasEnTemasSeleccionados = useMemo(() => {
    return temas
      .filter((t) => temasSeleccionados.includes(t.id))
      .reduce((acc, curr) => acc + curr.totalPreguntas, 0);
  }, [temas, temasSeleccionados]);

  // Selección rápida de temas
  const seleccionarTodos = () => setTemasSeleccionados(temas.map((t) => t.id));
  const deseleccionarTodos = () => setTemasSeleccionados([]);

  // Utrera shortcuts
  const seleccionarComunesUtrera = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun').map((t) => t.id));
  const seleccionarEspecificosUtrera = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'especifico').map((t) => t.id));

  // Andalucía shortcuts
  const seleccionarComunesAndalucia = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun').map((t) => t.id));
  const seleccionarEspecificosAndalucia = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'especifico').map((t) => t.id));

  const seleccionarComunesB1 = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun' && t.numero >= 1 && t.numero <= 9).map((t) => t.id));
  const seleccionarComunesB2 = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun' && t.numero >= 10 && t.numero <= 17).map((t) => t.id));
  const seleccionarComunesB3 = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun' && t.numero >= 18 && t.numero <= 23).map((t) => t.id));
  const seleccionarComunesB4 = () =>
    setTemasSeleccionados(temas.filter((t) => t.bloque === 'comun' && t.numero >= 24 && t.numero <= 30).map((t) => t.id));

  const toggleTema = (id: number) => {
    setTemasSeleccionados((prev) =>
      prev.includes(id) ? prev.filter((t) => t !== id) : [...prev, id]
    );
  };

  const temasFiltrados = useMemo(() => {
    if (!busquedaTema.trim()) return temas;
    const q = busquedaTema.toLowerCase();
    return temas.filter(
      (t) =>
        t.numero.toString().includes(q) ||
        t.titulo.toLowerCase().includes(q)
    );
  }, [temas, busquedaTema]);

  // Cantidad efectiva de preguntas
  const cantidadEfectiva = useMemo(() => {
    if (modo === 'fallos') {
      return Math.min(numeroPreguntas, preguntasFalladasCount);
    }
    return Math.min(numeroPreguntas, preguntasEnTemasSeleccionados);
  }, [modo, numeroPreguntas, preguntasFalladasCount, preguntasEnTemasSeleccionados]);

  const tiempoTotalCalculado = useMemo(() => {
    return cantidadEfectiva * segundosPorPregunta;
  }, [cantidadEfectiva, segundosPorPregunta]);

  const handleLanzarSimulacroOficial = () => {
    onIniciarTest({
      temasSeleccionados: temas.map((t) => t.id),
      numeroPreguntas: esAndalucia ? 100 : 100,
      modo: 'examen',
      temporizadorActivo: true,
      tiempoTotalSegundos: 5400, // 90 minutos oficiales
      aleatorizarPreguntas: true,
      aleatorizarOpciones: true,
      penalizacion,
      origenPreguntas: esAndalucia ? 'propio' : 'todos',
      oposicionId,
    });
  };

  const handleComenzar = () => {
    if (modo !== 'fallos' && temasSeleccionados.length === 0) {
      alert('Por favor, selecciona al menos un tema para realizar el examen.');
      return;
    }
    if (cantidadEfectiva <= 0) {
      alert('No hay preguntas disponibles con la selección actual.');
      return;
    }

    onIniciarTest({
      temasSeleccionados,
      numeroPreguntas: cantidadEfectiva,
      modo,
      temporizadorActivo: modo === 'examen' ? temporizadorActivo : false,
      tiempoTotalSegundos: tiempoTotalCalculado,
      aleatorizarPreguntas: aleatorizar,
      aleatorizarOpciones,
      penalizacion,
      origenPreguntas: esAndalucia ? 'propio' : origenPreguntas,
      oposicionId,
    });
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      {/* Cabecera */}
      <div className="mb-6 text-center sm:text-left flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            {esAndalucia ? (
              <>
                <Landmark className="h-7 w-7 text-emerald-600 inline" />
                <span>Oposición Junta de Andalucía</span>
              </>
            ) : (
              <>
                <Building2 className="h-7 w-7 text-blue-600 inline" />
                <span>Oposición Ayuntamiento de Utrera</span>
              </>
            )}
          </h1>
          <p className="mt-1 text-sm sm:text-base text-slate-600">
            {esAndalucia
              ? 'Cuerpo Técnico Facultativo A2.2018 (Educación Social) · 70 Temas (30 Comunes + 40 Específicos)'
              : 'Técnico/a Medio en Educación Social A2 · 60 Temas (12 Comunes + 48 Específicos)'}
          </p>
        </div>
        <div className="inline-flex self-center sm:self-auto items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border shadow-sm bg-white">
          <span className={`h-2.5 w-2.5 rounded-full ${esAndalucia ? 'bg-emerald-500' : 'bg-blue-500'}`}></span>
          <span className="text-slate-700">{totalPreguntasDisponibles} preguntas oficiales</span>
        </div>
      </div>

      {/* Banner destacado: Simulacro Oficial */}
      <div
        className={`mb-8 p-5 sm:p-6 rounded-2xl text-white shadow-lg flex flex-col md:flex-row items-center justify-between gap-4 transition-all ${
          esAndalucia
            ? 'bg-gradient-to-r from-emerald-700 via-teal-800 to-emerald-950'
            : 'bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-800'
        }`}
      >
        <div className="space-y-1 text-center md:text-left">
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-white/20 text-white backdrop-blur-sm">
            <Sparkles className="h-3.5 w-3.5 text-amber-300" />
            <span>{esAndalucia ? 'Convocatoria Oficial Junta de Andalucía' : 'Convocatoria Oficial Utrera (BOP 102)'}</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-black tracking-tight">
            Simulacro Real de Examen (100 preguntas · 90 min)
          </h2>
          <p className="text-xs sm:text-sm text-slate-100 max-w-xl">
            {esAndalucia
              ? 'Formato oficial del examen de la Junta: 100 preguntas tipo test sobre materias comunes y específicas, penalización oficial y cronómetro real de 90 minutos.'
              : 'Formato oficial de Utrera: 100 preguntas aleatorias tipo test (comunes y específicos), penalización oficial (-0,33 por fallo) y 90 minutos.'}
          </p>
        </div>
        <button
          type="button"
          onClick={handleLanzarSimulacroOficial}
          className="whitespace-nowrap px-6 py-3.5 rounded-xl font-bold text-sm sm:text-base bg-amber-400 hover:bg-amber-300 text-slate-950 shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center gap-2 cursor-pointer"
        >
          <Play className="h-5 w-5 fill-current" />
          <span>Iniciar Simulacro Oficial</span>
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Columna Izquierda: Opciones del examen */}
        <div className="lg:col-span-7 space-y-6">
          {/* Tarjeta: Origen del Banco de Preguntas (solo para Utrera que tiene Red Opositor) */}
          {!esAndalucia && (
            <div className="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200 shadow-sm">
              <h2 className="text-base font-bold text-slate-900 flex items-center gap-2 mb-3">
                <Database className="h-5 w-5 text-blue-600" />
                <span>Banco de Preguntas</span>
              </h2>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: 'todos', label: 'Todos', sub: '1.810 preg.' },
                  { id: 'propio', label: 'Temas Propios', sub: '900 preg.' },
                  { id: 'red_opositor', label: 'Red Opositor', sub: '910 preg.' },
                ].map((banco) => (
                  <button
                    key={banco.id}
                    type="button"
                    onClick={() => setOrigenPreguntas(banco.id as OrigenPreguntas)}
                    className={`p-3 rounded-xl border text-center transition-all ${
                      origenPreguntas === banco.id
                        ? 'bg-blue-50 border-blue-500 ring-2 ring-blue-500/20 text-blue-900 font-bold'
                        : 'border-slate-200 hover:border-slate-300 text-slate-600'
                    }`}
                  >
                    <div className="text-xs font-semibold">{banco.label}</div>
                    <div className="text-[11px] text-slate-400">{banco.sub}</div>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Tarjeta: Modo de Estudio */}
          <div className="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200 shadow-sm">
            <h2 className="text-base font-bold text-slate-900 flex items-center gap-2 mb-3">
              <Layers className={`h-5 w-5 ${esAndalucia ? 'text-emerald-600' : 'text-blue-600'}`} />
              <span>Modalidad de Test</span>
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <button
                type="button"
                onClick={() => setModo('examen')}
                className={`p-4 rounded-xl border text-left transition-all ${
                  modo === 'examen'
                    ? esAndalucia
                      ? 'bg-emerald-50 border-emerald-500 ring-2 ring-emerald-500/20 text-emerald-950 font-bold'
                      : 'bg-blue-50 border-blue-500 ring-2 ring-blue-500/20 text-blue-950 font-bold'
                    : 'border-slate-200 hover:border-slate-300 text-slate-700'
                }`}
              >
                <div className="text-sm font-semibold mb-1">Modo Examen</div>
                <div className="text-xs text-slate-500">Corrección final con nota oficial, temporizador y penalización.</div>
              </button>

              <button
                type="button"
                onClick={() => setModo('estudio')}
                className={`p-4 rounded-xl border text-left transition-all ${
                  modo === 'estudio'
                    ? esAndalucia
                      ? 'bg-emerald-50 border-emerald-500 ring-2 ring-emerald-500/20 text-emerald-950 font-bold'
                      : 'bg-blue-50 border-blue-500 ring-2 ring-blue-500/20 text-blue-950 font-bold'
                    : 'border-slate-200 hover:border-slate-300 text-slate-700'
                }`}
              >
                <div className="text-sm font-semibold mb-1">Modo Estudio</div>
                <div className="text-xs text-slate-500">Corrección inmediata tras responder con justificación legal en cada pregunta.</div>
              </button>

              <button
                type="button"
                onClick={() => setModo('fallos')}
                className={`p-4 rounded-xl border text-left transition-all ${
                  modo === 'fallos'
                    ? 'bg-amber-50 border-amber-500 ring-2 ring-amber-500/20 text-amber-950 font-bold'
                    : 'border-slate-200 hover:border-slate-300 text-slate-700'
                }`}
              >
                <div className="text-sm font-semibold mb-1 flex items-center justify-between">
                  <span>Modo Fallos</span>
                  <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-amber-200 text-amber-800">
                    {preguntasFalladasCount}
                  </span>
                </div>
                <div className="text-xs text-slate-500">Repasa exclusivamente las preguntas que has fallado en exámenes previos.</div>
              </button>
            </div>
          </div>

          {/* Tarjeta: Parámetros del Test */}
          <div className="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200 shadow-sm space-y-5">
            <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
              <Clock className={`h-5 w-5 ${esAndalucia ? 'text-emerald-600' : 'text-blue-600'}`} />
              <span>Número de Preguntas y Tiempo</span>
            </h2>

            {/* Número de preguntas */}
            <div>
              <label className="text-xs font-semibold text-slate-700 block mb-2">
                Número de preguntas para este test:
              </label>
              <div className="flex flex-wrap gap-2">
                {[10, 15, 20, 30, 50, 100].map((num) => (
                  <button
                    key={num}
                    type="button"
                    onClick={() => setNumeroPreguntas(num)}
                    className={`px-3.5 py-2 rounded-xl text-xs font-semibold border transition-all ${
                      numeroPreguntas === num
                        ? esAndalucia
                          ? 'bg-emerald-600 text-white border-emerald-600 shadow-sm'
                          : 'bg-blue-600 text-white border-blue-600 shadow-sm'
                        : 'border-slate-200 hover:border-slate-300 text-slate-700'
                    }`}
                  >
                    {num} preguntas
                  </button>
                ))}
              </div>
            </div>

            {/* Temporizador */}
            {modo === 'examen' && (
              <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <div className="text-sm font-semibold text-slate-900">Activar temporizador oficial</div>
                  <div className="text-xs text-slate-500">54 segundos por pregunta (ritmo oficial del examen).</div>
                </div>
                <label className="relative inline-flex items-center cursor-pointer">
                  <input
                    type="checkbox"
                    checked={temporizadorActivo}
                    onChange={(e) => setTemporizadorActivo(e.target.checked)}
                    className="sr-only peer"
                  />
                  <div className={`w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all ${
                    esAndalucia ? 'peer-checked:bg-emerald-600' : 'peer-checked:bg-blue-600'
                  }`}></div>
                </label>
              </div>
            )}

            {/* Aleatorización de preguntas */}
            <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
              <div>
                <div className="text-sm font-semibold text-slate-900">Aleatorizar preguntas</div>
                <div className="text-xs text-slate-500">Mezcla el orden de las preguntas en cada intento.</div>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={aleatorizar}
                  onChange={(e) => setAleatorizar(e.target.checked)}
                  className="sr-only peer"
                />
                <div className={`w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all ${
                  esAndalucia ? 'peer-checked:bg-emerald-600' : 'peer-checked:bg-blue-600'
                }`}></div>
              </label>
            </div>

            {/* Aleatorización de opciones (a, b, c, d) */}
            <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
              <div>
                <div className="text-sm font-semibold text-slate-900">Barajar opciones (a, b, c, d)</div>
                <div className="text-xs text-slate-500">Cambia dinámicamente la posición de las 4 respuestas.</div>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={aleatorizarOpciones}
                  onChange={(e) => setAleatorizarOpciones(e.target.checked)}
                  className="sr-only peer"
                />
                <div className={`w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all ${
                  esAndalucia ? 'peer-checked:bg-emerald-600' : 'peer-checked:bg-blue-600'
                }`}></div>
              </label>
            </div>

            {/* Fórmula de penalización */}
            <div className="pt-4 border-t border-slate-100">
              <label className="text-xs font-semibold text-slate-700 block mb-2">
                Penalización por error:
              </label>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: 'tercio', label: '-1/3 (Estándar)', sub: '3 fallos = -1 acierto' },
                  { id: 'cuarto', label: '-1/4 (IAAP)', sub: '4 fallos = -1 acierto' },
                  { id: 'ninguna', label: 'Sin resta', sub: 'Estabilización' },
                ].map((p) => (
                  <button
                    key={p.id}
                    type="button"
                    onClick={() => setPenalizacion(p.id as TipoPenalizacion)}
                    className={`p-2.5 rounded-xl border text-center transition-all ${
                      penalizacion === p.id
                        ? esAndalucia
                          ? 'bg-emerald-50 border-emerald-500 ring-2 ring-emerald-500/20 text-emerald-950 font-bold'
                          : 'bg-blue-50 border-blue-500 ring-2 ring-blue-500/20 text-blue-950 font-bold'
                        : 'border-slate-200 hover:border-slate-300 text-slate-600'
                    }`}
                  >
                    <div className="text-xs font-semibold">{p.label}</div>
                    <div className="text-[10px] text-slate-400">{p.sub}</div>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Columna Derecha: Selección de Temas */}
        <div className="lg:col-span-5 space-y-4">
          <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col h-[520px]">
            <div className="flex items-center justify-between mb-2">
              <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
                <Filter className={`h-4 w-4 ${esAndalucia ? 'text-emerald-600' : 'text-blue-600'}`} />
                <span>Selección de Temas ({temasSeleccionados.length}/{temas.length})</span>
              </h2>
            </div>

            {/* Botones de selección rápida */}
            <div className="flex flex-wrap gap-1.5 mb-3">
              <button
                type="button"
                onClick={seleccionarTodos}
                className="px-2.5 py-1 text-xs font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-md transition-colors"
              >
                Todos ({temas.length})
              </button>
              <button
                type="button"
                onClick={deseleccionarTodos}
                className="px-2.5 py-1 text-xs font-medium text-red-600 hover:bg-red-50 rounded-md transition-colors"
              >
                Ninguno
              </button>

              {esAndalucia ? (
                <>
                  <button
                    type="button"
                    onClick={seleccionarComunesAndalucia}
                    className="px-2.5 py-1 text-xs font-semibold bg-emerald-100 hover:bg-emerald-200 text-emerald-900 rounded-md border border-emerald-300 transition-colors"
                  >
                    Comunes (1-30)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarEspecificosAndalucia}
                    className="px-2.5 py-1 text-xs font-semibold bg-emerald-100 hover:bg-emerald-200 text-emerald-900 rounded-md border border-emerald-300 transition-colors"
                  >
                    Específicos (1-40)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarComunesB1}
                    className="px-2 py-1 text-[11px] font-medium bg-emerald-50 hover:bg-emerald-100 text-emerald-800 rounded-md border border-emerald-200"
                    title="Temas Comunes 1 a 9: Constitución, Estatuto y Órganos"
                  >
                    Común B1 (1-9)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarComunesB2}
                    className="px-2 py-1 text-[11px] font-medium bg-emerald-50 hover:bg-emerald-100 text-emerald-800 rounded-md border border-emerald-200"
                    title="Temas Comunes 10 a 17: Procedimiento y Contratos"
                  >
                    Común B2 (10-17)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarComunesB3}
                    className="px-2 py-1 text-[11px] font-medium bg-emerald-50 hover:bg-emerald-100 text-emerald-800 rounded-md border border-emerald-200"
                    title="Temas Comunes 18 a 23: Función Pública y Hacienda"
                  >
                    Común B3 (18-23)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarComunesB4}
                    className="px-2 py-1 text-[11px] font-medium bg-emerald-50 hover:bg-emerald-100 text-emerald-800 rounded-md border border-emerald-200"
                    title="Temas Comunes 24 a 30: Digital, PRL e Igualdad"
                  >
                    Común B4 (24-30)
                  </button>
                </>
              ) : (
                <>
                  <button
                    type="button"
                    onClick={seleccionarComunesUtrera}
                    className="px-2.5 py-1 text-xs font-medium bg-blue-50 hover:bg-blue-100 text-blue-800 rounded-md border border-blue-200"
                  >
                    Comunes (1-12)
                  </button>
                  <button
                    type="button"
                    onClick={seleccionarEspecificosUtrera}
                    className="px-2.5 py-1 text-xs font-medium bg-blue-50 hover:bg-blue-100 text-blue-800 rounded-md border border-blue-200"
                  >
                    Específicos (13+)
                  </button>
                </>
              )}
            </div>

            {/* Buscador de temas */}
            <div className="mb-2">
              <input
                type="text"
                placeholder="Buscar por número o título..."
                value={busquedaTema}
                onChange={(e) => setBusquedaTema(e.target.value)}
                className="w-full text-xs px-3 py-2 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-slate-400"
              />
            </div>

            {/* Lista scrollable de temas */}
            <div className="flex-1 overflow-y-auto space-y-1.5 pr-1 border border-slate-100 rounded-xl p-2 bg-slate-50/50">
              {temasFiltrados.map((tema) => {
                const seleccionado = temasSeleccionados.includes(tema.id);
                return (
                  <div
                    key={tema.id}
                    onClick={() => toggleTema(tema.id)}
                    className={`flex items-start gap-2.5 p-2 rounded-lg cursor-pointer text-left transition-all ${
                      seleccionado
                        ? esAndalucia
                          ? 'bg-emerald-50/80 border border-emerald-200 text-slate-900'
                          : 'bg-blue-50/80 border border-blue-200 text-slate-900'
                        : 'bg-white border border-slate-200/70 hover:border-slate-300 text-slate-600'
                    }`}
                  >
                    <div className="mt-0.5">
                      {seleccionado ? (
                        <CheckSquare className={`h-4 w-4 ${esAndalucia ? 'text-emerald-600' : 'text-blue-600'}`} />
                      ) : (
                        <Square className="h-4 w-4 text-slate-400" />
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-1.5">
                        <span className={`font-bold text-xs ${esAndalucia ? 'text-emerald-900' : 'text-blue-900'}`}>
                          {tema.bloque === 'comun' ? 'C' : 'E'}{tema.numero.toString().padStart(2, '0')}
                        </span>
                        <span className="text-[10px] font-medium px-1.5 py-0.2 rounded bg-white border border-slate-200 text-slate-500">
                          {tema.bloque === 'comun' ? 'Común' : 'Específico'}
                        </span>
                        <span className="text-[10px] text-slate-400 ml-auto">
                          {tema.totalPreguntas} preg.
                        </span>
                      </div>
                      <p className="text-xs text-slate-700 truncate mt-0.5" title={tema.titulo}>
                        {tema.titulo}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Botón Comenzar Test */}
          <div
            className={`p-5 rounded-2xl shadow-lg text-white space-y-4 transition-all ${
              esAndalucia
                ? 'bg-gradient-to-br from-emerald-600 to-teal-800'
                : 'bg-gradient-to-br from-blue-600 to-indigo-700'
            }`}
          >
            <div className="flex justify-between items-center text-sm border-b border-white/20 pb-3">
              <span className="text-slate-100">Preguntas del test:</span>
              <span className="font-bold text-lg">{cantidadEfectiva}</span>
            </div>
            <div className="flex justify-between items-center text-sm">
              <span className="text-slate-100">Modalidad:</span>
              <span className="font-medium capitalize bg-white/10 px-2 py-0.5 rounded text-xs">
                {modo === 'examen' ? 'Simulacro Oficial' : modo === 'estudio' ? 'Modo Estudio' : 'Repaso de Fallos'}
              </span>
            </div>

            <button
              type="button"
              onClick={handleComenzar}
              disabled={cantidadEfectiva === 0}
              className={`w-full py-3.5 px-6 rounded-xl font-bold text-base flex items-center justify-center gap-2 shadow-md transition-all ${
                cantidadEfectiva === 0
                  ? 'bg-slate-300 text-slate-500 cursor-not-allowed'
                  : esAndalucia
                  ? 'bg-white text-emerald-800 hover:bg-emerald-50 active:scale-[0.98]'
                  : 'bg-white text-blue-700 hover:bg-blue-50 active:scale-[0.98]'
              }`}
            >
              <Play className="h-5 w-5 fill-current" />
              <span>Comenzar Examen</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
