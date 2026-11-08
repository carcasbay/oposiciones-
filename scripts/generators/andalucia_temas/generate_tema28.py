import os
from build_theme import compile_pdf

md_content = """# TEMA 28: La Investigación en Educación Social. El Rol de Investigador/a del Educador/a Social. Paradigmas y Métodos. Estrategias y Técnicas de Recogida de Datos. Análisis de Datos. La Investigación-Acción Participativa. El Informe de Investigación. Investigación sobre Problemas y Cuestiones Fundamentales Relacionadas con el Sistema Educativo

---

## FICHA TÉCNICA DEL TEMA
* **Cuerpo:** Cuerpo Técnico Facultativo de la Junta de Andalucía
* **Especialidad:** Educación Social (A2.2018)
* **Carácter:** Materias Específicas del Programa Oficial
* **Marco Legal y Documental:**
  - Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA), arts. 4, 131 y 133 (Evaluación, innovación e investigación educativa).
  - Ley Orgánica 2/2006 (LOE), modificada por la LOMLOE 3/2020.
  - Instrucciones de 17 de septiembre de 2010 de la Dirección General de Participación e Innovación Educativa.
* **Autores y Doctrinas de Referencia:** Donald Schön (El profesional reflexivo), Kurt Lewin (Investigación-Acción y ciclos de cambio), Orlando Fals Borda (Investigación-Acción Participativa - IAP comunitaria), Barney Glaser y Anselm Strauss (Grounded Theory / Teoría Fundamentada), Thomas Kuhn (Estructura de las revoluciones científicas y paradigmas).

---

## ÍNDICE DE CONTENIDOS
1. Introducción y estatuto de la investigación en la práctica de la Educación Social.
2. El rol de investigador/a del educador o educadora social: El práctico reflexivo (Donald Schön).
3. Paradigmas de investigación en las Ciencias Sociales y de la Educación:
   - 3.1. Paradigma positivista o empírico-analítico (cuantitativo).
   - 3.2. Paradigma interpretativo o hermenéutico (cualitativo).
   - 3.3. Paradigma sociocrítico o emancipador (participativo).
4. Estrategias y técnicas de recogida de datos en el ámbito escolar:
   - 4.1. Técnicas cuantitativas: Cuestionarios, escalas Likert e indicadores estadísticos de Séneca.
   - 4.2. Técnicas cualitativas: Observación participante, entrevistas en profundidad, grupos de discusión e historias de vida.
   - 4.3. El principio de triangulación como criterio de validez y rigor científico.
5. Análisis de datos en la investigación socioeducativa:
   - 5.1. Análisis cuantitativo descriptivo e inferencial.
   - 5.2. Análisis cualitativo de contenido: Categorización y codificación.
6. La Investigación-Acción Participativa (IAP) como metodología nuclear:
   - 6.1. Orígenes y fundamentos (Kurt Lewin y Orlando Fals Borda).
   - 6.2. La espiral dialéctica: Planificar, actuar, observar y reflexionar.
   - 6.3. Aplicación de la IAP en la comunidad escolar andaluza.
7. El informe de investigación socioeducativa y la devolución social de resultados.
8. Líneas prioritarias de investigación sobre el sistema educativo andaluz (convivencia, absentismo, brecha digital, inclusión).
9. Conclusión.
10. Anexo: Mapa conceptual y tabla sinóptica del Tema 28.

---

## 1. Introducción y estatuto de la investigación en la Educación Social

La investigación en Educación Social no es una actividad puramente teórica reservada a los laboratorios universitarios o a la academia distante; constituye una **dimensión inherente e irrenunciable de la práctica profesional cotidiana**. No es posible transformar una realidad socioeducativa que no se comprende en profundidad, ni es éticamente aceptable intervenir en la vida de menores y familias sin evaluar con rigor empírico el impacto real de las acciones desplegadas.

Para la **Educación Social**, investigar es un **acto pedagógico y político de concienciación y cambio social**. La investigación socioeducativa se caracteriza por su carácter contextualizado, aplicado y transformador: busca generar conocimiento útil para desvelar las causas estructurales del fracaso escolar, desmontar prejuicios clasistas y capacitar a la comunidad educativa para que asuma el protagonismo en la resolución de sus propios desafíos (Orlando Fals Borda).

En Andalucía, la LEA (arts. 131 a 133) consagra la investigación y la innovación educativa como motores de la calidad de la enseñanza pública, encomendando al personal técnico del centro el análisis reflexivo de sus prácticas.

---

## 2. El rol de investigador/a del educador/a social: El práctico reflexivo

Frente a la concepción tradicional del educador como mero ejecutor mecánico de instrucciones dictadas por otros, Donald Schön formuló el concepto del **profesional reflexivo**:
* **Reflexión EN la acción:** Capacidad de reajustar la intervención en tiempo real mientras se interactúa con el alumno, el grupo o la familia, interpretando imprevistos y resistencias.
* **Reflexión SOBRE la acción:** Análisis crítico posterior, sistemático y distanciado sobre lo acontecido, contrastando los resultados observados con las hipótesis iniciales.
* El Educador Social actúa como un **investigador en el aula y en la comunidad**: diagnostica problemáticas complejas, prueba estrategias pedagógicas innovadoras y documenta rigurosamente sus hallazgos.

---

## 3. Paradigmas de investigación en las Ciencias Sociales

Siguiendo la epistemología científica contemporánea (Thomas Kuhn, Habermas), se diferencian tres grandes paradigmas:

```
                  PARADIGMAS DE INVESTIGACIÓN SOCIOEDUCATIVA
 ┌──────────────────────┬──────────────────────┬──────────────────────┐
 │ PARADIGMA POSITIVISTA│ PARADIGMA INTERPRET. │ PARADIGMA SOCIOCRÍT. │
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ • Finalidad: Explicar│ • Finalidad: Compren-│ • Finalidad: Trans-  │
 │   y predecir causas  │   der significados   │   formar y emancipar │
 │ • Enfoque cuantitat. │ • Enfoque cualitat.  │ • Enfoque dialógico  │
 │ • Neutralidad / test │ • Empatía hermenéut. │ • IAP / Coinvestigac.│
 │ • Datos numéricos    │ • Discurso y vivencia│ • Unión teoría-praxis│
 └──────────────────────┴──────────────────────┴──────────────────────┘
```

1. **Paradigma Positivista / Cuantitativo:** Busca leyes generales y relaciones de causa-efecto. Emplea la estadística, el control de variables y el cuestionario estandarizado. Valioso para conocer tasas macro de absentismo o repetición en Andalucía.
2. **Paradigma Interpretativo / Cualitativo:** Centrado en comprender los significados subjetivos que los actores otorgan a sus vivencias (¿qué siente un menor al sufrir acoso escolar?). Emplea la entrevista abierta y la observación etnográfica.
3. **Paradigma Sociocrítico / Emancipador:** Paradigma de referencia para la Educación Social. Rechaza la pretendida neutralidad valorativa: la ciencia debe servir para denunciar injusticias y liberar a los colectivos oprimidos mediante la unión indisociable de teoría y práctica (praxis).

---

## 4. Estrategias y técnicas de recogida de datos en la escuela

### 4.1. Técnicas Cuantitativas
* **Cuestionarios e Inventarios Cerrados:** Recogida masiva de datos con preguntas estructuradas (escalas Likert de 1 a 5).
* **Indicadores Estadísticos de Gestión Escolar:** Explotación sistemática de series temporales de la plataforma *Séneca* (tasas de absentismo mensual, partes de incidencias, notas por materias y género).

### 4.2. Técnicas Cualitativas
* **Observación Participante:** Inmersión del educador social en los escenarios naturales (el patio, el comedor, los pasillos) registrando conductas espontáneas en su diario de campo.
* **Entrevistas en Profundidad y Semiestructuradas:** Diálogo guiado para rescatar relatos biográficos y dinámicas sociofamiliares.
* **Grupos de Discusión (Focus Groups):** Reuniones colectivas de debate entre estudiantes o familias para hacer emerger discursos compartidos.
* **Historias de Vida:** Reconstrucción longitudinal de la trayectoria escolar y vital de jóvenes en riesgo.

### 4.3. La Triangulación como Criterio de Rigor Metodológico
Para evitar sesgos subjetivos, la Educación Social exige la **triangulación metodológica**: contrastar datos cuantitativos (estadísticas de faltas) con datos cualitativos (entrevistas al alumno y familia) y con la observación directa del equipo docente.

---

## 5. Análisis de datos en la investigación socioeducativa

1. **Análisis Cuantitativo:** Tratamiento estadístico descriptivo (medias, porcentajes, desviaciones típicas) e inferencial (pruebas chi-cuadrado, correlaciones de Pearson) mediante software como SPSS o herramientas abiertas.
2. **Análisis Cualitativo de Contenido:** Procedimiento riguroso de categorización y codificación textual (Glaser y Strauss):
   - *Codificación abierta:* Identificación de unidades de significado en las transcripciones.
   - *Codificación axial:* Agrupación de códigos en categorías temáticas emergentes.
   - *Codificación selectiva:* Construcción de un modelo explicativo teórico fundamentado en los datos.

---

## 6. La Investigación-Acción Participativa (IAP)

La **Investigación-Acción Participativa (IAP)**, concebida por Kurt Lewin y refundada en América Latina por Orlando Fals Borda, es la metodología insignia de la Educación Social comunitaria:
* **Ruptura de la Relación Sujeto-Objeto:** La comunidad educativa (alumnado, familias, docentes y vecinos) no es "objeto pasivo de estudio", sino **sujeto coinvestigador activo**.
* **La Espiral Dialéctica de Lewin:** Proceso cíclico continuo estructurado en cuatro fases recurrentes:

```
                    ESPIRAL DIALÉCTICA DE LA IAP (LEWIN)
                ┌─────────────────────────────────┐
                │ 1. PLANIFICAR (Plan de acción)  │
                └───────────────┬─────────────────┘
                                ▼
                ┌─────────────────────────────────┐
                │ 2. ACTUAR (Ejecución comunitar.)│
                └───────────────┬─────────────────┘
                                ▼
                ┌─────────────────────────────────┐
                │ 3. OBSERVAR (Recogida de datos) │
                └───────────────┬─────────────────┘
                                ▼
                ┌─────────────────────────────────┐
                │ 4. REFLEXIONAR (Reajuste crítico│
                └───────────────┬─────────────────┘
                                │
                    (Vuelve al ciclo siguiente)
```

### Aplicación Práctica en la Escuela Andaluza
Creación de una **Comisión Mixta de Investigación** (alumnado de ESO, docentes, AMPA y educador social) para investigar participativamente los conflictos del patio escolar, diseñando los propios alumnos las zonas de juego y las normas de convivencia compartidas.

---

## 7. El informe de investigación y la devolución social

El proceso científico culmina con la redacción del **informe técnico de investigación**:
* **Estructura Académica Canónica:** Título, introducción y justificación, marco teórico conceptual, diseño metodológico (muestra, técnicas y análisis), exposición de resultados, discusión crítica y propuestas operativas de mejora para el centro docente.
* **Principio de Devolución Social (Fals Borda):** El conocimiento generado no puede quedar archivado en una estantería burocrática; debe ser "devuelto" a la comunidad escolar en asambleas participativas, talleres de barrio y reuniones de claustro en un lenguaje accesible y motivador para la acción.

---

## 8. Cuestiones e investigaciones prioritarias en el sistema educativo andaluz

La Educación Social investiga sobre problemáticas vivas de alto impacto en Andalucía:
1. **Convivencia y Ciberodio:** Prevalencia de dinámicas de acoso escolar en redes sociales y discursos de odio xenófobos o lgtbifóbicos en la adolescencia.
2. **Factores Críticos del Absentismo Escolar:** Análisis cualitativo de las causas que sostienen la desvinculación escolar en barrios de transformación social (Estrategia ERACIS).
3. **Brecha Digital y Equidad Familiar:** Estudio del impacto de la falta de competencias y dispositivos digitales en hogares vulnerables.
4. **Coeducación y Masculinidades Juveniles:** Efectos del consumo precoz de pornografía online en las relaciones afectivas adolescentes.

---

## 9. Conclusión

La investigación en Educación Social no es un adorno académico ni un ejercicio estéril de erudición; es la **fuerza intelectual que permite fundamentar la justicia social con datos irrefutables y transformar la realidad con rigor ético**.

El **Educador y la Educadora Social** como práctico reflexivo investiga con el corazón en la comunidad y la mente en la ciencia: escucha la voz de los silenciados, somete su práctica a examen continuo y convierte la investigación-acción en un instrumento insuperable de libertad, equidad y dignidad educativa.

---

## 10. Anexo: Mapa conceptual y tabla sinóptica del Tema 28

| Eje Temático | Normativa / Doctrinas Clave | Conceptos e Implicación Práctica |
| :--- | :--- | :--- |
| **Práctico Reflexivo** | Donald Schön | Reflexión en la acción y sobre la acción; el profesional como investigador permanente. |
| **Paradigmas Científicos** | Thomas Kuhn • Jürgen Habermas | Positivista (cuantitativo/leyes), Interpretativo (cualitativo/comprensión) y Sociocrítico (emancipación). |
| **Técnicas Cuantitativas** | Cuestionarios • Séneca | Indicadores macro, estadísticas de absentismo y escalas de actitudes estandarizadas. |
| **Técnicas Cualitativas** | Observación • Entrevista • Grupos | Diario de campo etnográfico, entrevistas en profundidad y análisis de contenido temático. |
| **Triangulación Metodológica** | Criterio de validez empírica | Contraste cruzado de datos cuantitativos, testimonios cualitativos y observación de campo. |
| **La IAP** | Kurt Lewin • Orlando Fals Borda | Ciclos dialécticos de planificar-actuar-observar-reflexionar. El sujeto como coinvestigador. |
| **Devolución Social** | Fals Borda • LEA (arts. 131-133) | Retorno pedagógico del conocimiento a la comunidad escolar para activar la acción transformadora. |
| **Rol del Educador/a Social** | Instrucciones de 17 de septiembre de 2010 | Investigador de aula y comunidad, dinamizador de la IAP y redactor de propuestas de mejora. |
"""

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 28 - La Investigación en Educación Social. Rol Investigador. Paradigmas. Técnicas. IAP. Informe de Investigación</title>
  <style>
    @page {
      size: A4;
      margin: 20mm 18mm 20mm 18mm;
      @bottom-right {
        content: counter(page);
      }
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1f2937;
      line-height: 1.6;
      font-size: 11pt;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
    }

    .cover {
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-height: 85vh;
      border-left: 6px solid #7c3aed;
      padding-left: 30px;
      margin-top: 40px;
    }

    .badge {
      display: inline-block;
      background: #f5f3ff;
      color: #6d28d9;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 10pt;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 24px;
      width: fit-content;
      border: 1px solid #ddd6fe;
    }

    .cover h1 {
      font-size: 26pt;
      line-height: 1.25;
      color: #0f172a;
      margin: 0 0 16px 0;
      font-weight: 800;
    }

    .cover h2 {
      font-size: 13pt;
      font-weight: 400;
      color: #4b5563;
      margin: 0 0 35px 0;
      line-height: 1.5;
    }

    .meta-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 18px 22px;
      font-size: 10pt;
      color: #334155;
      max-width: 500px;
    }

    .meta-box p {
      margin: 4px 0;
    }

    h2.section-title {
      color: #6d28d9;
      font-size: 14pt;
      font-weight: 700;
      border-bottom: 2px solid #c4b5fd;
      padding-bottom: 6px;
      margin-top: 30px;
      margin-bottom: 14px;
      page-break-after: avoid;
    }

    h3.sub-title {
      color: #7c3aed;
      font-size: 12pt;
      font-weight: 600;
      margin-top: 20px;
      margin-bottom: 10px;
      page-break-after: avoid;
    }

    p {
      margin-top: 0;
      margin-bottom: 12px;
      text-align: justify;
    }

    ul, ol {
      margin-top: 0;
      margin-bottom: 14px;
      padding-left: 24px;
    }

    li {
      margin-bottom: 6px;
    }

    strong {
      color: #0f172a;
      font-weight: 600;
    }

    .callout {
      background: #f5f3ff;
      border-left: 4px solid #7c3aed;
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      margin: 16px 0;
      font-size: 10.5pt;
      page-break-inside: avoid;
    }

    .callout-title {
      font-weight: 700;
      color: #6d28d9;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .compare-container {
      display: flex;
      gap: 16px;
      margin: 16px 0;
      page-break-inside: avoid;
    }

    .compare-box {
      flex: 1;
      padding: 14px;
      border-radius: 8px;
      font-size: 10pt;
    }

    .compare-purple {
      background-color: #f5f3ff;
      border: 1px solid #ddd6fe;
      border-top: 4px solid #7c3aed;
    }

    .compare-rose {
      background-color: #fff1f2;
      border: 1px solid #fecdd3;
      border-top: 4px solid #e11d48;
    }

    .compare-box h4 {
      margin: 0 0 8px 0;
      font-size: 11pt;
      font-weight: 700;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 9pt;
      page-break-inside: auto;
    }

    tr {
      page-break-inside: avoid;
      page-break-after: auto;
    }

    th {
      background: #6d28d9;
      color: #ffffff;
      font-weight: 600;
      text-align: left;
      padding: 10px 12px;
      border: 1px solid #6d28d9;
    }

    td {
      padding: 8px 10px;
      border: 1px solid #e2e8f0;
      vertical-align: top;
    }

    tr:nth-child(even) td {
      background-color: #f8fafc;
    }

    .toc-container {
      page-break-after: always;
      margin-top: 20px;
    }

    .toc-title {
      font-size: 17pt;
      color: #6d28d9;
      font-weight: 700;
      border-bottom: 2px solid #7c3aed;
      padding-bottom: 8px;
      margin-bottom: 20px;
    }

    .toc-list {
      list-style-type: none;
      padding-left: 0;
    }

    .toc-item {
      display: flex;
      align-items: baseline;
      padding: 8px 12px;
      margin-bottom: 6px;
      border-radius: 6px;
      background: #f8fafc;
      border: 1px solid #f1f5f9;
    }

    .toc-num {
      font-weight: 800;
      color: #7c3aed;
      width: 32px;
      flex-shrink: 0;
    }

    .toc-text {
      color: #1e293b;
      font-weight: 500;
    }

    .page-break {
      page-break-before: always;
    }
  </style>
