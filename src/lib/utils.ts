import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { Pregunta, OpcionLetra } from '@/types';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatearTiempo(segundos: number): string {
  const mins = Math.floor(segundos / 60);
  const secs = segundos % 60;
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

export function mezclarArray<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function mezclarOpcionesPregunta(pregunta: Pregunta): Pregunta {
  const letras: OpcionLetra[] = ['a', 'b', 'c', 'd'];
  const textos = letras.map((l) => pregunta.opciones[l].toLowerCase());

  // No barajar opciones si alguna hace referencia posicional ("todas las anteriores", "a y b son correctas", etc.)
  const tieneReferenciaPosicional = textos.some(
    (t) =>
      t.includes('anteriores') ||
      t.includes('a y b') ||
      t.includes('a y c') ||
      t.includes('b y c') ||
      t.includes('ninguna de las') ||
      t.includes('todas son correctas')
  );

  if (tieneReferenciaPosicional) {
    return pregunta;
  }

  const pares = letras.map((letra) => ({
    letraOriginal: letra,
    texto: pregunta.opciones[letra],
  }));

  const mezclados = mezclarArray(pares);
  let nuevaSolucion: OpcionLetra = pregunta.solucion;

  const nuevasOpciones = {
    a: mezclados[0].texto,
    b: mezclados[1].texto,
    c: mezclados[2].texto,
    d: mezclados[3].texto,
  };

  mezclados.forEach((item, index) => {
    if (item.letraOriginal === pregunta.solucion) {
      nuevaSolucion = letras[index];
    }
  });

  return {
    ...pregunta,
    opciones: nuevasOpciones,
    solucion: nuevaSolucion,
  };
}
