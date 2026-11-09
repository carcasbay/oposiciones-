import fs from 'fs';
import path from 'path';

export interface OpcionesPregunta {
  a: string;
  b: string;
  c: string;
  d: string;
}

export type OposicionId = 'utrera' | 'andalucia';

export interface Pregunta {
  id: string;
  temaId: number;
  temaTitulo: string;
  numero: number;
  enunciado: string;
  opciones: OpcionesPregunta;
  solucion: 'a' | 'b' | 'c' | 'd';
  justificacion: string;
  origen?: 'propio' | 'red_opositor';
  oposicionId?: OposicionId;
}

export interface TemaInfo {
  id: number;
  numero: number;
  titulo: string;
  totalPreguntas: number;
  bloque: 'comun' | 'especifico';
  oposicionId?: OposicionId;
}

function parseMarkdownTest(
  filePath: string,
  temasMarkdownDir: string,
  oposicionId: OposicionId,
  bloqueForzado?: 'comun' | 'especifico',
  idOffset: number = 0
): { tema: TemaInfo; preguntas: Pregunta[] } | null {
  const content = fs.readFileSync(filePath, 'utf-8');
  const fileName = path.basename(filePath);

  // 1. Extraer número de tema
  const fileNumMatch = fileName.match(/test_tema_(\d+)/i);
  if (!fileNumMatch) {
    console.warn(`[PARSER WARNING] No se pudo extraer número de tema de ${fileName}`);
    return null;
  }
  const temaNumero = parseInt(fileNumMatch[1], 10);

  // 2. Extraer título del tema
  let temaTitulo = '';
  const standardTitleMatch = content.match(/^#\s*TEMA\s*\d+\s*[—–-]\s*(.+)$/m);
  if (standardTitleMatch) {
    temaTitulo = standardTitleMatch[1].trim();
  } else {
    const materiaMatch = content.match(/###\s*Materia:\s*(.+)$/m);
    if (materiaMatch) {
      temaTitulo = materiaMatch[1].trim();
    } else {
      const paddedNum = temaNumero.toString().padStart(2, '0');
      let temaFile: string | undefined;
      if (fs.existsSync(temasMarkdownDir)) {
        temaFile = fs.readdirSync(temasMarkdownDir).find((f) => new RegExp(`^Tema_${paddedNum}_.*\\.md$`, 'i').test(f));
      }
      if (temaFile) {
        const rawName = temaFile.replace(/^Tema_\d+_/i, '').replace(/\.md$/i, '');
        temaTitulo = rawName.replace(/_/g, ' ');
      } else {
        temaTitulo = `Tema ${temaNumero}`;
      }
    }
  }

  // 3. Separar preguntas y soluciones
  const solucionesSplitRegex = /(?:^|\n)#{2,4}\s*(?:SOLUCIONES|TABLA DE RESPUESTAS|RESPUESTAS)[^\n]*/i;
  const solucionesSplit = content.split(solucionesSplitRegex);
  if (solucionesSplit.length < 2) {
    console.error(`[PARSER ERROR] No se encontró sección de SOLUCIONES en ${fileName}`);
    return null;
  }

  const preguntasTexto = solucionesSplit[0];
  const solucionesTexto = solucionesSplit.slice(1).join('\n');

  // 4. Parsear soluciones
  const mapaSoluciones = new Map<number, { letra: 'a' | 'b' | 'c' | 'd'; justificacion: string }>();
  const lineasSoluciones = solucionesTexto.split('\n');

  let currentSolNum: number | null = null;
  let currentLetra: 'a' | 'b' | 'c' | 'd' | null = null;
  let currentJustificacion: string[] = [];

  const flushSolucion = () => {
    if (currentSolNum !== null && currentLetra !== null) {
      let texto = currentJustificacion.join(' ').trim();
      texto = texto.replace(/^\*?Justificación\*?:\s*/i, '').trim();
      texto = texto.replace(/^\*\*\s*[—–-]?\s*/, '').trim();
      texto = texto.replace(/^[—–-]\s*/, '').trim();
      mapaSoluciones.set(currentSolNum, {
        letra: currentLetra,
        justificacion: texto,
      });
    }
    currentSolNum = null;
    currentLetra = null;
    currentJustificacion = [];
  };

  for (const rawLine of lineasSoluciones) {
    const line = rawLine.trim();
    if (!line) continue;

    const matchSol = line.match(/^(\d+)\.\s*(?:\*\*)?([a-dA-D])[\)\.]?(?:\*\*)?\s*(.*)$/i);
    if (matchSol) {
      flushSolucion();
      currentSolNum = parseInt(matchSol[1], 10);
      currentLetra = matchSol[2].toLowerCase() as 'a' | 'b' | 'c' | 'd';

      let resto = (matchSol[3] || '').trim();
      resto = resto.replace(/^\*\*\s*/, '').trim();
      resto = resto.replace(/\*\*$/, '').trim();
      resto = resto.replace(/^[—–-]\s*/, '').trim();
      resto = resto.replace(/^\*\*\s*/, '').trim();

      if (resto) {
        currentJustificacion.push(resto);
      }
    } else if (currentSolNum !== null) {
      let limpia = line.replace(/^\*?Justificación\*?:\s*/i, '').trim();
      currentJustificacion.push(limpia);
    }
  }
  flushSolucion();

  // 5. Parsear preguntas
  const lineasPreguntas = preguntasTexto.split('\n');
  const bloquesPreguntas: { numero: number; lineas: string[] }[] = [];
  let bloqueActual: { numero: number; lineas: string[] } | null = null;

  for (const line of lineasPreguntas) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    const matchHeaderPregunta = trimmed.match(/^#{2,4}\s*PREGUNTA\s*(\d+)/i);
    const matchNumeroPregunta = trimmed.match(/^(\d+)\.\s+(.*)$/);

    if (matchHeaderPregunta) {
      if (bloqueActual) {
        bloquesPreguntas.push(bloqueActual);
      }
      bloqueActual = {
        numero: parseInt(matchHeaderPregunta[1], 10),
        lineas: [],
      };
    } else if (matchNumeroPregunta && !trimmed.startsWith('**') && !/^[a-dA-D][\)\.]/.test(trimmed)) {
      if (bloqueActual) {
        bloquesPreguntas.push(bloqueActual);
      }
      bloqueActual = {
        numero: parseInt(matchNumeroPregunta[1], 10),
        lineas: [matchNumeroPregunta[2]],
      };
    } else if (bloqueActual) {
      bloqueActual.lineas.push(trimmed);
    }
  }
  if (bloqueActual) {
    bloquesPreguntas.push(bloqueActual);
  }

  // 6. Extraer enunciado y opciones de cada bloque
  const preguntas: Pregunta[] = [];

  for (const bp of bloquesPreguntas) {
    const numero = bp.numero;
    const sol = mapaSoluciones.get(numero);

    let enunciado = '';
    const opciones: Record<'a' | 'b' | 'c' | 'd', string> = { a: '', b: '', c: '', d: '' };
    let currentOpt: 'a' | 'b' | 'c' | 'd' | null = null;
    const lineasEnunciado: string[] = [];

    for (const rawLine of bp.lineas) {
      const line = rawLine.trim();
      const matchOpt = line.match(/^([a-dA-D])[\)\.\-]\s*(.*)$/);

      if (matchOpt) {
        currentOpt = matchOpt[1].toLowerCase() as 'a' | 'b' | 'c' | 'd';
        opciones[currentOpt] = matchOpt[2].trim();
      } else if (currentOpt) {
        opciones[currentOpt] += ' ' + line;
      } else {
        lineasEnunciado.push(line);
      }
    }

    enunciado = lineasEnunciado.join(' ').trim();
    enunciado = enunciado.replace(/^\*{1,2}/, '').replace(/\*{1,2}$/, '').trim();

    if (!enunciado) {
      console.warn(`[PARSER WARNING] Pregunta ${numero} de Tema ${temaNumero} (${oposicionId}) no tiene enunciado.`);
      continue;
    }

    if (!sol) {
      console.warn(`[PARSER WARNING] No se encontró solución para pregunta ${numero} de Tema ${temaNumero} (${oposicionId})`);
    }

    if (!opciones.a || !opciones.b || !opciones.c || !opciones.d) {
      console.warn(`[PARSER WARNING] Opciones incompletas en pregunta ${numero} de Tema ${temaNumero} (${oposicionId})`);
    }

    const idNum = idOffset + temaNumero;
    let idPrefix: string;
    if (oposicionId === 'andalucia') {
      idPrefix = bloqueForzado === 'comun' ? `and_c${temaNumero}` : `and_e${temaNumero}`;
    } else {
      idPrefix = `t${temaNumero}`;
    }

    preguntas.push({
      id: `${idPrefix}_q${numero}`,
      temaId: idNum,
      temaTitulo: temaTitulo,
      numero: numero,
      enunciado: enunciado,
      opciones: {
        a: opciones.a || '',
        b: opciones.b || '',
        c: opciones.c || '',
        d: opciones.d || '',
      },
      solucion: sol?.letra || 'a',
      justificacion: sol?.justificacion || '',
      origen: 'propio',
      oposicionId: oposicionId,
    });
  }

  const bloqueTipo = bloqueForzado 
    ? bloqueForzado 
    : (oposicionId === 'utrera' ? (temaNumero <= 12 ? 'comun' : 'especifico') : 'especifico');

  const temaInfo: TemaInfo = {
    id: idOffset + temaNumero,
    numero: temaNumero,
    titulo: temaTitulo,
    totalPreguntas: preguntas.length,
    bloque: bloqueTipo,
    oposicionId: oposicionId,
  };

  return { tema: temaInfo, preguntas };
}

