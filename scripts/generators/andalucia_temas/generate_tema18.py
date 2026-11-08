import os
from build_theme import compile_pdf

md_content = """# TEMA 18: Aspectos e Implicaciones Socioeducativas de la Diversidad. Condicionantes y Características Personales del Alumnado Relevantes para el Desarrollo del Aprendizaje. Atención a la Diversidad desde la Educación Social en los Centros Educativos. Ámbitos de Intervención. El Enfoque Preventivo de los Problemas Escolares. La Escuela Inclusiva como Respuesta Socioeducativa. Programas Institucionales para la Atención a las Necesidades Socioeducativas Asociados a Contextos Socioculturales Desfavorecidos o a Situaciones Personales

---

## FICHA TÉCNICA DEL TEMA
* **Cuerpo:** Cuerpo Técnico Facultativo de la Junta de Andalucía
* **Especialidad:** Educación Social (A2.2018)
* **Carácter:** Materias Específicas del Programa Oficial
* **Marco Legal y Documental:**
  - Ley Orgánica 2/2006 (LOE), modificada por la LOMLOE 3/2020 (Título II, Equidad en la Educación).
  - Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA), Título III (Equidad en la Educación).
  - Decretos 100/2023, 101/2023 y 102/2023 (Currículo y atención a las diferencias individuales en Infantil, Primaria y Secundaria en Andalucía).
  - Orden de 15 de enero de 2021 (Atención a la diversidad en Andalucía) e Instrucciones anuales de inicio de curso.
  - Instrucciones de 17 de septiembre de 2010 de la Dirección General de Participación e Innovación Educativa.
* **Autores y Doctrinas de Referencia:** Tony Booth y Mel Ainscow (*Index for Inclusion* / Barreras para el aprendizaje y la participación), Gerardo Echeita (Educación inclusiva), Ignacio Calderón Almendros (Educación y exclusión social), CAST (Diseño Universal para el Aprendizaje - DUA).

---

## ÍNDICE DE CONTENIDOS
1. Introducción y fundamentación socioeducativa de la diversidad humana.
2. Aspectos e implicaciones socioeducativas de la diversidad: Del modelo del déficit a la pedagogía inclusiva.
3. Condicionantes y características personales del alumnado relevantes para el aprendizaje:
   - 3.1. Tipología de Necesidades Específicas de Apoyo Educativo (NEAE) en la LOMLOE y normativa andaluza.
   - 3.2. Situación de desventaja sociocultural y vulnerabilidad socioeconómica.
4. La escuela inclusiva como respuesta socioeducativa:
   - 4.1. Diferencias esenciales entre exclusión, segregación, integración e inclusión.
   - 4.2. El modelo de barreras al aprendizaje y la participación (Booth y Ainscow).
   - 4.3. El Diseño Universal para el Aprendizaje (DUA) como paradigma didáctico.
5. El enfoque preventivo de las dificultades y desajustes escolares.
6. Programas institucionales de atención a las necesidades socioeducativas en Andalucía:
   - 6.1. Compensación educativa y Programa PROA+ / Transfórmate.
   - 6.2. Aulas Temporales de Adaptación Lingüística (ATAL) y acogida al alumnado migrante.
   - 6.3. Aulas Hospitalarias y Atención Educativa Domiciliaria.
7. Ámbitos de actuación e intervención del educador o educadora social en la diversidad escolar.
8. Conclusión.
9. Anexo: Mapa conceptual y tabla sinóptica del Tema 18.

---

## 1. Introducción y fundamentación socioeducativa de la diversidad humana

La diversidad no constituye una anomalía estadística, una perturbación curricular ni una categoría marginal atribuible a un grupo específico de estudiantes: **la diversidad es la característica constitutiva y definitoria de la condición humana y de toda comunidad educativa**. Todo ser humano aprende desde una biografía única, modulada por sus capacidades biopsicosociales, su capital cultural y lingüístico, su ritmo madurativo y las circunstancias socioeconómicas de su núcleo familiar.

Durante décadas, los sistemas escolares operaron bajo una ideología homogeneizadora de corte asimilacionista, considerando las diferencias individuales y socioculturales como un "hándicap" que requería segregación o asimilación forzada. La **Educación Social** aporta una ruptura epistemológica radical: la diversidad es un **valor educativo de primer orden y una exigencia innegociable de justicia distributiva y derechos humanos**.

En Andalucía, comunidad histórica de enorme riqueza cultural y acusadas brechas socioeconómicas territoriales, la escuela pública asume el reto de garantizar una **educación inclusiva, equitativa y de calidad**. En este escenario, el Educador y la Educadora Social ejerce un papel determinante como facilitador de la inclusión, desmontando las barreras institucionales, relacionales y sociofamiliares que obstaculizan el éxito y la participación de todo el alumnado.

---

## 2. Aspectos e implicaciones socioeducativas de la diversidad

El abordaje socioeducativo de la diversidad exige superar el **modelo médico-rehabilitador del déficit**, que culpabiliza a la persona o a su familia de las dificultades de aprendizaje, para abrazar el **modelo social y relacional de la inclusión**:
* Las dificultades no residen de forma intrínseca en el estudiante, sino en la **interacción dialéctica entre sus características personales y las barreras físicas, actitudinales y curriculares** que el propio entorno escolar y social le impone (Booth y Ainscow).
* El éxito escolar no es solo un logro cognitivo individual, sino el resultado del acceso equitativo a oportunidades socioeducativas de calidad.

---

## 3. Condicionantes y características personales del alumnado

El alumnado que requiere una atención educativa diferente a la ordinaria se agrupa bajo el concepto de **Alumnado con Necesidad Específica de Apoyo Educativo (NEAE)** (LOMLOE, art. 71):

```
                   TIPOLOGÍA DEL ALUMNADO CON NEAE (LOMLOE Y LEA)
 ┌──────────────────────┬──────────────────────┬──────────────────────┐
 │ NECESIDADES EDUCAT.  │ CIRCUNSTANCIAS       │ ALTAS CAPACIDADES Y  │
 │ ESPECIALES (NEE)     │ SOCIOFAMILIARES      │ OTRAS CONDICIONES    │
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ • Discapacidad física│ • Desventaja socio-  │ • Altas capacidades  │
 │   psíquica o sensorial cultural o económica │   intelectuales (AACC)│
 │ • Trastorno espectro │ • Incorporación      │ • Trastornos graves  │
 │   autista (TEA)      │   tardía al sistema  │   del lenguaje / TDAH│
 │ • Graves trastornos  │ • Situación de tutela│ • Retraso madurativo │
 │   de conducta / salud│   o riesgo social    │   (etapa infantil)   │
 └──────────────────────┴──────────────────────┴──────────────────────┘
```

### 3.1. Condicionantes personales y del desarrollo
* **Ritmos biológicos y cognitivos heterogéneos:** Procesamiento de la información, memoria de trabajo, estilo de aprendizaje (visual, auditivo, kinestésico).
* **Neurodiversidad:** Comprender el autismo, el TDAH o la dislexia como variaciones naturales del neurodesarrollo que exigen adaptaciones metodológicas y accesibilidad cognitiva.

### 3.2. Situación de desventaja sociocultural y vulnerabilidad socioeconómica
Factores sociofamiliares de alto impacto:
* **Pobreza material y precariedad habitacional:** Falta de espacio digno de estudio, carencia de conectividad digital en el hogar (*brecha digital*) y malnutrición infantil.
* **Bajo capital formativo de los progenitores:** Dificultad para apoyar las tareas escolares y escasa vinculación afectiva con la cultura académica formal.
* **Minorías étnicas e infancias migrantes:** Duelo migratorio, barreras idiomáticas y choque cultural entre las pautas familiares y las normas escolares.

---

## 4. La escuela inclusiva como respuesta socioeducativa

### 4.1. Evolución de los paradigmas educativos
1. **Exclusión:** Negación absoluta del derecho a la educación escolar para personas diversas.
2. **Segregación:** Escolarización en centros separados o aulas gueto especiales.
3. **Integración:** El alumno diverso accede al aula ordinaria, pero es él quien debe adaptarse al ritmo rígido de la escuela; si fracasa, la culpa es suya.
4. **Inclusión:** La escuela se transforma estructuralmente para acoger y dar respuesta a las necesidades de **todas las personas**, sin distinciones.

### 4.2. El Modelo de Barreras al Aprendizaje y la Participación (Booth y Ainscow)
El *Index for Inclusion* sustituye el concepto patologizante de "alumno con necesidades" por el de **barreras que el centro debe erradicar**:
* **Barreras Políticas:** Leyes, normativas o normativas internas excluyentes.
* **Barreras Culturales:** Prejuicios, bajas expectativas del profesorado (efecto Pigmalión negativo) y estigmatización social.
* **Barreras Prácticas:** Metodologías expositivas memorísticas, rigidez horaria y espacios arquitectónicos inaccesibles.

### 4.3. El Diseño Universal para el Aprendizaje (DUA)
Paradigma pedagógico impulsado por el Center for Applied Special Technology (CAST), asumido explícitamente por la LOMLOE y los Decretos curriculares andaluces de 2023. Ofrece tres redes neurales de intervención didáctica:
1. **Múltiples formas de Implicación (El «Por qué» del aprendizaje):** Motivar el interés y la autorregulación.
2. **Múltiples formas de Representación (El «Qué» del aprendizaje):** Presentar la información en múltiples formatos (texto, audio, gráfico, lectura fácil).
3. **Múltiples formas de Acción y Expresión (El «Cómo» del aprendizaje):** Permitir al alumno demostrar lo que sabe mediante diversos canales (oral, escrito, artístico, digital).

---

## 5. El enfoque preventivo de los problemas escolares

La Educación Social privilegia la **prevención primaria e interactiva** frente a la intervención paliativa o punitiva tardía:
* **Detección Precoz:** Identificación en la etapa de Educación Infantil (0-6 años) de señales de alerta en el lenguaje, la motricidad o la socialización en coordinación con los Equipos de Orientación Educativa (EOE) y los Centros de Atención Infantil Temprana (CAIT - Ley 1/2023).
* **Clima de Aula Seguro:** Construcción de dinámicas grupales cooperativas que neutralizan el rechazo social y el acoso escolar.
* **Acompañamiento a la Transición Educativa:** Planes específicos de acogida en el paso de Primaria a Secundaria para amortiguar el impacto del cambio y prevenir el fracaso.

---

## 6. Programas institucionales de atención a las necesidades socioeducativas en Andalucía

1. **Compensación Educativa y Plan PROA+ / Transfórmate:**
   - Financiado con fondos europeos del Mecanismo de Recuperación y Resiliencia.
   - Focalizado en centros con alta tasa de vulnerabilidad socioeducativa para reducir el abandono escolar temprano y ofrecer refuerzo pedagógico vespertino.
2. **Aulas Temporales de Adaptación Lingüística (ATAL):**
   - Dispositivos de apoyo específico para la inmersión lingüística acelerada en castellano del alumnado de origen extranjero, garantizando su escolarización inmediata y evitando la segregación.
3. **Aulas Hospitalarias y Atención Educativa Domiciliaria:**
   - Garantía de continuidad académica y acompañamiento emocional al alumnado con enfermedades de larga duración hospitalizado o convaleciente en su domicilio.
4. **Planes de Convivencia e Igualdad:**
   - Protocolos específicos contra la lgtbifobia, el machismo y el racismo, garantizando que la diversidad de identidad y de origen sea protegida.

---

## 7. Ámbitos de actuación e intervención del educador o educadora social

De acuerdo con las **Instrucciones de 17 de septiembre de 2010**, el educador social despliega una intervención integral en cuatro planos:
1. **Ámbito Alumnado:**
   - Acompañamiento socioemocional a menores en situación de vulnerabilidad o crisis vital.
   - Dinamización de grupos de tutoría entre iguales y fomento del aprendizaje dialógico.
2. **Ámbito Familiar:**
   - Mediación y puente comunicativo con familias de etnia gitana, migrantes o en riesgo social que desconfían de la institución escolar.
   - Asesoramiento en la tramitación de becas escolares, ayudas de comedor, libros de texto y transporte.
3. **Ámbito Centro / Claustro:**
   - Asesoramiento colaborativo al Equipo Docente y al Departamento de Orientación sobre factores sociofamiliares y barreras comunitarias.
   - Participación en la elaboración y seguimiento de los Planes de Atención a la Diversidad (PAD).
4. **Ámbito Comunitario / Red Territorial:**
   - Coordinación fluida con los Servicios Sociales Comunitarios (PRISO, Ley 9/2016), centros de salud, entidades gitanas (Secretariado Gitano) y asociaciones barriales.

---

## 8. Conclusión

Una escuela de calidad no es aquella que selecciona o premia únicamente a los talentos privilegiados de partida, sino **aquella que acoge a cada ser humano en su singularidad irrepetible, compensa las desventajas de origen y maximiza el desarrollo pleno de todas sus potencialidades**.

El **Educador y la Educadora Social** humaniza y dinamiza la escuela inclusiva en Andalucía: tiende puentes entre las aulas y los barrios vulnerables, combate el estigma del fracaso escolar y convierte la diversidad en el motor ético de una sociedad más libre, solidaria y justa.

---

## 9. Anexo: Mapa conceptual y tabla sinóptica del Tema 18

| Eje Temático | Normativa / Doctrinas Clave | Conceptos e Implicación Práctica |
| :--- | :--- | :--- |
| **Concepto de Inclusión** | Gerardo Echeita • Ignacio Calderón | Derecho inalienable de justicia; transformación integral del centro frente al modelo asimilacionista. |
| **Barreras al Aprendizaje** | Tony Booth y Mel Ainscow (*Index*) | Sustitución del déficit individual por barreras políticas, culturales y prácticas escolares. |
| **Diseño Universal (DUA)** | CAST • LOMLOE • Decretos 2023 | Múltiples formas de implicación («por qué»), representación («qué») y acción/expresión («cómo»). |
| **Categorías de NEAE** | LOMLOE (art. 71) • LEA • Ord. 2021 | NEE (discapacidad/trastornos), Altas Capacidades, Incorporación tardía, Vulnerabilidad socioeducativa. |
| **Programas en Andalucía** | Plan PROA+ / Transfórmate • ATAL | Compensación de desigualdades, inmersión lingüística y acompañamiento escolar en zonas vulnerables. |
| **Atención Hospitalaria** | Ley de Infancia de Andalucía (2021) | Aulas hospitalarias y atención domiciliaria para garantizar el derecho a la educación en convalecencia. |
| **Rol del Educador/a Social** | Instrucciones de 17 de septiembre de 2010 | Puente sociofamiliar, mediación intercultural, asesoramiento en PAD y trabajo en red comunitaria. |
"""

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 18 - Aspectos Socioeducativos de la Diversidad. Características del Alumnado. Escuela Inclusiva. DUA. Programas en Andalucía</title>
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
    <h1>TEMA 18</h1>
    <h2>Aspectos e implicaciones socioeducativas de la diversidad. Condicionantes y características personales del alumnado relevantes para el desarrollo del aprendizaje. Atención a la diversidad desde la Educación Social. Ámbitos de intervención. Enfoque preventivo. Escuela inclusiva. Programas institucionales en Andalucía</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> LOMLOE 3/2020; Ley 17/2007 (LEA, Título III); Decretos 100/101/102 de 2023 de Andalucía; Orden 15 de enero de 2021; Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Tony Booth y Mel Ainscow (Index for Inclusion), Gerardo Echeita, Ignacio Calderón, CAST (DUA)</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 18</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y fundamentación socioeducativa de la diversidad humana</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">Aspectos e implicaciones de la diversidad: Del déficit a la inclusión</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">Condicionantes y características personales del alumnado (NEAE)</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">La escuela inclusiva: Barreras al aprendizaje y Diseño Universal (DUA)</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">El enfoque preventivo de las dificultades escolares</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">Programas institucionales de atención socioeducativa en Andalucía</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">Ámbitos de actuación e intervención del educador o educadora social</span></li>
      <li class="toc-item"><span class="toc-num">08</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 18</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y fundamentación socioeducativa de la diversidad humana</h2>
  <p>
    La diversidad no constituye una disfunción del aula, un estorbo curricular ni una etiqueta marginal para unos pocos estudiantes: <strong>la diversidad es la condición constitutiva y enriquecedora de toda comunidad humana</strong>. Cada alumno accede al proceso de enseñanza-aprendizaje desde una biografía única, caracterizada por sus ritmos madurativos, talentos individuales, patrimonio lingüístico-cultural y las condiciones materiales de su entorno sociofamiliar.
  </p>
  <p>
    La <strong>Educación Social</strong> promueve una ruptura epistemológica con la vieja escuela selectiva: la diversidad no debe ser «homogeneizada», sino celebrada y potenciada mediante una pedagogía de la equidad. Exige a la institución educativa transformarse para dar respuesta a la singularidad de cada estudiante, eliminando cualquier vestigio de exclusión o segregación.
  </p>
  <p>
    En Andalucía, caracterizada por su pluralidad cultural y por intensas brechas socioeconómicas entre comarcas, el Educador/a Social actúa como garantía de inclusión efectiva, tendiendo puentes entre la institución escolar, los hogares vulnerables y las redes comunitarias.
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. Aspectos e implicaciones de la diversidad: Del déficit a la inclusión</h2>
  <p>
    El paradigma socioeducativo contemporáneo refuta el <strong>modelo médico-rehabilitador del déficit</strong>, que sitúa el problema dentro del estudiante y lo somete a terapias aisladas. En su lugar, abraza el <strong>modelo social de la inclusión</strong>:
  </p>
  <ul>
    <li>Las dificultades de aprendizaje no son defectos biológicos fijos, sino el resultado del choque entre las características del sujeto y las <strong>barreras físicas, actitudinales y curriculares</strong> impuestas por el centro educativo y la sociedad.</li>
    <li>La equidad escolar exige no dar a todos exactamente lo mismo, sino ofrecer a cada estudiante los apoyos y recursos personalizados que precisa para alcanzar el máximo desarrollo de sus capacidades.</li>
  </ul>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. Condicionantes y características personales del alumnado (NEAE)</h2>
  <p>
    La normativa educativa (LOMLOE, LEA y Orden de 15 de enero de 2021) agrupa a los estudiantes que requieren respuestas diferenciadas bajo el concepto de <strong>Alumnado con Necesidad Específica de Apoyo Educativo (NEAE)</strong>:
  </p>

  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">NECESIDADES EDUCATIVAS ESPECIALES (NEE)</h4>
      <p>
        • Discapacidad física, intelectual, visual o auditiva.<br>
        • Trastorno del Espectro Autista (TEA).<br>
        • Trastornos graves de conducta y de salud mental.<br>
        • Requieren adaptaciones curriculares significativas y personal especializado (PT, AL, PTIS).
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">VULNERABILIDAD SOCIOFAMILIAR Y OTRAS NEAE</h4>
      <p>
        • <em>Desventaja sociocultural:</em> Familias en exclusión social, pobreza severa o minorías no escolarizadas.<br>
        • <em>Incorporación tardía:</em> Alumnado de origen extranjero con desconocimiento del idioma.<br>
        • <em>Altas capacidades intelectuales:</em> Necesidad de enriquecimiento curricular y acompañamiento emocional.
      </p>
    </div>
  </div>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. La escuela inclusiva: Barreras al aprendizaje y Diseño Universal (DUA)</h2>

  <h3 class="sub-title">4.1. El Enfoque de Barreras (Tony Booth y Mel Ainscow)</h3>
  <p>
    El <em>Index for Inclusion</em> plantea que los centros educativos deben realizar una autoevaluación institucional continua para derribar tres categorías de barreras:
  </p>
  <ul>
    <li><strong>Barreras Políticas:</strong> Normas rígidas o sistemas de admisión que favorecen la guetización.</li>
    <li><strong>Barreras Culturales:</strong> Prejuicios clasistas, xenófobos o capacitistas del entorno y bajas expectativas del claustro.</li>
    <li><strong>Barreras Prácticas:</strong> Metodologías unidireccionales de clase magistral y libros de texto uniformes.</li>
  </ul>

  <h3 class="sub-title">4.2. El Diseño Universal para el Aprendizaje (DUA)</h3>
  <div class="callout">
    <div class="callout-title">Principios del DUA en los Decretos Curriculares Andaluces de 2023</div>
    <p>
      1. <strong>Múltiples formas de Implicación (El «Por qué»):</strong> Despertar el interés, proponer retos adaptados y fomentar la autorregulación.<br>
      2. <strong>Múltiples formas de Representación (El «Qué»):</strong> Presentar los contenidos en soportes visuales, auditivos, manipulativos y texto en lectura fácil.<br>
      3. <strong>Múltiples formas de Acción y Expresión (El «Cómo»):</strong> Diversificar los modos de evaluar (vídeos, proyectos prácticos, exposiciones orales).
    </p>
  </div>

  <!-- SECCIÓN 5 -->
  <div class="page-break"></div>
  <h2 class="section-title">5. El enfoque preventivo de las dificultades escolares</h2>
  <p>
    Frente a la intervención de bomberos que acude solo cuando estalla la expulsión disciplinar, la Educación Social articula la <strong>prevención primaria y proactiva</strong>:
  </p>
  <ul>
    <li><strong>Detección Precoz en Educación Infantil (0-6 años):</strong> Coordinación con los Equipos de Orientación Educativa (EOE) y los Centros de Atención Infantil Temprana (CAIT - Ley 1/2023 de Andalucía) ante retrasos madurativos o privación sensorial.</li>
    <li><strong>Tutoría entre Iguales y Aprendizaje Cooperativo:</strong> Redes de soporte mutuo que impiden el aislamiento social de alumnos diversos.</li>
    <li><strong>Acompañamiento en Transiciones Educativas:</strong> Planes de enlace entre 6.º de Primaria y 1.º de ESO para amortiguar el impacto del cambio institucional.</li>
  </ul>

  <!-- SECCIÓN 6 -->
  <h2 class="section-title">6. Programas institucionales de atención socioeducativa en Andalucía</h2>
  <ul>
    <li><strong>Programa PROA+ / Transfórmate:</strong> Financiado con fondos de la Unión Europea para centros con alto índice de vulnerabilidad socioeducativa; refuerza el éxito escolar y la convivencia.</li>
    <li><strong>Aulas Temporales de Adaptación Lingüística (ATAL):</strong> Docentes de apoyo itinerantes que imparten inmersión acelerada en español a estudiantes extranjeros, compatibilizándola con su permanencia en el aula ordinaria.</li>
    <li><strong>Aulas Hospitalarias y Atención Domiciliaria:</strong> Apoyo escolar y afectivo directo para menores con tratamientos médicos prolongados o convalecencia doméstica.</li>
    <li><strong>Planes de Compensación Educativa:</strong> Dotación suplementaria de recursos materiales y humanos a centros situados en zonas desfavorecidas.</li>
  </ul>

  <!-- SECCIÓN 7 -->
  <div class="page-break"></div>
  <h2 class="section-title">7. Ámbitos de actuación e intervención del educador o educadora social</h2>
  <p>
    En virtud de las <strong>Instrucciones de 17 de septiembre de 2010</strong>, el Educador Social ejerce funciones especializadas:
  </p>
  <ul>
    <li><strong>Enlace Sociofamiliar con Familias Vulnerables:</strong> Mediación con familias gitanas, migrantes o en riesgo social para garantizar su asistencia a tutorías y su implicación activa en el centro.</li>
    <li><strong>Gestión de Becas y Equidad Material:</strong> Ayuda a progenitores analfabetos digitales en la tramitación de becas escolares, ayudas de comedor, libros de texto y transporte gratuito.</li>
    <li><strong>Colaboración en el Plan de Atención a la Diversidad (PAD):</strong> Asesoramiento al claustro y al Departamento de Orientación sobre las variables contextuales y comunitarias del alumnado.</li>
    <li><strong>Trabajo en Red Territorial:</strong> Coordinación operativa con los Servicios Sociales Comunitarios (PRISO), equipos de infancia, Salud Mental (USMIJ) y entidades gitanas del barrio.</li>
  </ul>

  <!-- SECCIÓN 8 -->
  <h2 class="section-title">8. Conclusión</h2>
  <p>
    La excelencia de un sistema educativo público no se mide por las notas de los alumnos más brillantes y acomodados, sino por su capacidad para <strong>acoger, cuidar y promover a quienes se encuentran en situaciones de mayor desventaja de partida</strong>.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> es el guardián de la equidad en la escuela andaluza: derriba las barreras de la indiferencia y el clasismo, construye lazos de confianza entre el hogar y el pupitre y hace realidad el sueño de una escuela auténticamente inclusiva donde todas las infancias tienen derecho a brillar.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 18</h2>
  <p>Resumen estructurado de paradigmas de diversidad, marco normativo y programas inclusivos:</p>

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
        <td><strong>Modelo Inclusivo</strong></td>
        <td>Gerardo Echeita<br>Ignacio Calderón Almendros</td>
        <td>La diversidad como derecho humano universal. Transformación institucional frente a la segregación.</td>
      </tr>
      <tr>
        <td><strong>Barreras al Aprendizaje</strong></td>
        <td>Tony Booth y Mel Ainscow (<em>Index</em>)</td>
        <td>Barreras políticas, culturales (estigmas) y prácticas didácticas que la escuela debe derribar.</td>
      </tr>
      <tr>
        <td><strong>Diseño Universal (DUA)</strong></td>
        <td>CAST<br>Decretos 100/101/102 (2023)</td>
        <td>Múltiples formas de implicación («por qué»), representación («qué») y acción/expresión («cómo»).</td>
      </tr>
      <tr>
        <td><strong>Categorías NEAE</strong></td>
        <td>LOMLOE (art. 71)<br>Orden 15 de enero de 2021</td>
        <td>NEE (discapacidades y trastornos graves), Altas Capacidades, Incorporación tardía y Desventaja sociofamiliar.</td>
      </tr>
      <tr>
        <td><strong>Programas en Andalucía</strong></td>
        <td>PROA+ / Transfórmate<br>Aulas ATAL e Inmersión</td>
        <td>Compensación educativa en zonas vulnerables, acogida lingüística y apoyo contra el abandono escolar.</td>
      </tr>
      <tr>
        <td><strong>Atención Convaleciente</strong></td>
        <td>Ley 4/2021 de Infancia de Andalucía</td>
        <td>Aulas hospitalarias y atención domiciliaria para salvaguardar el derecho a la educación en enfermedad.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Mediación sociofamiliar con colectivos vulnerables, tramitación de becas, PAD y red comunitaria con SSCC.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

md_path = "andalucia/Tema_18_Aspectos_Socioeducativos_Diversidad_Escuela_Inclusiva.md"
html_path = "andalucia/Tema_18_Aspectos_Socioeducativos_Diversidad_Escuela_Inclusiva.html"
pdf_path = "andalucia/Tema_18_Aspectos_Socioeducativos_Diversidad_Escuela_Inclusiva.pdf"

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")
compile_pdf(html_path, pdf_path)
