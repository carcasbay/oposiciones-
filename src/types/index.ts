export type OpcionLetra = 'a' | 'b' | 'c' | 'd';

export interface OpcionesPregunta {
  a: string;
  b: string;
  c: string;
  d: string;
}

export type OrigenPreguntas = 'todos' | 'propio' | 'red_opositor';
export type OposicionId = 'utrera' | 'andalucia';

export interface Pregunta {
  id: string; // ej. "t1_q1", "and_t1_q1", "ro_q1"
  temaId: number;
  temaTitulo: string;
  numero: number;
  enunciado: string;
  opciones: OpcionesPregunta;
  solucion: OpcionLetra;
  justificacion: string;
  origen?: 'propio' | 'red_opositor';
  oposicionId?: OposicionId;
}

export interface TemaInfo {
  id: number;
  numero: number;
  titulo: string;
  totalPreguntas: number;
  bloque: 'comun' | 'especifico'; // 1-12 común, 13-60 específico para Utrera; todos específicos para Andalucía
  oposicionId?: OposicionId;
}

export type ModoExamen = 'examen' | 'estudio' | 'fallos';
export type TipoPenalizacion = 'tercio' | 'cuarto' | 'ninguna';

export interface ConfiguracionTest {
  temasSeleccionados: number[];
  numeroPreguntas: number;
  modo: ModoExamen;
  temporizadorActivo: boolean;
  tiempoTotalSegundos: number; // por defecto 54s por pregunta
  aleatorizarPreguntas: boolean;
  aleatorizarOpciones?: boolean;
  penalizacion?: TipoPenalizacion;
  origenPreguntas?: OrigenPreguntas;
  oposicionId?: OposicionId;
}

export interface RespuestaExamen {
  preguntaId: string;
  respuestaSeleccionada: OpcionLetra | null;
  esCorrecta: boolean | null; // null si no contestada
  marcadaDuda: boolean;
}

export interface DesgloseTemaResultado {
  temaId: number;
  temaTitulo: string;
  total: number;
  aciertos: number;
  errores: number;
  enBlanco: number;
  porcentajeAcierto: number;
}

export interface ResultadoExamen {
  id: string;
  fecha: string; // ISO string
  config: ConfiguracionTest;
  respuestas: Record<string, RespuestaExamen>;
  preguntas: Pregunta[];
  aciertos: number;
  errores: number;
  enBlanco: number;
  puntuacionNeta: number; // A - E/3
  notaSobre10: number; // (A - E/3)/Total * 10
  aprobado: boolean;
  tiempoTotalSegundos: number;
  tiempoEmpleadoSegundos: number;
  desglosePorTema: DesgloseTemaResultado[];
  oposicionId?: OposicionId;
}

export interface PreguntaFalladaInfo {
  preguntaId: string;
  vecesFallada: number;
  ultimaFecha: string;
  temaId: number;
  oposicionId?: OposicionId;
}

export interface HistorialUsuario {
  examenes: ResultadoExamen[];
  preguntasFalladas: Record<string, PreguntaFalladaInfo>; // clave: preguntaId
}
