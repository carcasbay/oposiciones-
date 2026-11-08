import os
from build_theme import compile_pdf

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 15 - Educación para la Salud. Promoción del Bienestar Emocional. Hábitos Saludables. Educación Afectivo Sexual. Prevención de Adicciones</title>
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

    /* Portada */
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

    /* Estructura de títulos */
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

    /* Cajas destacadas */
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

    .callout-blue {
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
    }
    .callout-blue .callout-title {
      color: #1d4ed8;
    }

    .callout-amber {
      background: #fefce8;
      border-left: 4px solid #ca8a04;
    }
    .callout-amber .callout-title {
      color: #a16207;
    }

    /* Comparativa esquemática */
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

    /* Tablas */
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

    /* Índice con estilo formal */
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

    .badge-chip {
      display: inline-block;
      background: #ede9fe;
      color: #5b21b6;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 8.5pt;
      font-weight: 600;
      margin: 2px 2px;
    }
  </style>
</head>
<body>

  <!-- PORTADA -->
  <div class="cover">
    <div class="badge">Oposiciones Junta de Andalucía • A2.2018</div>
    <h1>TEMA 15</h1>
    <h2>Educación para la salud. La escuela como promotora de la salud y el bienestar emocional. Las conductas y los hábitos saludables. Educación afectivo sexual. Prevención de las adicciones. Actuación e intervención del educador o educadora social en el desarrollo de la educación para la salud y educación de los sentimientos</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> Carta de Ottawa (1986); Ley 16/2011 de Salud Pública de Andalucía; III Plan Andaluz sobre Drogas y Adicciones; Programa Hábitos de Vida Saludable; Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Michael Marmot, Daniel Goleman, Rafael Bisquerra, OMS / Red SHE</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 15</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y contextualización en la Educación Social</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">Educación para la salud: Concepto, modelos y marco normativo</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">La escuela como promotora de la salud y el bienestar emocional</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">Conductas y hábitos de vida saludables en el ámbito escolar</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">Educación afectivo-sexual integral</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">Prevención de las adicciones químicas y comportamentales</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">Actuación e intervención del educador o educadora social</span></li>
      <li class="toc-item"><span class="toc-num">08</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 15</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y contextualización en la Educación Social</h2>
  <p>
    La <strong>Educación para la Salud</strong> ha experimentado una profunda transformación epistemológica en las últimas décadas. Ha superado la vieja concepción biomédica, restrictiva y biologicista —centrada exclusivamente en la prevención de enfermedades y el miedo punitivo— para consolidarse como un <strong>proceso pedagógico integral, emancipador y comunitario orientado a la promoción del bienestar físico, mental y social</strong>.
  </p>
  <p>
    La escuela es el entorno privilegiado para consolidar estilos de vida saludables: es la única institución por la que transita el 100% de la población durante su periodo evolutivo más plástico. No obstante, la salud no depende únicamente de decisiones biológicas individuales; está profundamente condicionada por los <strong>determinantes sociales de la salud (Michael Marmot)</strong>: la pobreza, la precariedad habitacional, el nivel educativo de las familias y el entorno barrial inciden directamente en las tasas de obesidad infantil, salud mental precaria o adicciones juveniles.
  </p>
  <p>
    Para el <strong>Educador y la Educadora Social</strong>, este ámbito es de una vigencia incuestionable. En un momento de alarma social por el incremento de autolesiones, depresión adolescente, ludopatía online y consumo precoz de pornografía, el educador social despliega una intervención integral: dinamiza la salud emocional en las aulas, lidera la asesoría confidencial para jóvenes (<em>Forma Joven</em>), previene adicciones y teje alianzas operativas entre la escuela, las familias y el sistema sanitario público andaluz.
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. Educación para la salud: Concepto, modelos y marco normativo</h2>

  <h3 class="sub-title">2.1. El concepto holístico de salud y la Carta de Ottawa</h3>
  <p>
    La Organización Mundial de la Salud (OMS, 1948) definió la salud como <em>«un estado de completo bienestar físico, mental y social, y no solamente la ausencia de afecciones o enfermedades»</em>.
  </p>
  <div class="callout">
    <div class="callout-title">La Carta de Ottawa para la Promoción de la Salud (1986)</div>
    <p>
      Establece cinco áreas prioritarias de intervención:<br>
      1. <strong>Construcción de políticas públicas saludables.</strong><br>
      2. <strong>Creación de entornos protectores que apoyen la salud</strong> (escuelas saludables).<br>
      3. <strong>Fortalecimiento de la acción comunitaria</strong> y participación social.<br>
      4. <strong>Desarrollo de habilidades personales</strong> a través de la educación socioafectiva.<br>
      5. <strong>Reorientación de los servicios sanitarios</strong> hacia la prevención primaria.
    </p>
  </div>

  <h3 class="sub-title">2.2. La Red de Escuelas Promotoras de Salud (SHE)</h3>
  <p>
    Impulsada por la OMS, la Comisión Europea y el Consejo de Europa, promueve que los centros educativos no se limiten a «impartir charlas aisladas de salud», sino que configuren un <strong>entorno físico y relacional protector</strong>: comedores escolares saludables, patios dinámicos, clima de convivencia positivo y alianza estrecha con las familias y el entorno local.
  </p>

  <h3 class="sub-title">2.3. Determinantes sociales de la salud (Michael Marmot)</h3>
  <p>
    Existe un estricto <strong>gradiente social de la salud</strong>: a menor nivel socioeconómico familiar, mayor es la prevalencia de obesidad infantil, caries, sedentarismo, tabaquismo y patologías de salud mental. La Educación para la Salud en Andalucía debe ser, por tanto, una herramienta de <strong>equidad social y compensación de desigualdades</strong>.
  </p>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. La escuela como promotora de la salud y el bienestar emocional</h2>

  <h3 class="sub-title">3.1. Crisis de salud mental infantojuvenil</h3>
  <p>
    La Organización Mundial de la Salud alerta de que el 50% de los trastornos mentales del adulto debutan antes de los 14 años. En el ámbito educativo andaluz se constata un incremento preocupante de:
  </p>
  <ul>
    <li>Trastornos de ansiedad generalizada y ataques de pánico escolares.</li>
    <li>Episodios depresivos, apatía y anhedonia vital en adolescentes.</li>
    <li><strong>Autolesiones no suicidas (cortes, quemaduras)</strong> como mecanismo disfuncional de alivio de dolor emocional inasumible.</li>
    <li>Conducta suicida e ideación autolítica (obligación de activar el Protocolo de prevención del suicidio de la Consejería de Desarrollo Educativo).</li>
  </ul>

  <h3 class="sub-title">3.2. Estrategia de Salud Mental de Andalucía y coordinación con USMIJ</h3>
  <p>
    Articula la atención integral interdisciplinar entre los centros educativos y las <strong>Unidades de Salud Mental Infanto-Juvenil (USMIJ)</strong> del Servicio Andaluz de Salud (SAS), garantizando la continuidad pedagógica durante los tratamientos ambulatorios u hospitalarios.
  </p>

  <h3 class="sub-title">3.3. Educación de los sentimientos e inteligencia emocional</h3>
  <p>
    Siguiendo las aportaciones de <strong>Daniel Goleman y Rafael Bisquerra</strong>, la educación emocional entrena competencias básicas para la vida:
  </p>
  <ul>
    <li><strong>Conciencia emocional:</strong> Identificar y poner palabras al mundo afectivo propio.</li>
    <li><strong>Regulación emocional:</strong> Tolerar la frustración, modular la ira y gestionar el estrés sin recurrir a la violencia o el aislamiento.</li>
    <li><strong>Autonomía emocional:</strong> Construir un autoconcepto positivo no dependiente del juicio o validación ajena en redes.</li>
    <li><strong>Habilidades socioemocionales:</strong> Empatía activa, escucha profunda y resolución dialogada de desacuerdos.</li>
  </ul>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. Conductas y hábitos de vida saludables en el ámbito escolar</h2>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">NUTRICIÓN Y ACTIVIDAD FÍSICA</h4>
      <p>
        • Fomento de la dieta mediterránea y frutas en recreos.<br>
        • Supresión de bollería industrial y bebidas azucaradas en centros.<br>
        • Mínimo 60 minutos diarios de actividad física y descansos activos.<br>
        • Desplazamientos activos (caminos escolares seguros).
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">HIGIENE DEL SUEÑO Y PANTALLAS</h4>
      <p>
        • La luz azul de móviles nocturnos bloquea la melatonina.<br>
        • El insomnio digital genera somnolencia diurna y fracaso escolar.<br>
        • Pautas familiares de «cero pantallas» 2 horas antes de dormir.<br>
        • Promoción de rutinas estables de descanso.
      </p>
    </div>
  </div>

  <h3 class="sub-title">4.1. Programas institucionales en Andalucía: «Creciendo en Salud» y «Forma Joven»</h3>
  <p>
    La Consejería de Desarrollo Educativo y FP estructura la promoción de hábitos saludables a través de:
  </p>
  <ul>
    <li><strong>Creciendo en Salud (Infantil y Primaria):</strong> Educación emocional, consumo de frutas en la escuela, higiene bucodental y estilo de vida activo.</li>
    <li><strong>Forma Joven en el Ámbito Educativo (Secundaria y Formación Profesional):</strong> Asesorías de salud integral en institutos donde los jóvenes reciben orientación confidencial sobre sexualidad, adicciones y convivencia.</li>
  </ul>

  <!-- SECCIÓN 5 -->
  <div class="page-break"></div>
  <h2 class="section-title">5. Educación afectivo-sexual integral</h2>
  <p>
    La sexualidad no se reduce a la reproducción biológica ni al temor al contagio: es una <strong>dimensión humana central de placer, comunicación, afecto, identidad y ternura</strong>.
  </p>
  <div class="callout callout-blue">
    <div class="callout-title">Pilares de la Educación Afectivo-Sexual Integral</div>
    <p>
      • <strong>Consentimiento expreso y libre:</strong> «Solo sí es sí». El respeto incondicional a los límites corporales propios y ajenos.<br>
      • <strong>Prevención de ITS y embarazos no planificados:</strong> Información rigurosa y desestigmatizada sobre métodos barrera.<br>
      • <strong>Diversidad afectivo-sexual y de género:</strong> Respeto pleno a las identidades y orientaciones (Ley 4/2023 y Ley 8/2017 de Andalucía).<br>
      • <strong>Deconstrucción del porno violento online:</strong> Combate contra la normalización de la agresión y las expectativas irreales transmitidas por la industria pornográfica de internet.
    </p>
  </div>

  <!-- SECCIÓN 6 -->
  <h2 class="section-title">6. Prevención de las adicciones químicas y comportamentales</h2>
  <p>
    El <strong>III Plan Andaluz sobre Drogas y Adicciones (PADA)</strong> aborda dos vertientes complementarias:
  </p>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">ADICCIONES CON SUSTANCIA</h4>
      <p>
        • Alcohol: consumo intensivo de fin de semana (<em>binge drinking</em>).<br>
        • Cannabis: desmitificación de supuestos efectos terapéuticos e inocuidad.<br>
        • Vapeadores y tabaco: falsa percepción de seguridad de los cigarrillos electrónicos.<br>
        • Psicofármacos sin prescripción médica.
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">ADICCIONES COMPORTAMENTALES</h4>
      <p>
        • Juegos de azar y apuestas deportivas online (ludopatía juvenil).<br>
        • Videojuegos compulsivos y micropagos (<em>loot boxes</em>).<br>
        • Redes sociales: dependencia de la validación y tiranía del «like».<br>
        • Consumo compulsivo de pornografía.
      </p>
    </div>
  </div>

  <p>
    Los niveles de prevención se articulan en: <strong>Universal</strong> (alumnado general para retrasar el inicio y potenciar habilidades de asertividad), <strong>Selectiva</strong> (grupos con factores de riesgo asociados) e <strong>Indicada</strong> (intervención específica ante primeros signos de abuso).
  </p>

  <!-- SECCIÓN 7 -->
  <div class="page-break"></div>
  <h2 class="section-title">7. Actuación e intervención del educador o educadora social</h2>
  <p>
    Al amparo de las <strong>Instrucciones de 17 de septiembre de 2010</strong>, el Educador/a Social actúa como el articulador comunitario entre la escuela, la salud y la comunidad:
  </p>
  <ul>
    <li><strong>Gestión y Dinamización de la Asesoría «Forma Joven»:</strong> Creación de un espacio confidencial, cercano y desprovisto de juicios punitivos en el que el alumnado puede consultar inquietudes sobre sexualidad, relaciones amorosas tóxicas o consumos problemáticos.</li>
    <li><strong>Talleres de Educación Emocional en el POAT:</strong> Sesiones prácticas de gestión de la ansiedad ante los exámenes, prevención de autolesiones y resolución pacífica de conflictos.</li>
    <li><strong>Acompañamiento en Adicciones y Derivación:</strong> Detección temprana de juego patológico o consumo de sustancias en coordinación con los Centros de Tratamiento Ambulatorio (CTA) del SAS.</li>
    <li><strong>Escuelas de Familias sobre Higiene Digital y Afectividad:</strong> Capacitación a madres y padres para la gestión del uso de pantallas en el hogar y la detección precoz de síntomas depresivos en sus hijos.</li>
  </ul>

  <!-- SECCIÓN 8 -->
  <h2 class="section-title">8. Conclusión</h2>
  <p>
    La salud y el bienestar emocional no se logran prohibiendo o culpabilizando; se conquistan <strong>capacitando a las personas para cuidar de sí mismas y de su entorno</strong>.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> humaniza la promoción de la salud en la escuela andaluza: no actúa como un facultativo distante, sino como un pedagogo de proximidad que enseña a nombrar las emociones, educa en la afectividad respetuosa, previene las adicciones y construye entornos comunitarios donde crecer con salud, dignidad y alegría de vivir.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 15</h2>
  <p>Resumen estructurado de ejes conceptuales, marco regulador y praxis socioeducativa en salud:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Eje Temático</th>
        <th style="width: 38%;">Normativa y Planes de Referencia</th>
        <th style="width: 37%;">Conceptos e Implicación Práctica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Concepto de Salud</strong></td>
        <td>Carta de Ottawa (1986)<br>OMS (1948)<br>Red Europea SHE</td>
        <td>Visión holística (física, mental y social). La escuela como entorno promotor de entornos protectores de vida.</td>
      </tr>
      <tr>
        <td><strong>Determinantes Sociales</strong></td>
        <td>Michael Marmot<br>Ley 16/2011 de Salud Pública de Andalucía</td>
        <td>Gradiente social de salud: la pobreza y el contexto sociofamiliar condicionan la prevalencia de enfermedades. Equidad educativa.</td>
      </tr>
      <tr>
        <td><strong>Salud Mental Escolar</strong></td>
        <td>Estrategia de Salud Mental de Andalucía<br>Protocolo Autolesiones y Suicidio</td>
        <td>Detección de ansiedad, depresión y autolesiones no suicidas. Coordinación interdisciplinar con USMIJ del SAS.</td>
      </tr>
      <tr>
        <td><strong>Educación Emocional</strong></td>
        <td>Daniel Goleman<br>Rafael Bisquerra</td>
        <td>Conciencia, regulación emocional, tolerancia a la frustración y habilidades interpersonales asertivas.</td>
      </tr>
      <tr>
        <td><strong>Hábitos de Vida Saludable</strong></td>
        <td>Programa «Creciendo en Salud» (Infantil/Primaria)<br>«Forma Joven» (Secundaria)</td>
        <td>Alimentación mediterránea, ejercicio diario, descansos activos e higiene del sueño frente a la luz azul.</td>
      </tr>
      <tr>
        <td><strong>Educación Afectivo-Sexual</strong></td>
        <td>Ley 4/2023 (LGTBI y Trans)<br>Ley 8/2017 de Andalucía<br>Ley Orgánica 10/2022 («Solo sí es sí»)</td>
        <td>Consentimiento libre, métodos de barrera, respeto a la diversidad y deconstrucción de la pornografía violenta digital.</td>
      </tr>
      <tr>
        <td><strong>Adicciones Químicas</strong></td>
        <td>III Plan Andaluz sobre Drogas y Adicciones (PADA)</td>
        <td>Prevención de <em>binge drinking</em>, desmitificación del cannabis y cese de vapeadores. Derivación a CTA.</td>
      </tr>
      <tr>
        <td><strong>Adicciones Comportamentales</strong></td>
        <td>Estrategia Nacional sobre Adicciones<br>Ley del Juego</td>
        <td>Apuestas deportivas online, videojuegos compulsivos (cajas de botín) y tiranía de la validación en redes sociales.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Dinamizador de la Asesoría Forma Joven, talleres socioafectivos en POAT, escuelas de familias y trabajo en red comunitaria.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

html_path = "andalucia/Tema_15_Educacion_Salud_Bienestar_Adicciones.html"
pdf_path = "andalucia/Tema_15_Educacion_Salud_Bienestar_Adicciones.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {html_path}")
compile_pdf(html_path, pdf_path)