</head>
<body>

  <!-- PORTADA -->
  <div class="cover">
    <div class="badge">Oposiciones Junta de Andalucía • A2.2018</div>
    <h1>TEMA 28</h1>
    <h2>La investigación en Educación Social. El rol de investigador/a del educador/a social. Paradigmas y métodos. Estrategias y técnicas de recogida de datos. Análisis de datos. La Investigación-Acción Participativa. El informe de investigación. Temas clave en el sistema educativo</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> Ley 17/2007 (LEA, arts. 4, 131-133); LOMLOE 3/2020; Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Donald Schön (Práctico reflexivo), Kurt Lewin, Orlando Fals Borda (IAP), Barney Glaser y Anselm Strauss</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 28</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y estatuto de la investigación en la práctica de la Educación Social</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">El rol de investigador/a del educador/a social: El práctico reflexivo (Donald Schön)</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">Paradigmas de investigación en Ciencias Sociales: Positivista, interpretativo y sociocrítico</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">Técnicas de recogida de datos y el principio de triangulación metodológica</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">Análisis de datos cuantitativos y cualitativos en el centro docente</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">La Investigación-Acción Participativa (IAP): Fundamentos y ciclos de Lewin</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">El informe de investigación socioeducativa y la devolución social de resultados</span></li>
      <li class="toc-item"><span class="toc-num">08</span><span class="toc-text">Cuestiones prioritarias de investigación en el sistema educativo andaluz</span></li>
      <li class="toc-item"><span class="toc-num">09</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 28</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y estatuto de la investigación en la Educación Social</h2>
  <p>
    La investigación en Educación Social no es un mero aditamento académico desvinculado de la realidad cotidiana; constituye un <strong>componente estructural irrenunciable para garantizar la calidad, el rigor ético y la eficacia de la acción pedagógica</strong>. No es posible transformar aquello que no se comprende a fondo, ni es ético intervenir sobre colectivos vulnerables sin evaluar sistemáticamente las consecuencias reales de las medidas aplicadas.
  </p>
  <p>
    Para la Educación Social, investigar es un **acto transformador y participativo** orientado a desvelar las barreras estructurales que generan desigualdad en la escuela pública andaluza (Orlando Fals Borda).
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. El rol de investigador/a del educador/a social: El práctico reflexivo (Donald Schön)</h2>
  <ul>
    <li><strong>Reflexión EN la acción:</strong> Reajuste inmediato de las dinámicas socioeducativas mientras se interactúa en el aula o el patio.</li>
    <li><strong>Reflexión SOBRE la acción:</strong> Análisis crítico y distanciado una vez finalizada la intervención, contrastando resultados con hipótesis previas para optimizar la praxis.</li>
    <li>El educador/a social como <strong>investigador situado</strong>: detecta problemas en la cotidianidad escolar, formula hipótesis socioeducativas y documenta con rigor empírico los cambios alcanzados.</li>
  </ul>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. Paradigmas de investigación en Ciencias Sociales</h2>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">PARADIGMA POSITIVISTA E INTERPRETATIVO</h4>
      <p>
        • <em>Positivista (Cuantitativo):</em> Explicación causal, datos numéricos de Séneca, escalas estandarizadas y generalización estadística.<br>
        • <em>Interpretativo (Cualitativo):</em> Comprensión fenomenológica del significado subjetivo de las vivencias del alumnado (entrevistas en profundidad).
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">PARADIGMA SOCIOCRÍTICO O EMANCIPADOR</h4>
      <p>
        • Paradigma nuclear de la Educación Social.<br>
        • Rompe la neutralidad valorativa: la investigación debe transformar la realidad escolar y erradicar las opresiones estructurales mediante la IAP.
      </p>
    </div>
  </div>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. Técnicas de recogida de datos y triangulación metodológica</h2>
  <ul>
    <li><strong>Cuantitativas:</strong> Cuestionarios tipo Likert sobre clima de aula y explotación estadística de registros de absentismo y sanciones en <em>Séneca</em>.</li>
    <li><strong>Cualitativas:</strong> Observación participante con notas y diario de campo, entrevistas sociofamiliares semiestructuradas, historias de vida y grupos de discusión.</li>
    <li><strong>Triangulación Metodológica:</strong> Cruce contrastado de datos cuantitativos, testimonios cualitativos y observaciones docentes para garantizar la validez científica y eliminar sesgos subjetivos.</li>
  </ul>

  <!-- SECCIÓN 5 -->
  <div class="page-break"></div>
  <h2 class="section-title">5. Análisis de datos en la investigación socioeducativa</h2>
  <p>
    Tratamiento analítico con rigor científico:
  </p>
  <ul>
    <li><strong>Análisis Cuantitativo:</strong> Estadística descriptiva (frecuencias, porcentajes, correlaciones) para dimensionar problemáticas escolares masivas.</li>
    <li><strong>Análisis Cualitativo de Contenido:</strong> Proceso riguroso de codificación abierta, axial y selectiva (Glaser y Strauss) para generar categorías conceptuales a partir de los discursos de las familias y estudiantes.</li>
  </ul>

  <!-- SECCIÓN 6 -->
  <h2 class="section-title">6. La Investigación-Acción Participativa (IAP): Fundamentos y ciclos de Lewin</h2>
  <p>
    La <strong>IAP</strong> (Kurt Lewin y Orlando Fals Borda) es la metodología transformadora por excelencia de la Educación Social comunitaria:
  </p>
  <div class="callout">
    <div class="callout-title">Los Ciclos Dialécticos de la IAP</div>
    <p>
      1. <strong>Planificar:</strong> Diagnóstico participativo conjunto del problema escolar con los implicados.<br>
      2. <strong>Actuar:</strong> Puesta en marcha de las acciones educativas acordadas colectivamente.<br>
      3. <strong>Observar:</strong> Registro sistemático de las transformaciones y resistencias observadas.<br>
      4. <strong>Reflexionar:</strong> Evaluación compartida en asamblea para reajustar el siguiente ciclo de cambio.
    </p>
  </div>

  <!-- SECCIÓN 7 -->
  <div class="page-break"></div>
  <h2 class="section-title">7. El informe de investigación socioeducativa y la devolución social</h2>
  <p>
    El rigor científico exige redactar un **informe técnico formal** (introducción, marco teórico, diseño metodológico, resultados empíricos, discusión y propuestas para el PEC).
  </p>
  <p>
    Asimismo, el <strong>principio de devolución social (Fals Borda)</strong> mandata que los resultados sean devueltos a la comunidad educativa (estudiantes, familias y claustro) en formatos claros y accesibles para impulsar la movilización democrática del centro.
  </p>

  <!-- SECCIÓN 8 -->
  <h2 class="section-title">8. Cuestiones prioritarias de investigación en el sistema educativo andaluz</h2>
  <ul>
    <li>Prevalencia del ciberacoso y los discursos de odio en redes sociales adolescentes.</li>
    <li>Causas socioestructurales del absentismo crónico en zonas desfavorecidas (ERACIS).</li>
    <li>Impacto de la brecha digital en el rendimiento y la cohesión de las familias vulnerables.</li>
    <li>Efectos del consumo precoz de pornografía violenta online en la convivencia coeducativa.</li>
  </ul>

  <!-- SECCIÓN 9 -->
  <h2 class="section-title">9. Conclusión</h2>
  <p>
    La investigación en Educación Social no busca la acumulación teórica vana ni el distanciamiento tecnocrático; es la **herramienta imprescindible para dotar de evidencia empírica a la justicia social**.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> como investigador reflexivo une la precisión de la ciencia con el compromiso por los más desfavorecidos, construyendo una escuela pública andaluza basada en el conocimiento riguroso, la participación democrática y la dignidad humana.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 28</h2>
  <p>Resumen estructurado de paradigmas, técnicas de recogida, IAP e investigación en el sistema educativo:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Eje Temático</th>
        <th style="width: 38%;">Normativa y Doctrinas Clave</th>
        <th style="width: 37%;">Conceptos e Implicación Práctica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Práctico Reflexivo</strong></td>
        <td>Donald Schön</td>
        <td>Reflexión en la acción y sobre la acción; el profesional como investigador de su propia práctica.</td>
      </tr>
      <tr>
        <td><strong>Paradigmas</strong></td>
        <td>Thomas Kuhn • Jürgen Habermas</td>
        <td>Positivista (cuantitativo/control), Interpretativo (cualitativo/comprensión) y Sociocrítico (emancipación).</td>
      </tr>
      <tr>
        <td><strong>Técnicas Cuantitativas</strong></td>
        <td>Cuestionarios • Séneca</td>
        <td>Estadísticas de faltas, correlaciones descriptivas e indicadores de rendimiento por género y etnia.</td>
      </tr>
      <tr>
        <td><strong>Técnicas Cualitativas</strong></td>
        <td>Observación • Entrevistas • Grupos</td>
        <td>Diario de campo, entrevistas en profundidad, grupos de discusión y categorización temática.</td>
      </tr>
      <tr>
        <td><strong>Triangulación</strong></td>
        <td>Criterio de validez empírica</td>
        <td>Cruce sistemático de fuentes de información, técnicas cualitativas y cuantitativas para evitar sesgos.</td>
      </tr>
      <tr>
        <td><strong>La IAP</strong></td>
        <td>Kurt Lewin • Orlando Fals Borda</td>
        <td>Espiral de planificar, actuar, observar y reflexionar. La comunidad como sujeto coinvestigador.</td>
      </tr>
      <tr>
        <td><strong>Devolución Social</strong></td>
        <td>Orlando Fals Borda • LEA (arts. 131-133)</td>
        <td>Retorno del conocimiento a la comunidad educativa para activar la acción transformadora del PEC.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Investigador situado en el centro, dinamizador de IAP comunitaria y autor de propuestas evaluadas.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

md_path = "andalucia/Tema_28_Investigacion_Educacion_Social_Metodos_IAP.md"
html_path = "andalucia/Tema_28_Investigacion_Educacion_Social_Metodos_IAP.html"
pdf_path = "andalucia/Tema_28_Investigacion_Educacion_Social_Metodos_IAP.pdf"

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")
compile_pdf(html_path, pdf_path)
