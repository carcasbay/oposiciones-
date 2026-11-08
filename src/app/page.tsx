'use client';

import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { 
  Pregunta, 
  TemaInfo, 
  ConfiguracionTest, 
  ResultadoExamen,
  OposicionId
} from '@/types';
import questionsAndaluciaRaw from '@/data/questions_andalucia.json';
import temasAndaluciaRaw from '@/data/temas_andalucia.json';
import questionsUtreraRaw from '@/data/questions_utrera.json';
import temasUtreraRaw from '@/data/temas_utrera.json';

import { mezclarArray, mezclarOpcionesPregunta } from '@/lib/utils';
import { guardarResultadoExamen, obtenerPreguntasFalladasIds } from '@/lib/storage';
import { Navbar } from '@/components/Navbar';
import { ConfiguradorTest } from '@/components/ConfiguradorTest';
import { PantallaExamen } from '@/components/PantallaExamen';
import { PantallaResultados } from '@/components/PantallaResultados';
import { PanelEstadisticas } from '@/components/PanelEstadisticas';

type VistaApp = 'configurador' | 'examen' | 'resultados' | 'estadisticas';

export default function Home() {
  const [vista, setVista] = useState<VistaApp>('configurador');
  const [oposicionActiva, setOposicionActiva] = useState<OposicionId>('andalucia');

  // Selección de datos según la oposición activa
  const allQuestions = useMemo(() => {
    return oposicionActiva === 'andalucia'
      ? (questionsAndaluciaRaw as Pregunta[])
      : (questionsUtreraRaw as Pregunta[]);
  }, [oposicionActiva]);

  const allTemas = useMemo(() => {
    return oposicionActiva === 'andalucia'
      ? (temasAndaluciaRaw as TemaInfo[])
      : (temasUtreraRaw as TemaInfo[]);
  }, [oposicionActiva]);

  // Examen activo
  const [preguntasExamen, setPreguntasExamen] = useState<Pregunta[]>([]);
  const [configExamen, setConfigExamen] = useState<ConfiguracionTest | null>(null);

  // Último resultado generado
  const [ultimoResultado, setUltimoResultado] = useState<ResultadoExamen | null>(null);

  // Preguntas falladas en localStorage para la oposición activa
  const [falladasIds, setFalladasIds] = useState<string[]>([]);

  // Configuración preestablecida al abrir el configurador
  const [configPreestablecida, setConfigPreestablecida] = useState<Partial<ConfiguracionTest> | undefined>(undefined);

  const refrescarFalladas = useCallback(() => {
    const ids = obtenerPreguntasFalladasIds(oposicionActiva);
    setFalladasIds(ids);
  }, [oposicionActiva]);

  useEffect(() => {
    refrescarFalladas();
  }, [refrescarFalladas]);

  // Manejo de cambio de oposición
  const handleCambiarOposicion = (nuevaOposicion: OposicionId) => {
    if (nuevaOposicion === oposicionActiva) return;

    if (vista === 'examen') {
      const confirmar = window.confirm(
        'Tienes un examen en curso. ¿Deseas cancelarlo y cambiar de oposición?'
      );
      if (!confirmar) return;
    }

    setOposicionActiva(nuevaOposicion);
    setConfigPreestablecida(undefined);
    setPreguntasExamen([]);
    setConfigExamen(null);
    setUltimoResultado(null);
    setVista('configurador');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Iniciar un nuevo examen con la configuración seleccionada
  const handleIniciarTest = (config: ConfiguracionTest) => {
    let pool: Pregunta[] = [];

    let baseQuestions = allQuestions;
    if (oposicionActiva !== 'andalucia') {
      if (config.origenPreguntas === 'propio') {
        baseQuestions = allQuestions.filter((q) => q.origen === 'propio');
      } else if (config.origenPreguntas === 'red_opositor') {
        baseQuestions = allQuestions.filter((q) => q.origen === 'red_opositor');
      }
    }

    if (config.modo === 'fallos') {
      const idsSet = new Set(falladasIds);
      pool = baseQuestions.filter((q) => idsSet.has(q.id));
    } else {
      const temasSet = new Set(config.temasSeleccionados);
      pool = baseQuestions.filter((q) => temasSet.has(q.temaId));
    }

    if (pool.length === 0) {
      alert('No se encontraron preguntas para los temas seleccionados.');
      return;
    }

    // Aleatorizar si está marcado
    if (config.aleatorizarPreguntas) {
      pool = mezclarArray(pool);
    }

    // Limitar al número de preguntas configurado
    let seleccionadas = pool.slice(0, config.numeroPreguntas);

    // Barajar las opciones (a, b, c, d) dentro de cada pregunta si está activado (por defecto true)
    if (config.aleatorizarOpciones !== false) {
      seleccionadas = seleccionadas.map(mezclarOpcionesPregunta);
    }

    const configConOposicion: ConfiguracionTest = {
      ...config,
      oposicionId: oposicionActiva,
    };

    setPreguntasExamen(seleccionadas);
    setConfigExamen(configConOposicion);
    setVista('examen');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Finalizar examen y procesar resultado
  const handleFinalizarExamen = (resultado: ResultadoExamen) => {
    const resultadoConOposicion = {
      ...resultado,
      oposicionId: oposicionActiva,
    };
    guardarResultadoExamen(resultadoConOposicion);
    refrescarFalladas();
    setUltimoResultado(resultadoConOposicion);
    setVista('resultados');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Repetir el examen recién concluido con la misma configuración
  const handleRepetirMismoTest = () => {
    if (configExamen) {
      handleIniciarTest(configExamen);
    } else {
      setVista('configurador');
    }
  };

  // Iniciar test desde el radar de temas flojos
  const handleIniciarTestConTemas = (temasIds: number[]) => {
    setConfigPreestablecida({
      temasSeleccionados: temasIds,
      numeroPreguntas: 15,
      modo: 'examen',
      oposicionId: oposicionActiva,
    });
    setVista('configurador');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Iniciar test directo con la bolsa de fallos
  const handleIniciarModoFallos = () => {
    refrescarFalladas();
    if (falladasIds.length === 0) {
      alert('Actualmente no tienes preguntas en tu bolsa de fallos para esta oposición.');
      return;
    }
    handleIniciarTest({
      temasSeleccionados: allTemas.map((t) => t.id),
      numeroPreguntas: Math.min(20, falladasIds.length),
      modo: 'fallos',
      temporizadorActivo: false,
      tiempoTotalSegundos: Math.min(20, falladasIds.length) * 54,
      aleatorizarPreguntas: true,
      oposicionId: oposicionActiva,
    });
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar
        vistaActual={vista}
        onCambiarVista={(v) => {
          setVista(v);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }}
        enExamen={vista === 'examen'}
        totalTemas={allTemas.length}
        totalPreguntas={allQuestions.length}
        falladasCount={falladasIds.length}
        onIniciarModoFallos={falladasIds.length > 0 ? handleIniciarModoFallos : undefined}
        oposicionActiva={oposicionActiva}
        onCambiarOposicion={handleCambiarOposicion}
      />

      <main className="flex-1">
        {vista === 'configurador' && (
          <ConfiguradorTest
            key={oposicionActiva}
            temas={allTemas}
            totalPreguntasDisponibles={allQuestions.length}
            preguntasFalladasCount={falladasIds.length}
            onIniciarTest={handleIniciarTest}
            configInicial={configPreestablecida}
            oposicionId={oposicionActiva}
          />
        )}

        {vista === 'examen' && configExamen && (
          <PantallaExamen
            preguntas={preguntasExamen}
            config={configExamen}
            onFinalizarExamen={handleFinalizarExamen}
            onCancelarExamen={() => setVista('configurador')}
          />
        )}

        {vista === 'resultados' && ultimoResultado && (
          <PantallaResultados
            resultado={ultimoResultado}
            onRepetirTest={handleRepetirMismoTest}
            onNuevoTest={() => {
              setConfigPreestablecida(undefined);
              setVista('configurador');
            }}
            onVerEstadisticas={() => setVista('estadisticas')}
          />
        )}

        {vista === 'estadisticas' && (
          <PanelEstadisticas
            key={oposicionActiva}
            temas={allTemas}
            onIniciarTestConTemas={handleIniciarTestConTemas}
            onIniciarModoFallos={handleIniciarModoFallos}
            onNuevoTest={() => {
              setConfigPreestablecida(undefined);
              setVista('configurador');
            }}
            oposicionId={oposicionActiva}
          />
        )}
      </main>

      {/* Pie de página institucional */}
      {vista !== 'examen' && (
        <footer className="border-t border-slate-200 bg-white py-6 mt-12 text-center text-xs text-slate-500">
          <div className="max-w-7xl mx-auto px-4 space-y-1">
            <p className="font-semibold text-slate-700">
              {oposicionActiva === 'andalucia'
                ? 'Junta de Andalucía · Cuerpo de Técnicos Facultativos de Grado Medio (A2.2018 Educación Social)'
                : 'Excmo. Ayuntamiento de Utrera · Subescala Técnica Media de Administración Especial (Educación Social)'}
            </p>
            <p>
              {oposicionActiva === 'andalucia'
                ? 'Conforme a la Orden de 21 de noviembre de 2022 (BOJA extraordinario nº 35) · Temario Específico Oficial (40 temas)'
                : 'Conforme a las bases publicadas en el BOP de Sevilla nº 102 · Convocatoria 2024 (60 temas: 12 comunes y 48 específicos)'}
            </p>
            <p className="text-[11px] text-slate-400">
              Single-Page App 100% Estática · Datos compilados en build time · Historial persistido de forma independiente por oposición en tu navegador
            </p>
          </div>
        </footer>
      )}
    </div>
  );
}
