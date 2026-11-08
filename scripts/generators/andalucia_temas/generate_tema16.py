import os
import sys
from build_theme import compile_pdf

# --- TEMA 16: DATOS Y TEXTO ---

md_content = """# TEMA 16: Educación para el Ocio y el Tiempo Libre. Modelos y Estrategias de Intervención desde el Campo Socioeducativo. Recursos Culturales y Sociales para el Ocio y el Tiempo Libre. Agentes para la Intervención Social en el Ámbito del Tiempo Libre. Actuación e Intervención del Educador o Educadora Social en el Desarrollo de la Educación para el Ocio y el Tiempo Libre

---

## FICHA TÉCNICA DEL TEMA
* **Cuerpo:** Cuerpo Técnico Facultativo de la Junta de Andalucía
* **Especialidad:** Educación Social (A2.2018)
* **Carácter:** Materias Específicas del Programa Oficial
* **Marco Legal y Documental:**
  - Carta de los Derechos del Niño (ONU, 1989, art. 31: derecho al descanso, esparcimiento y juego).
  - Ley Orgánica 2/2006 (LOE), modificada por la LOMLOE 3/2020.
  - Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA), arts. 12 y 13 (Plan de Apertura y actividades extraescolares).
  - Ley 4/2021, de 27 de julio, de Infancia y Adolescencia de Andalucía.
  - Decreto 327/2010 y Decreto 328/2010 (Reglamentos Orgánicos de IES y Colegios).
  - Instrucciones de 17 de septiembre de 2010 de la Dirección General de Participación e Innovación Educativa.
* **Autores y Doctrinas de Referencia:** Joffre Dumazedier (Las 3 "D" del ocio: Délassement, Divertissement, Développement), Manuel Cuenca Cabeza (Pedagogía del ocio, ocio autotélico vs. alienante), Toni Puig (Animación sociocultural y juventud), Johan Huizinga (*Homo Ludens*).

---

## ÍNDICE DE CONTENIDOS
1. Introducción y conceptualización del ocio y tiempo libre en la sociedad contemporánea.
2. Evolución y modelos teóricos de la educación del ocio: Del tiempo residual al ocio como derecho humano.
3. Estrategias de intervención socioeducativa en el ocio y el tiempo libre.
4. Mapa de recursos culturales, sociales y comunitarios para el ocio.
5. Agentes de la intervención social en el ámbito del tiempo libre.
6. Actuación e intervención del educador o educadora social:
   - 6.1. Dinamización de patios escolares inclusivos y recreos activos.
   - 6.2. Conexión del centro educativo con la comunidad (Plan de Apertura, PROA Andalucía).
   - 6.3. Alternativas de ocio saludable juvenil frente al consumo de sustancias y pantallas.
7. Conclusión.
8. Anexo: Mapa conceptual y tabla sinóptica del Tema 16.

---

## 1. Introducción y conceptualización del ocio y tiempo libre en la sociedad contemporánea

El ocio y el tiempo libre han dejado de ser concebidos como un mero paréntesis pasivo tras la jornada laboral o escolar para situarse en el núcleo mismo del **desarrollo integral, la salud emocional y la socialización ciudadana**. En la sociedad hiperconectada y de consumo del siglo XXI, el tiempo liberado de obligaciones se encuentra frecuentemente colonizado por la industria del entretenimiento pasivo, la tiranía de las redes sociales y el aislamiento digital, o bien mercantilizado bajo lógicas excluyentes para aquellos sectores infantojuveniles en situación de vulnerabilidad económica.

Para la **Educación Social**, el ocio constituye un **derecho humano fundamental e inalienable** (reconocido en el artículo 31 de la Convención sobre los Derechos del Niño y en el artículo 24 de la Declaración Universal de Derechos Humanos). La intervención socioeducativa no busca simplemente "entretener" o "mantener ocupados" a los menores para evitar conductas conflictivas, sino proporcionar experiencias significativas de descubrimiento, creatividad, cooperación y autogestión vital.

En el marco de la escuela pública andaluza, el Educador y la Educadora Social actúa como puente indispensable entre la institución escolar y el tejido comunitario, transformando los tiempos no lectivos (recreos, tardes, fines de semana) en verdaderas oportunidades de equidad, convivencia pacífica e inclusión social.

---

## 2. Evolución y modelos teóricos de la educación del ocio

### 2.1. Distinción conceptual: Tiempo libre vs. Ocio
* **Tiempo Libre:** Dimensión cronológica y cuantitativa. Es el segmento temporal que resta tras haber cumplido las obligaciones laborales, escolares, fisiológicas y familiares primarias.
* **Ocio (*Leisure* / *Otium*):** Dimensión cualitativa y actitudinal. Implica una vivencia subjetiva caracterizada por la **libertad de elección, la gratuidad (carácter autotélico), la satisfacción personal y el desarrollo creador**.

### 2.2. Las tres funciones clásicas del ocio (Joffre Dumazedier)
El sociólogo francés Joffre Dumazedier definió el ocio a través de las conocidas **3 "D"**:
1. **Descanso (*Délassement*):** Liberación de la fatiga psicofísica acumulada y recuperación del equilibrio biológico.
2. **Diversión (*Divertissement*):** Ruptura con la monotonía rutinaria, desahogo afectivo, juego y entretenimiento gratificante.
3. **Desarrollo personal (*Développement*):** Cultivo voluntario de destrezas intelectuales, corporales, artísticas y cívicas que expanden la personalidad.

### 2.3. Modelos pedagógicos del ocio (Manuel Cuenca Cabeza)
* **Modelo Moralista / Compensatorio:** Entiende el ocio como un instrumento para corregir la desviación social y alejar a la juventud de "vicios" (drogas, delincuencia). Tiende al dirigismo paternalista.
* **Modelo Consumista / Comercial:** Reduce el ocio a un producto de mercado. Promueve el consumo pasivo de pantallas, compras y espectáculos masificados, generando frustración en sectores desfavorecidos.
* **Modelo Humanista / Emancipador:** Defendido por la Pedagogía Social moderna. Concibe el **ocio autotélico** como una experiencia valiosa en sí misma, orientada a la autorrealización, la participación democrática, la solidaridad y la transformación comunitaria.

---

## 3. Estrategias de intervención socioeducativa en el ocio y el tiempo libre

La intervención socioeducativa despliega cuatro estrategias metodológicas vertebrales:
1. **Animación Sociocultural (ASC):** Metodología comunitaria que estimula la iniciativa de los propios colectivos para que se conviertan en agentes activos de su cultura y tiempo de recreación (Toni Puig, Quintana Cabanas).
2. **Pedagogía de la Creación y el Juego (*Homo Ludens*):** Rescate del juego libre y cooperativo como laboratorio de ensayo social, resolución de conflictos y regulación de emociones.
3. **Educación Ambiental y Ocio en la Naturaleza:** Campamentos, senderismo, rutas medioambientales que contrarrestan el "déficit de naturaleza" urbano y enseñan sostenibilidad.
4. **Ocio Nocturno Alternativo y Reducción de Riesgos:** Proyectos municipales y comunitarios dirigidos a adolescentes y jóvenes que abren espacios deportivos, culturales y artísticos en fines de semana nocturnos como alternativa al botellón.

---

## 4. Mapa de recursos culturales, sociales y comunitarios para el ocio

La intervención del educador social se nutre del ecosistema territorial:

| Tipología de Recurso | Ejemplos e Instituciones | Utilidad Socioeducativa |
| :--- | :--- | :--- |
| **Equipamientos de Proximidad** | Centros cívicos, Casas de la Juventud, Ludotecas municipales | Espacios seguros de socialización, talleres creativos y encuentro intergeneracional. |
| **Infraestructuras Culturales** | Bibliotecas públicas, Museos, Teatros comunitarios | Democratización de la cultura, fomento lector y alfabetización artística. |
| **Instalaciones Deportivas** | Pistas polideportivas de barrio, skateparks, piscinas públicas | Fomento del ocio activo, hábitos saludables y superación de la segregación juvenil. |
| **Espacios Naturales Protegidos** | Parques metropolitanos, Red de Espacios Naturales de Andalucía (RENPA) | Convivencia comunitaria al aire libre, voluntariado medioambiental y educación ecológica. |

---

## 5. Agentes de la intervención social en el ámbito del tiempo libre

1. **Monitores/as y Directores/as de Tiempo Libre:** Perfiles técnicos de la educación no formal formados en escuelas de tiempo libre oficiales homologadas por el Instituto Andaluz de la Juventud (IAJ).
2. **Asociacionismo Juvenil e Infantil:** Grupos Scouts, Movimiento Junior, Cruz Roja Juventud, asociaciones estudiantiles y clubes deportivos de base. Fomentan el aprendizaje democrático y la autogestión.
3. **Administraciones Públicas:**
   - **Consejería de Desarrollo Educativo y FP:** Programas de refuerzo y apertura de centros (*Plan de Apertura*, PROA Andalucía).
   - **Instituto Andaluz de la Juventud (IAJ):** Albergues juveniles (Inturjoven), campos de voluntariado, formación juvenil.
   - **Ayuntamientos (Áreas de Juventud, Deportes y Servicios Sociales Comunitarios):** Oferta programática municipal en fines de semana y vacaciones escolares.

---

## 6. Actuación e intervención del educador o educadora social

De acuerdo con las **Instrucciones de 17 de septiembre de 2010**, el educador/a social en centros educativos andaluces despliega líneas de acción preferentes en el tiempo libre:

### 6.1. Dinamización de patios escolares inclusivos y recreos activos
* Superación del monopolio del balón de fútbol y la segregación por género de las pistas deportivas centrales.
* Creación de espacios diversificados: zonas de juegos de mesa gigantes, rincones de lectura y conversación (*chill-out*), espacios artísticos y torneos deportivos mixtos y cooperativos.
* Prevención directa del acoso escolar y aislamiento de alumnado vulnerable durante el recreo.

### 6.2. Conexión del centro escolar con la comunidad (Plan de Apertura y PROA)
* **Plan de Apertura de Centros (art. 12 y 13 LEA):** Optimización de las instalaciones escolares fuera del horario lectivo (aula matinal, comedor escolar y actividades extraescolares culturales, deportivas e idiomáticas).
* **Programa de Refuerzo, Orientación y Apoyo (PROA Andalucía):** Vinculación del apoyo escolar por las tardes con talleres socioeducativos lúdicos que refuercen la autoestima y la motivación intrínseca.
* Conexión fluida con los recursos del barrio: derivación de menores y familias a ludotecas, escuelas de música y clubes deportivos para garantizar becas de gratuidad a familias en riesgo de exclusión.

### 6.3. Alternativas de ocio saludable juvenil frente a adicciones y pantallas
* Coordinación con la Asesoría *Forma Joven* y el área municipal de juventud para implementar programas de ocio nocturno preventivo.
* Talleres de "desconexión digital consciente" y uso crítico de videojuegos (prevención del juego patológico y apuestas online).
* Capacitación y empoderamiento de líderes juveniles (alumnado ayudante y mediador) para organizar sus propias propuestas culturales.

---

## 7. Conclusión

El tiempo libre no es un vacío que deba ser llenado compulsivamente con consumo, sino un **territorio privilegiado de humanización y libertad**. Una sociedad que niega el acceso a un ocio enriquecedor y digno a su infancia y juventud vulnera un derecho básico y perpetúa la brecha de desigualdad.

La intervención del **Educador y la Educadora Social** rescata el valor pedagógico del juego, la cultura comunitaria y el encuentro humano. Al abrir la escuela al barrio y transformar el tiempo de ocio en un laboratorio de ciudadanía crítica, el educador social siembra las bases de una comunidad más justa, saludable y cohesionada.

---

## 8. Anexo: Mapa conceptual y tabla sinóptica del Tema 16

| Eje Temático | Normativa / Doctrinas Clave | Conceptos e Implicación Práctica |
| :--- | :--- | :--- |
| **Concepto de Ocio** | CDN (art. 31) • DUDH (art. 24) | Derecho humano inalienable. Tiempo autotélico, libremente elegido, placentero y humanizador. |
| **Funciones del Ocio** | Joffre Dumazedier (Las 3 "D") | Descanso (*Délassement*), Diversión (*Divertissement*) y Desarrollo personal (*Développement*). |
| **Modelos Pedagógicos** | Manuel Cuenca Cabeza | Ocio humanista/emancipador frente a modelos moralistas punitivos y modelos comerciales pasivos. |
| **Estrategias Metodológicas**| Toni Puig • Quintana Cabanas | Animación sociocultural, pedagogía del juego (*Homo Ludens*), educación ambiental y ocio nocturno alternativo. |
| **Ecosistema de Recursos** | IAJ • Red Inturjoven • Ayuntamientos | Casas de juventud, ludotecas, bibliotecas de barrio, pistas polideportivas y red de espacios naturales. |
| **Marco Andaluz** | LEA (arts. 12 y 13) • D. 327/328 (2010) | Plan de Apertura de centros (extraescolares, aula matinal), PROA Andalucía y apertura comunitaria. |
| **Rol del Educador/a Social** | Instrucciones de 17 de septiembre de 2010 | Patios inclusivos, recreos activos, dinamización del asociacionismo juvenil y alternativas de ocio sin pantallas ni tóxicos. |
"""

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 16 - Educación para el Ocio y el Tiempo Libre. Modelos y Estrategias. Recursos. Agentes y Rol del Educador Social</title>
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
    <h1>TEMA 16</h1>
    <h2>Educación para el ocio y el tiempo libre. Modelos y estrategias de intervención desde el campo socioeducativo. Recursos culturales y sociales para el ocio y el tiempo libre. Agentes para la intervención social en el ámbito del tiempo libre. Actuación e intervención del educador o educadora social</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> Convención Derechos del Niño (art. 31); Ley 17/2007 (LEA, arts. 12-13); Ley 4/2021 de Infancia de Andalucía; Decretos 327/328 (2010); Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Joffre Dumazedier (Las 3 "D"), Manuel Cuenca Cabeza, Toni Puig, Johan Huizinga</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 16</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y conceptualización del ocio y tiempo libre en la sociedad actual</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">Evolución y modelos teóricos de la educación del ocio</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">Estrategias de intervención socioeducativa en el tiempo libre</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">Mapa de recursos culturales, sociales y comunitarios</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">Agentes para la intervención social en el ámbito del ocio</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">Actuación e intervención del educador o educadora social</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 16</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y conceptualización del ocio y tiempo libre en la sociedad actual</h2>
  <p>
    El ocio y el tiempo libre han dejado de ser concebidos como un mero paréntesis pasivo tras la jornada laboral o escolar para situarse en el núcleo mismo del <strong>desarrollo integral, la salud emocional y la socialización ciudadana</strong>. En la sociedad contemporánea, el tiempo liberado se encuentra a menudo colonizado por el consumo comercial de pantallas, el aislamiento digital y las ofertas mercantilizadas que excluyen a la infancia y juventud en situación de vulnerabilidad social.
  </p>
  <p>
    Para la <strong>Educación Social</strong>, el ocio es un <strong>derecho humano fundamental e inalienable</strong>, consagrado en el artículo 31 de la Convención sobre los Derechos del Niño de 1989. La intervención socioeducativa no pretende «mantener entretenidos» a los menores con un enfoque moralista o de control social, sino abrir espacios de aprendizaje no formal donde vivenciar la creatividad, el protagonismo juvenil, la cooperación y el placer de vivir.
  </p>
  <p>
    En la escuela pública andaluza, el Educador/a Social actúa como articulador entre el centro educativo y los recursos del barrio, transformando los tiempos no lectivos (recreos, tardes, periodos vacacionales) en oportunidades de equidad, compensación de desigualdades e inclusión.
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. Evolución y modelos teóricos de la educación del ocio</h2>

  <h3 class="sub-title">2.1. Distinción conceptual: Tiempo libre vs. Ocio</h3>
  <ul>
    <li><strong>Tiempo Libre:</strong> Concepto cronológico y cuantitativo. Es el tiempo residual que queda tras cumplir los deberes escolares, laborales y las necesidades biopsicosociales primarias.</li>
    <li><strong>Ocio (Otium / Leisure):</strong> Dimensión cualitativa y vivencial. Experiencia subjetiva elegida con libertad, caracterizada por la gratuidad, el disfrute personal y el desarrollo creador (carácter autotélico).</li>
  </ul>

  <h3 class="sub-title">2.2. Las tres funciones del ocio según Joffre Dumazedier (Las 3 "D")</h3>
  <div class="callout">
    <div class="callout-title">Funciones Esenciales del Ocio Humanizador</div>
    <p>
      1. <strong>Descanso (Délassement):</strong> Reparación física y psíquica frente a las tensiones y fatigas cotidianas.<br>
      2. <strong>Diversión (Divertissement):</strong> Ruptura con la monotonía, disfrute lúdico y desahogo emocional.<br>
      3. <strong>Desarrollo personal (Développement):</strong> Enriquecimiento personal voluntario mediante la cultura, el arte, la actividad física y el compromiso asociativo.
    </p>
  </div>

  <h3 class="sub-title">2.3. Modelos pedagógicos del ocio (Manuel Cuenca Cabeza)</h3>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">MODELO HUMANISTA / EMANCIPADOR</h4>
      <p>
        El ocio como experiencia valiosa en sí misma (ocio autotélico). Favorece la autorrealización, la autonomía crítica, la solidaridad comunitaria y la ciudadanía participativa.
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">MODELO CONSUMISTA Y MORALISTA</h4>
      <p>
        • <em>Consumista:</em> Ocio mercantilizado, consumo pasivo de pantallas y alienación.<br>
        • <em>Moralista:</em> Ocio instrumentalizado para el control punitivo y evitar conductas delictivas.
      </p>
    </div>
  </div>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. Estrategias de intervención socioeducativa en el tiempo libre</h2>
  <ul>
    <li><strong>Animación Sociocultural (ASC):</strong> Metodología participativa que dinamiza a los grupos para que tomen la iniciativa sobre su propia oferta cultural y comunitaria (Toni Puig).</li>
    <li><strong>Pedagogía del Juego (Homo Ludens - Johan Huizinga):</strong> El juego libre y cooperativo como ensayo de roles, autorregulación y aprendizaje de normas sociales.</li>
    <li><strong>Educación Ambiental y Tiempo Libre en la Naturaleza:</strong> Campamentos y senderismo que combaten el déficit de naturaleza y promueven la sostenibilidad y el trabajo colaborativo.</li>
    <li><strong>Programas de Ocio Nocturno Alternativo:</strong> Apertura de polideportivos e instalaciones culturales durante los fines de semana por la noche para ofrecer alternativas saludables al botellón.</li>
  </ul>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. Mapa de recursos culturales, sociales y comunitarios</h2>
  <p>
    La intervención en Andalucía articula una extensa red de equipamientos:
  </p>
  <ul>
    <li><strong>Equipamientos Locales:</strong> Casas de la Juventud, ludotecas municipales, centros cívicos y centros de barrio.</li>
    <li><strong>Recursos Culturales:</strong> Bibliotecas públicas, museos, teatros y escuelas municipales de música y danza.</li>
    <li><strong>Infraestructuras Deportivas:</strong> Pistas de barrio, polideportivos, skateparks y piscinas públicas, esenciales para la prevención del sedentarismo.</li>
    <li><strong>Medio Natural y Albergues:</strong> Red de Espacios Naturales de Andalucía (RENPA) y la red de albergues del Instituto Andaluz de la Juventud (Inturjoven).</li>
  </ul>

  <!-- SECCIÓN 5 -->
  <h2 class="section-title">5. Agentes para la intervención social en el ámbito del tiempo libre</h2>
  <ul>
    <li><strong>Monitores/as y Directores/as de Tiempo Libre:</strong> Educadores no formales formados en Escuelas oficiales homologadas por el Instituto Andaluz de la Juventud (IAJ).</li>
    <li><strong>Asociacionismo Juvenil e Infantil:</strong> Grupos Scouts, Cruz Roja Juventud, asociaciones estudiantiles y clubes deportivos de base.</li>
    <li><strong>Administraciones Públicas:</strong> Coordinación transversal entre la Consejería de Desarrollo Educativo y FP, el IAJ y las Concejalías municipales de Juventud, Deportes y Servicios Sociales Comunitarios.</li>
  </ul>

  <!-- SECCIÓN 6 -->
  <div class="page-break"></div>
  <h2 class="section-title">6. Actuación e intervención del educador o educadora social</h2>
  <p>
    En virtud de las <strong>Instrucciones de 17 de septiembre de 2010</strong>, el Educador/a Social asume un rol vertebrador en la comunidad educativa:
  </p>

  <h3 class="sub-title">6.1. Dinamización de patios inclusivos y recreos activos</h3>
  <p>
    Transformación de los patios escolares para evitar el monopolio del fútbol y la exclusión de alumnado vulnerable: habilitación de zonas de descanso, juegos de mesa, espacios artísticos y ligas deportivas mixtas y cooperativas.
  </p>

  <h3 class="sub-title">6.2. Conexión del centro escolar con la comunidad (Plan de Apertura y PROA)</h3>
  <ul>
    <li><strong>Plan de Apertura de Centros (arts. 12 y 13 LEA):</strong> Optimización de aula matinal, comedor y actividades extraescolares culturales, deportivas e idiomáticas.</li>
    <li><strong>Programa PROA Andalucía:</strong> Integración de acompañamiento escolar con talleres socioeducativos lúdicos por las tardes.</li>
    <li><strong>Becas y Derivación Comunitaria:</strong> Conexión con Servicios Sociales para asegurar el acceso gratuito a actividades extraescolares a menores en riesgo de exclusión.</li>
  </ul>

  <h3 class="sub-title">6.3. Alternativas de ocio saludable juvenil frente a adicciones y pantallas</h3>
  <p>
    En coordinación con la Asesoría <em>Forma Joven</em>, el educador dinamiza talleres de desconexión digital, ocio activo de fin de semana y alternativas al juego online con dinero.
  </p>

  <!-- SECCIÓN 7 -->
  <h2 class="section-title">7. Conclusión</h2>
  <p>
    El tiempo libre no es un vacío que deba llenarse con consumo o dependencia tecnológica, sino un <strong>espacio privilegiado de dignidad, humanización y ciudadanía</strong>.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> devuelve al ocio su potencia pedagógica y transformadora, abriendo la escuela pública al barrio y garantizando que ningún menor quede privado del derecho universal a jugar, crear y disfrutar en comunidad.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 16</h2>
  <p>Resumen estructurado de modelos teóricos, agentes, recursos y praxis socioeducativa en el ocio:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Eje Temático</th>
        <th style="width: 38%;">Normativa y Autores Clave</th>
        <th style="width: 37%;">Conceptos e Implicación Práctica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Concepto de Ocio</strong></td>
        <td>Convención Derechos Niño (art. 31)<br>DUDH (art. 24)</td>
        <td>Derecho humano fundamental. Experiencia autotélica, voluntaria, placentera y de autorrealización.</td>
      </tr>
      <tr>
        <td><strong>Funciones del Ocio</strong></td>
        <td>Joffre Dumazedier (Las 3 "D")</td>
        <td>Descanso (liberación psicofísica), Diversión (desahogo lúdico) y Desarrollo personal (creatividad y cultura).</td>
      </tr>
      <tr>
        <td><strong>Modelos Pedagógicos</strong></td>
        <td>Manuel Cuenca Cabeza</td>
        <td>Ocio humanista y emancipador frente a los enfoques consumistas pasivos o moralistas de control penal.</td>
      </tr>
      <tr>
        <td><strong>Estrategias de Intervención</strong></td>
        <td>Toni Puig<br>Johan Huizinga (Homo Ludens)</td>
        <td>Animación sociocultural comunitaria, pedagogía del juego, educación ambiental y ocio nocturno alternativo.</td>
      </tr>
      <tr>
        <td><strong>Ecosistema de Recursos</strong></td>
        <td>IAJ • Red Inturjoven • Ayuntamientos</td>
        <td>Casas de la juventud, ludotecas, bibliotecas públicas, instalaciones deportivas y áreas naturales (RENPA).</td>
      </tr>
      <tr>
        <td><strong>Marco Andaluz</strong></td>
        <td>Ley 17/2007 (LEA, arts. 12-13)<br>Decretos 327 y 328 (2010)</td>
        <td>Plan de Apertura de centros docentes, actividades extraescolares y programa PROA Andalucía.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Patios inclusivos, recreos activos, dinamización asociativa y alternativas saludables frente al abuso de pantallas.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

md_path = "andalucia/Tema_16_Educacion_Ocio_Tiempo_Libre.md"
html_path = "andalucia/Tema_16_Educacion_Ocio_Tiempo_Libre.html"
pdf_path = "andalucia/Tema_16_Educacion_Ocio_Tiempo_Libre.pdf"

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")
compile_pdf(html_path, pdf_path)
