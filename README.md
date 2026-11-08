# Oposiciones Educación Social · Andalucía (A2.2018) y Utrera

Plataforma web interactiva de preparación de oposiciones de **Educación Social**, desarrollada con **Next.js 15**, **React 19** y **Tailwind CSS**.

## Contenido integrado
- **Junta de Andalucía (Cuerpo Técnico Facultativo A2.2018 - Educación Social):**
  - **40 Temas Específicos** completos (`.md`, `.html` y `.pdf` en `andalucia/` y `PDFs_Para_Imprimir/`).
  - **600 preguntas oficiales tipo test** con 4 opciones equilibradas y soluciones jurídicas razonadas (`tests_andalucia/`).
- **Excmo. Ayuntamiento de Utrera (Técnico/a Medio en Educación Social):**
  - **60 Temas** (12 comunes y 48 específicos en `temario/`).
  - **1.810 preguntas tipo test** (900 de temas propios + 910 de simulacros oficiales en `tests/`).

## Comandos principales
- `npm run dev`: Compila los bancos de preguntas y arranca el servidor de desarrollo.
- `npm run parse`: Procesa los archivos Markdown de tests (`tests/` y `tests_andalucia/`) y genera los JSON estáticos en `src/data/`.
- `npm run build`: Genera la versión estática de producción lista para Vercel.