function processDirectory(
  testsDir: string,
  temasDir: string,
  oposicionId: OposicionId,
  bloqueForzado?: 'comun' | 'especifico',
  idOffset: number = 0
): { temas: TemaInfo[]; preguntas: Pregunta[] } {
  if (!fs.existsSync(testsDir)) {
    return { temas: [], preguntas: [] };
  }

  const allFiles = fs.readdirSync(testsDir);
  const testFiles = allFiles
    .filter((f) => /^test_tema_\d+\.md$/i.test(f))
    .sort((a, b) => {
      const numA = parseInt(a.match(/\d+/)![0], 10);
      const numB = parseInt(b.match(/\d+/)![0], 10);
      return numA - numB;
    });

  const temas: TemaInfo[] = [];
  const preguntas: Pregunta[] = [];

  for (const file of testFiles) {
    const fullPath = path.join(testsDir, file);
    const resultado = parseMarkdownTest(fullPath, temasDir, oposicionId, bloqueForzado, idOffset);
    if (resultado) {
      temas.push(resultado.tema);
      preguntas.push(...resultado.preguntas);
      const tag = bloqueForzado ? `${oposicionId.toUpperCase()} ${bloqueForzado.toUpperCase()}` : oposicionId.toUpperCase();
      console.log(
        `✓ [${tag}] Tema ${resultado.tema.numero.toString().padStart(2, '0')}: ${resultado.preguntas.length} preguntas`
      );
    }
  }

  return { temas, preguntas };
}

function main() {
  const baseDir = path.resolve(__dirname, '..');
  const targetDataDir = path.resolve(baseDir, 'src', 'data');

  if (!fs.existsSync(targetDataDir)) {
    fs.mkdirSync(targetDataDir, { recursive: true });
  }

  console.log(`\n==============================================`);
  console.log(`[PARSER MULTI-OPOSICIÓN] Iniciando procesamiento...`);
  console.log(`==============================================\n`);

  // 1. Procesar Utrera
  const utreraTestsDir = path.resolve(baseDir, 'tests');
  const utreraTemasDir = path.resolve(baseDir, 'temario', 'markdown');
  const utreraData = processDirectory(utreraTestsDir, utreraTemasDir, 'utrera');

  // Importar simulacros Red Opositor para Utrera si existen
  const simulacrosROPath = path.join(targetDataDir, 'simulacros_red_opositor.json');
  if (fs.existsSync(simulacrosROPath)) {
    try {
      const roQuestions: Pregunta[] = JSON.parse(fs.readFileSync(simulacrosROPath, 'utf-8')).map((q: any) => ({
        ...q,
        oposicionId: 'utrera' as OposicionId,
      }));
      utreraData.preguntas.push(...roQuestions);
      console.log(`✓ Simulacros Red Opositor importados para Utrera: ${roQuestions.length} preguntas`);

      for (const tema of utreraData.temas) {
        tema.totalPreguntas = utreraData.preguntas.filter((q) => q.temaId === tema.id).length;
      }
    } catch (e) {
      console.error(`[PARSER ERROR] Error al cargar simulacros_red_opositor.json:`, e);
    }
  }

  // 2. Procesar Andalucía (Común + Específico)
  const andaluciaComunTestsDir = path.resolve(baseDir, 'tests_andalucia_comun');
  const andaluciaComunTemasDir = path.resolve(baseDir, 'andalucia_comun');
  const andaluciaComunData = processDirectory(andaluciaComunTestsDir, andaluciaComunTemasDir, 'andalucia', 'comun', 0);

  const andaluciaEspTestsDir = path.resolve(baseDir, 'tests_andalucia');
  const andaluciaEspTemasDir = path.resolve(baseDir, 'andalucia');
  const andaluciaEspData = processDirectory(andaluciaEspTestsDir, andaluciaEspTemasDir, 'andalucia', 'especifico', 30);

  const andaluciaData = {
    temas: [...andaluciaComunData.temas, ...andaluciaEspData.temas],
    preguntas: [...andaluciaComunData.preguntas, ...andaluciaEspData.preguntas],
  };

  // 3. Escribir archivos específicos por oposición
  fs.writeFileSync(path.join(targetDataDir, 'questions_utrera.json'), JSON.stringify(utreraData.preguntas, null, 2), 'utf-8');
  fs.writeFileSync(path.join(targetDataDir, 'temas_utrera.json'), JSON.stringify(utreraData.temas, null, 2), 'utf-8');

  fs.writeFileSync(path.join(targetDataDir, 'questions_andalucia.json'), JSON.stringify(andaluciaData.preguntas, null, 2), 'utf-8');
  fs.writeFileSync(path.join(targetDataDir, 'temas_andalucia.json'), JSON.stringify(andaluciaData.temas, null, 2), 'utf-8');

  // 4. Escribir archivos globales unificados (backward compatibility)
  const todasLasPreguntas = [...utreraData.preguntas, ...andaluciaData.preguntas];
  const todosLosTemas = [...utreraData.temas, ...andaluciaData.temas];

  fs.writeFileSync(path.join(targetDataDir, 'questions.json'), JSON.stringify(todasLasPreguntas, null, 2), 'utf-8');
  fs.writeFileSync(path.join(targetDataDir, 'temas.json'), JSON.stringify(todosLosTemas, null, 2), 'utf-8');

  console.log(`\n==============================================`);
  console.log(`[PARSER ÉXITO] Resumen del procesamiento:`);
  console.log(`- UTRERA: ${utreraData.temas.length} temas | ${utreraData.preguntas.length} preguntas`);
  console.log(`- ANDALUCÍA: ${andaluciaData.temas.length} temas (${andaluciaComunData.temas.length} comunes + ${andaluciaEspData.temas.length} específicos) | ${andaluciaData.preguntas.length} preguntas`);
  console.log(`- TOTAL COMBINADO: ${todosLosTemas.length} temas | ${todasLasPreguntas.length} preguntas`);
  console.log(`==============================================\n`);
}

main();
