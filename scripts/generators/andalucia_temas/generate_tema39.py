import os
from build_theme import compile_pdf

theme_num = 39
theme_title = "Tema 39: Educación de personas adultas y educación permanente como ámbito de acción de la Educación Social. La educación a lo largo de la vida. El modelo social. Normativa estatal y de Andalucía. Modelos y programas de intervención socioeducativa. Organización en Andalucía. El desarrollo comunitario como fin"
filename_base = "Tema_39_Educacion_Personas_Adultas_Educacion_Permanente_Desarrollo_Comunitario"

md_content = f"""# {theme_title}

## FICHA TÉCNICA
* **Cuerpo:** Cuerpo Técnico Facultativo, Opción Educación Social (A2.2018).
* **Junta de Andalucía** - Consejería de Desarrollo Educativo y Formación Profesional.
* **Materia:** Educación de personas adultas (EPA), Educación permanente (Lifelong Learning), andragogía (Knowles), pedagogía de la liberación (Freire), normativa estatal (LOMLOE arts. 66-70) y andaluza (LEA arts. 100-112, Decreto 196/2005 - CEPER/SEPER/IPEP), desarrollo comunitario.

---

## ÍNDICE SISTEMÁTICO

1. **INTRODUCCIÓN Y JUSTIFICACIÓN CONCEPTUAL**
   * 1.1. La Educación de Personas Adultas (EPA) y la Educación Permanente como derecho humano inalienable.
   * 1.2. Transición histórica: del modelo compensatorio-alfabetizador al paradigma del desarrollo integral y la emancipación.
   * 1.3. La Educación Social en la interfaz de la Educación Permanente: competencias del Educador/a Social.

2. **LA EDUCACIÓN A LO LARGO DE LA VIDA Y SUS IMPLICACIONES EN EL SISTEMA EDUCATIVO**
   * 2.1. Hitos internacionales y formulación doctrinal (UNESCO: Informes Faure 1972 y Delors 1996; CONFINTEA; Memorándum de la Comisión Europea 2000).
   * 2.2. Los cuatro pilares de la educación aplicados a la adultez (aprender a conocer, a hacer, a convivir y a ser).
   * 2.3. Implicaciones sistémicas: permeabilidad formativa, acreditación de aprendizajes formales, no formales e informales, y modularidad flexible.

3. **EL MODELO SOCIAL EN LA EDUCACIÓN PERMANENTE**
   * 3.1. Fundamentación teórica:
     * 3.1.1. La Andragogía de Malcolm Knowles y las características del aprendizaje adulto.
     * 3.1.2. La Pedagogía Crítica y la Concienciación de Paulo Freire: alfabetización liberadora frente a educación bancaria.
     * 3.1.3. La teoría del Aprendizaje Transformacional de Jack Mezirow.
   * 3.2. La educación permanente como respuesta frente a la brecha digital, las transiciones sociolaborales, la soledad no deseada y la exclusión social.

4. **LA EDUCACIÓN PERMANENTE Y DE PERSONAS ADULTAS EN LA NORMATIVA ESTATAL Y DE ANDALUCÍA**
   * 4.1. Marco estatal: Constitución Española (art. 27 y 40) y Ley Orgánica 2/2006 (LOE/LOMLOE, artículos 66 a 70 bis).
   * 4.2. Marco autonómico andaluz:
     * 4.2.1. Estatuto de Autonomía para Andalucía de 2007 (art. 21 y 52).
     * 4.2.2. Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA, Título II, Capítulo V, arts. 100 a 112).
     * 4.2.3. Decreto 196/2005, de 13 de septiembre, por el que se aprueba el Reglamento Orgánico de los Centros de Educación Permanente (CEPER).
     * 4.2.4. Oferta modular y modalidades: presencial, semipresencial y a distancia (IEDA).

5. **MODELOS Y PROGRAMAS DE INTERVENCIÓN SOCIOEDUCATIVA EN EDUCACIÓN PERMANENTE**
   * 5.1. Planes educativos formales (conducentes a titulación oficial):
     * 5.1.1. Formación Básica y Educación Secundaria Obligatoria para Personas Adultas (ESPA y ESPAD).
     * 5.1.2. Bachillerato para personas adultas y pruebas de acceso (Universidad +25/+45, Ciclos Formativos FP).
   * 5.2. Planes educativos no formales (planes de desarrollo y adaptación personal/comunitaria):
     * 5.2.1. Plan de fomento de la ciudadanía activa: interculturalidad, igualdad de género y hábitos de vida saludable.
     * 5.2.2. Plan de inclusión digital y superación de la brecha tecnológica.
     * 5.2.3. Español como lengua vehicular para población migrante.
     * 5.2.4. Conservación del patrimonio cultural andaluz y fomento de la memoria colectiva.
     * 5.2.5. Formación intergeneracional y Programas Universitarios de Mayores (Aulas de la Experiencia).

6. **LA ORGANIZACIÓN DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA**
   * 6.1. La Red Territorial de Centros:
     * 6.1.1. Centros de Educación Permanente (CEPER) y Secciones de Educación Permanente (SEPER).
     * 6.1.2. Institutos Provinciales de Educación Permanente (IPEP).
     * 6.1.3. Unidades y Aulas en Instituciones Penitenciarias.
   * 6.2. Órganos de gobierno, coordinación docente y participación de la comunidad en los CEPER.
   * 6.3. El papel del Instituto de Enseñanzas a Distancia de Andalucía (IEDA).

7. **EL DESARROLLO COMUNITARIO COMO FIN DE LA EDUCACIÓN PERMANENTE**
   * 7.1. Conexión dialéctica entre educación a lo largo de la vida, territorio y desarrollo local endógeno.
   * 7.2. Intervención en red: articulación de los CEPER con Servicios Sociales Comunitarios, Salud, CMIM y Tercer Sector.
   * 7.3. Metodologías participativas y proyectos comunitarios liderados por Educadores/as Sociales.

8. **CONCLUSIONES Y RETOS DE LA EDUCACIÓN PERMANENTE EN EL HORIZONTE ANDALUZ**
9. **ANEXO: CUADRO COMPARATIVO DE LA OFERTA Y ESTRUCTURA DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA**
"""

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{theme_title}</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {{
      content: counter(page);
      font-size: 9pt;
      color: #6b7280;
    }}
    @bottom-left {{
      content: "Cuerpo Técnico Facultativo A2.2018 - Educación Social (Junta de Andalucía)";
      font-size: 8pt;
      color: #9ca3af;
    }}
  }}
  body {{
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1f2937;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }}
  .cover {{
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 85vh;
    text-align: center;
    border: 3px double #7c3aed;
    padding: 30px;
    box-sizing: border-box;
  }}
  .cover h1 {{
    font-size: 20pt;
    color: #4c1d95;
    margin-bottom: 15px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .cover .badge {{
    background-color: #7c3aed;
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 9.5pt;
    font-weight: bold;
    margin-bottom: 25px;
    display: inline-block;
  }}
  .cover .meta-box {{
    background-color: #f5f3ff;
    border: 1px solid #ddd6fe;
    border-radius: 8px;
    padding: 18px;
    margin-top: 30px;
    text-align: left;
    width: 85%;
    font-size: 9pt;
  }}
  .toc-container {{
    page-break-after: always;
    padding: 20px 0;
  }}
  .toc-title {{
    font-size: 15pt;
    color: #4c1d95;
    border-bottom: 2px solid #7c3aed;
    padding-bottom: 6px;
    margin-bottom: 16px;
    text-transform: uppercase;
  }}
  .toc-item {{
    margin-bottom: 8px;
    font-size: 9.5pt;
  }}
  .toc-item.level-1 {{ font-weight: bold; color: #1e1b4b; margin-top: 10px; }}
  .toc-item.level-2 {{ margin-left: 15px; color: #374151; }}
  .toc-item.level-3 {{ margin-left: 30px; color: #4b5563; font-style: italic; }}

  h2.section-title {{
    color: #4c1d95;
    border-bottom: 1.5px solid #7c3aed;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 12px;
    font-size: 13pt;
    text-transform: uppercase;
    page-break-after: avoid;
  }}
  h3.sub-title {{
    color: #6d28d9;
    font-size: 10.5pt;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}
  h4.sub-sub-title {{
    color: #5b21b6;
    font-size: 9.5pt;
    margin-top: 10px;
    margin-bottom: 4px;
    page-break-after: avoid;
  }}
  p {{
    text-align: justify;
    margin-bottom: 8px;
    margin-top: 0;
  }}
  ul, ol {{
    margin-top: 4px;
    margin-bottom: 8px;
    padding-left: 20px;
  }}
  li {{
    margin-bottom: 4px;
    text-align: justify;
  }}
  .callout {{
    background-color: #faf5ff;
    border-left: 4px solid #7c3aed;
    padding: 10px 14px;
    margin: 12px 0;
    border-radius: 0 6px 6px 0;
    font-size: 9pt;
  }}
  .callout-title {{
    font-weight: bold;
    color: #5b21b6;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .norm-box {{
    background-color: #f8fafc;
    border-left: 4px solid #0284c7;
    padding: 10px 14px;
    margin: 12px 0;
    font-size: 9pt;
  }}
  .norm-title {{
    font-weight: bold;
    color: #0369a1;
    margin-bottom: 4px;
  }}
  .compare-container {{
    display: flex;
    gap: 12px;
    margin: 12px 0;
  }}
  .compare-box {{
    flex: 1;
    background: #fdf4ff;
    border: 1px solid #f0abfc;
    border-radius: 6px;
    padding: 10px;
    font-size: 8.5pt;
  }}
  .compare-title {{
    font-weight: bold;
    color: #86198f;
    margin-bottom: 6px;
    border-bottom: 1px solid #f0abfc;
    padding-bottom: 3px;
  }}
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 8.5pt;
  }}
  table.data-table th, table.data-table td {{
    border: 1px solid #e2e8f0;
    padding: 6px 8px;
    text-align: left;
  }}
  table.data-table th {{
    background-color: #f3e8ff;
    color: #4c1d95;
    font-weight: bold;
  }}
  table.data-table tr:nth-child(even) {{
    background-color: #faf5ff;
  }}
</style>
</head>
<body>

<div class="cover">
  <div class="badge">TEMARIO ESPECÍFICO - EDUCACIÓN SOCIAL (A2.2018)</div>
  <h1>TEMA 39</h1>
  <h2 style="font-size: 13.5pt; color: #5b21b6; font-weight: 600; max-width: 90%; margin-bottom: 25px;">
    EDUCACIÓN DE PERSONAS ADULTAS Y EDUCACIÓN PERMANENTE COMO ÁMBITO DE ACCIÓN DE LA EDUCACIÓN SOCIAL. LA EDUCACIÓN A LO LARGO DE LA VIDA Y SUS IMPLICACIONES EN EL SISTEMA EDUCATIVO. EL MODELO SOCIAL EN LA EDUCACIÓN PERMANENTE. LA EDUCACIÓN PERMANENTE Y DE PERSONAS ADULTAS EN LA NORMATIVA ESTATAL Y DE ANDALUCÍA. MODELOS Y PROGRAMAS DE INTERVENCIÓN SOCIOEDUCATIVA. ORGANIZACIÓN EN ANDALUCÍA. EL DESARROLLO COMUNITARIO COMO FIN DE LA EDUCACIÓN PERMANENTE.
  </h2>
  
  <div class="meta-box">
    <strong>Marco Jurídico y Doctrinal de Referencia:</strong>
    <ul style="margin: 6px 0 0 0; padding-left: 18px;">
      <li><strong>Estatal:</strong> CE (arts. 27 y 40), LOE/LOMLOE (Ley Orgánica 3/2020, Título I, Cap. IX, arts. 66 a 70 bis).</li>
      <li><strong>Andalucía:</strong> Estatuto de Autonomía de 2007 (art. 21 y 52), Ley 17/2007 (LEA, arts. 100 a 112), Decreto 196/2005 (Reglamento Orgánico de los Centros de Educación Permanente - CEPER).</li>
      <li><strong>Doctrina y Modelos:</strong> Malcolm Knowles (Andragogía), Paulo Freire (Pedagogía del Oprimido y Educación Liberadora), Jack Mezirow (Aprendizaje Transformacional), UNESCO (Informes Faure y Delors).</li>
    </ul>
  </div>
</div>

<div class="toc-container">
  <div class="toc-title">Índice General del Tema 39</div>
  <div class="toc-item level-1">1. INTRODUCCIÓN Y JUSTIFICACIÓN CONCEPTUAL</div>
  <div class="toc-item level-2">1.1. La Educación de Personas Adultas y la Educación Permanente como derecho inalienable</div>
  <div class="toc-item level-2">1.2. Transición histórica: del modelo compensatorio al paradigma del desarrollo integral</div>
  <div class="toc-item level-2">1.3. La Educación Social en la interfaz de la Educación Permanente</div>
  
  <div class="toc-item level-1">2. LA EDUCACIÓN A LO LARGO DE LA VIDA Y SUS IMPLICACIONES EN EL SISTEMA EDUCATIVO</div>
  <div class="toc-item level-2">2.1. Hitos internacionales y formulación doctrinal (UNESCO, Informes Faure y Delors, Memorándum Europeo)</div>
  <div class="toc-item level-2">2.2. Los cuatro pilares de la educación aplicados a la adultez</div>
  <div class="toc-item level-2">2.3. Implicaciones sistémicas: permeabilidad, acreditación de competencias y modularidad flexible</div>

  <div class="toc-item level-1">3. EL MODELO SOCIAL EN LA EDUCACIÓN PERMANENTE</div>
  <div class="toc-item level-2">3.1. Fundamentación teórica: Andragogía (Knowles), Pedagogía Crítica (Freire) y Aprendizaje Transformacional (Mezirow)</div>
  <div class="toc-item level-2">3.2. La educación permanente frente a la brecha digital, el desempleo y la exclusión social</div>

  <div class="toc-item level-1">4. LA EDUCACIÓN PERMANENTE Y DE PERSONAS ADULTAS EN LA NORMATIVA ESTATAL Y DE ANDALUCÍA</div>
  <div class="toc-item level-2">4.1. Marco estatal: Constitución Española y LOE/LOMLOE (arts. 66 a 70 bis)</div>
  <div class="toc-item level-2">4.2. Marco autonómico andaluz: LEA (arts. 100 a 112) y Decreto 196/2005 (CEPER)</div>
  <div class="toc-item level-2">4.3. Oferta modular y modalidades: presencial, semipresencial y a distancia (IEDA)</div>

  <div class="toc-item level-1">5. MODELOS Y PROGRAMAS DE INTERVENCIÓN SOCIOEDUCATIVA EN EDUCACIÓN PERMANENTE</div>
  <div class="toc-item level-2">5.1. Planes educativos formales conducentes a titulación oficial (ESPA, Bachillerato, Pruebas de acceso)</div>
  <div class="toc-item level-2">5.2. Planes educativos no formales (ciudadanía activa, inclusión digital, español para migrantes, memoria y patrimonio)</div>

  <div class="toc-item level-1">6. LA ORGANIZACIÓN DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA</div>
  <div class="toc-item level-2">6.1. La Red Territorial de Centros: CEPER, SEPER, IPEP y Aulas Penitenciarias</div>
  <div class="toc-item level-2">6.2. Órganos de gobierno, coordinación docente y participación en los CEPER</div>
  <div class="toc-item level-2">6.3. El papel del Instituto de Enseñanzas a Distancia de Andalucía (IEDA)</div>

  <div class="toc-item level-1">7. EL DESARROLLO COMUNITARIO COMO FIN DE LA EDUCACIÓN PERMANENTE</div>
  <div class="toc-item level-2">7.1. Conexión dialéctica entre educación a lo largo de la vida y desarrollo local endógeno</div>
  <div class="toc-item level-2">7.2. Intervención en red: articulación de los CEPER con Servicios Sociales Comunitarios y Salud</div>
  <div class="toc-item level-2">7.3. Metodologías participativas lideradas por Educadores/as Sociales</div>

  <div class="toc-item level-1">8. CONCLUSIONES Y RETOS DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA</div>
  <div class="toc-item level-1">9. ANEXO: CUADRO COMPARATIVO DE LA ESTRUCTURA Y PLANES DE LA EDUCACIÓN PERMANENTE</div>
</div>

<!-- CONTENIDO DESARROLLADO -->
<h2 class="section-title">1. INTRODUCCIÓN Y JUSTIFICACIÓN CONCEPTUAL</h2>
<h3 class="sub-title">1.1. La Educación de Personas Adultas y la Educación Permanente como derecho inalienable</h3>
<p>
  En las sociedades contemporáneas, marcadas por una acelerada digitalización, transiciones demográficas hacia el envejecimiento y profundas transformaciones en el mercado de trabajo, la educación ha dejado de ser un patrimonio exclusivo de la infancia y la juventud. La <strong>Educación Permanente (Lifelong Learning)</strong> y la <strong>Educación de Personas Adultas (EPA)</strong> se configuran como un derecho humano fundamental de carácter continuado que garantiza que toda persona, independientemente de su edad, condición socioeconómica, género o nivel cultural inicial, disponga de oportunidades reales para actualizar sus conocimientos, desarrollar sus potencialidades creativas y ejercer una ciudadanía crítica.
</p>
<p>
  La Educación Social encuentra en este ámbito uno de sus espacios de praxis más genuinos, superando la visión asistencialista tradicional y asumiendo una función eminentemente emancipadora y comunitaria.
</p>

<h3 class="sub-title">1.2. Transición histórica: del modelo compensatorio al paradigma del desarrollo integral</h3>
<p>
  La evolución de la educación de adultos ha transitado por tres grandes etapas conceptuales:
</p>
<div class="compare-container">
  <div class="compare-box">
    <div class="compare-title">1. Modelo Compensatorio / Reparador (S. XIX - Mediados S. XX)</div>
    <p>Concebía la educación de adultos como un "remedio tardío" destinado a suplir los déficits de escolarización infantil. Su núcleo exclusivo era la alfabetización instrumental elemental (lectoescritura y cálculo aritmético básico), bajo una relación jerárquica y escolarizante.</p>
  </div>
  <div class="compare-box">
    <div class="compare-title">2. Modelo Tecnocrático / Capital Humano (Años 60 - 80)</div>
    <p>Ligado al auge de la industrialización y la formación profesional continua. La meta prioritaria era la adaptación técnico-laboral del trabajador a las exigencias productivas de las empresas, subordinando lo social a lo económico.</p>
  </div>
  <div class="compare-box">
    <div class="compare-title">3. Modelo Social y Emancipador (Finales S. XX - Actualidad)</div>
    <p>Paradigma de la educación a lo largo de toda la vida. Entiende la educación permanente como un proceso global de maduración personal, participación cívica, inclusión sociocomunitaria, juicio crítico y cohesión democrática.</p>
  </div>
</div>

<h3 class="sub-title">1.3. La Educación Social en la interfaz de la Educación Permanente</h3>
<p>
  El Educador o Educadora Social desempeña en la Educación Permanente un rol dinamizador singular:
</p>
<ul>
  <li><strong>Detección de necesidades formativas invisibilizadas:</strong> Especialmente en colectivos en exclusión (inmigrantes, personas gitanas, mayores aislados, parados de larga duración).</li>
  <li><strong>Orientación socioeducativa personalizada:</strong> Diseño de itinerarios vitales de inserción y retorno al sistema educativo formal.</li>
  <li><strong>Animación sociocultural y desarrollo local:</strong> Vinculación directa de los centros de educación de adultos con el tejido asociativo y las iniciativas vecinales.</li>
</ul>

<h2 class="section-title">2. LA EDUCACIÓN A LO LARGO DE LA VIDA Y SUS IMPLICACIONES EN EL SISTEMA EDUCATIVO</h2>
<h3 class="sub-title">2.1. Hitos internacionales y formulación doctrinal</h3>
<p>
  El armazón conceptual de la educación a lo largo de la vida ha sido forjado a través de conferencias y documentos de alcance mundial:
</p>
<div class="norm-box">
  <div class="norm-title">Grandes Hitos de la Educación Permanente</div>
  <ul>
    <li><strong>Informe Faure (UNESCO, 1972) - «Aprender a ser»:</strong> Plantea por primera vez la "ciudad educativa", donde la educación trasciende los muros escolares y abarca toda la vida humana y todas las instituciones sociales.</li>
    <li><strong>Informe Delors (UNESCO, 1996) - «La educación encierra un tesoro»:</strong> Consagra la educación a lo largo de la vida como la clave para acceder al siglo XXI, sustentada en cuatro pilares fundamentales.</li>
    <li><strong>Conferencias Internacionales de Educación de Adultos (CONFINTEA de la UNESCO):</strong> Desde Elsinor (1949), pasando por Hamburgo (CONFINTEA V, 1997 - Declaración sobre el Aprendizaje de Adultos) hasta Marrakech (CONFINTEA VII, 2022 - Marco de Acción de Marrakech), consolidando la EPA como bien público global y motor de los Objetivos de Desarrollo Sostenible (ODS 4).</li>
    <li><strong>Memorándum sobre el Aprendizaje Permanente (Comisión Europea, 2000):</strong> Define las directrices europeas para la empleabilidad, la ciudadanía activa y la inclusión social.</li>
  </ul>
</div>

<h3 class="sub-title">2.2. Los cuatro pilares de la educación aplicados a la adultez</h3>
<p>
  El Informe Delors reformuló los fines educativos en cuatro dimensiones que cobran plena vigencia en la persona adulta:
</p>
<ol>
  <li><strong>Aprender a conocer:</strong> Adquirir instrumentos de comprensión, pensamiento crítico frente a la infoxicación mediática y herramientas de "aprender a aprender".</li>
  <li><strong>Aprender a hacer:</strong> Capacitarse no solo para adquirir cualificaciones laborales rutinarias, sino para afrontar situaciones imprevistas y trabajar en equipo en contextos de incertidumbre.</li>
  <li><strong>Aprender a vivir juntos (a convivir):</strong> Desarrollar la comprensión del otro, resolver pacíficamente los conflictos y participar solidariamente en proyectos comunitarios plurales.</li>
  <li><strong>Aprender a ser:</strong> Favorecer la autonomía moral, la responsabilidad personal, la autorrealización estética, emocional y espiritual a lo largo de todas las etapas biográficas.</li>
</ol>

<h3 class="sub-title">2.3. Implicaciones sistémicas en el sistema educativo</h3>
<p>
  El paradigma de la educación a lo largo de la vida exige una transformación radical de las estructuras escolares tradicionales:
</p>
<ul>
  <li><strong>Ruptura del monopolio cronológico:</strong> La formación deja de ser una etapa cerrada que culmina a los 16, 18 o 24 años para convertirse en un flujo continuo y recurrente.</li>
  <li><strong>Permeabilidad entre educación formal, no formal e informal:</strong> Mecanismos oficiales de reconocimiento y acreditación de las competencias adquiridas mediante la experiencia laboral o el voluntariado (Real Decreto 143/2021).</li>
  <li><strong>Flexibilización y modularidad:</strong> Planes de estudio organizados en módulos y créditos independientes que permiten conciliar la formación con la vida familiar y laboral.</li>
</ul>

<h2 class="section-title">3. EL MODELO SOCIAL EN LA EDUCACIÓN PERMANENTE</h2>
<h3 class="sub-title">3.1. Fundamentación teórica del aprendizaje adulto</h3>
<p>
  La intervención socioeducativa con personas adultas requiere un enfoque psicopedagógico propio, alejado de la pedagogía infantil tradicional:
</p>

<h4 class="sub-sub-title">3.1.1. La Andragogía de Malcolm Knowles</h4>
<p>
  Knowles define la <em>andragogía</em> como el arte y la ciencia de ayudar a los adultos a aprender, diferenciándola de la pedagogía basada en la heteronomía del menor. Sus principios fundamentales son:
</p>
<ul>
  <li><strong>Autoconcepto del aprendiz:</strong> El adulto transita de una personalidad dependiente a un ser autodirigido que necesita ser respetado en su autonomía decisional.</li>
  <li><strong>Reservorio de experiencia acumulada:</strong> La biografía de la persona adulta es el recurso de aprendizaje más rico; los nuevos conocimientos deben anclarse dialécticamente en sus vivencias previas.</li>
  <li><strong>Disposición para aprender:</strong> El interés formativo surge directamente de las tareas y retos del desarrollo vital (crianza, cambio de empleo, jubilación).</li>
  <li><strong>Orientación del aprendizaje:</strong> Enfoque centrado en problemas reales de la vida cotidiana y no en contenidos disciplinares abstractos.</li>
  <li><strong>Motivación intrínseca:</strong> Prevalencia de la autoestima, la satisfacción personal y el reconocimiento social por encima de las recompensas externas.</li>
</ul>

<h4 class="sub-sub-title">3.1.2. La Pedagogía Crítica y la Concienciación de Paulo Freire</h4>
<p>
  Paulo Freire revolucionó la educación de adultos con obras cumbres como <em>«La pedagogía del oprimido»</em> y <em>«La educación como práctica de la libertad»</em>. Freire combate la <strong>educación bancaria</strong>, aquella que concibe al educando como una vasija vacía en la que el educador deposita información acrítica para reproducir el orden social.
</p>
<p>
  Frente a ella, postula la <strong>educación problematizadora y liberadora</strong>:
</p>
<div class="callout">
  <div class="callout-title">Principios Freirianos en la Intervención con Adultos</div>
  <ul>
    <li><strong>«Nadie educa a nadie, nadie se educa solo, los hombres se educan entre sí mediatizados por el mundo»:</strong> Relación horizontal y dialógica entre educador y educando.</li>
    <li><strong>Palabras y temas generadores:</strong> La alfabetización parte de la indagación del universo vocabular y las preocupaciones vitales de la comunidad (el salario, la salud, la vivienda, la tierra).</li>
    <li><strong>Lectura del mundo y lectura de la palabra:</strong> Aprender a leer las letras es indisociable de aprender a "leer críticamente la realidad" para desmitificar las causas estructurales de la opresión y actuar para transformarla (praxis: acción + reflexión).</li>
  </ul>
</div>

<h4 class="sub-sub-title">3.1.3. La teoría del Aprendizaje Transformacional de Jack Mezirow</h4>
<p>
  Mezirow explica cómo los adultos transforman sus <em>marcos de referencia</em> (creencias implícitas, sesgos culturales, asunciones no cuestionadas). El proceso se desencadena habitualmente a partir de un <em>dilema desorientador</em> (una crisis vital, una migración, una pérdida de empleo) que motiva un autoexamen crítico, la formulación de nuevas hipótesis sobre la vida y la asunción de nuevos roles sociales empoderados.
</p>

<h3 class="sub-title">3.2. La educación permanente frente a los retos sociales contemporáneos</h3>
<p>
  En el actual contexto socioeconómico andaluz, el modelo social de educación permanente actúa como trinchera y escudo frente a:
</p>
<ul>
  <li><strong>La Brecha Digital:</strong> Capacitación crítica frente al apagón analógico en trámites sanitarios, bancarios y de la administración electrónica, que amenaza con excluir masivamente a mayores y colectivos desfavorecidos.</li>
  <li><strong>La Vulnerabilidad Laboral:</strong> Recualificación de personas trabajadoras con baja cualificación o expulsadas de sectores en reconversión.</li>
  <li><strong>La Soledad No Deseada:</strong> Los centros de educación de adultos actúan como auténticas redes de apoyo social y espacios convivenciales protectores de la salud mental comunitaria.</li>
</ul>

<h2 class="section-title">4. LA EDUCACIÓN PERMANENTE Y DE PERSONAS ADULTAS EN LA NORMATIVA ESTATAL Y DE ANDALUCÍA</h2>
<h3 class="sub-title">4.1. Marco normativo estatal</h3>
<p>
  La <strong>Constitución Española de 1978</strong> reconoce en su artículo 27 el derecho universal a la educación, encomendando en su artículo 40 a los poderes públicos el fomento de una política formativa y de readaptación profesional continuada.
</p>
<p>
  La <strong>Ley Orgánica 2/2006, de 3 de mayo, de Educación (LOE)</strong>, tras las modificaciones introducidas por la <strong>LOMLOE (Ley Orgánica 3/2020)</strong>, regula la Educación de Personas Adultas en su <em>Título I, Capítulo IX (artículos 66 a 70 bis)</em>:
</p>
<div class="norm-box">
  <div class="norm-title">Preceptos Clave de la LOMLOE en Educación de Adultos</div>
  <ul>
    <li><strong>Finalidad (art. 66):</strong> Ofrecer a todas las personas mayores de 18 años (excepcionalmente mayores de 16 con contrato laboral o deportistas de alto rendimiento) la posibilidad de adquirir, actualizar o completar sus conocimientos para su desarrollo personal y profesional.</li>
    <li><strong>Objetivos (art. 66.3):</strong> Adquirir una formación básica, ampliar y renovar conocimientos y capacidades, desarrollar habilidades de participación democrática, anticipar y resolver conflictos familiares y sociales, y dominar las nuevas tecnologías de la información.</li>
    <li><strong>Organización y pruebas libres (arts. 67 y 68):</strong> Flexibilidad horaria y metodológica, adaptación curricular y convocatorias anuales de pruebas oficiales para la obtención del título de Graduado en ESO y Técnico de FP.</li>
  </ul>
</div>

<h3 class="sub-title">4.2. Marco normativo autonómico andaluz</h3>
<p>
  El <strong>Estatuto de Autonomía para Andalucía (Ley Orgánica 2/2007)</strong> establece en su artículo 21 el derecho a una educación pública de calidad a lo largo de toda la vida y consagra en su artículo 52 las competencias exclusivas de la Junta en materia de enseñanza.
</p>
<p>
  La <strong>Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA)</strong> regula de manera pormenorizada la Educación Permanente en su <em>Título II, Capítulo V (artículos 100 a 112)</em>:
</p>
<ul>
  <li><strong>Principios rectores (art. 101):</strong> Accesibilidad universal, adaptación a la realidad territorial andaluza, fomento de la ciudadanía democrática, enfoque de género, impulso de la cultura andaluza y cooperación interinstitucional.</li>
  <li><strong>Estructura organizativa (art. 106 y 107):</strong> Establece una red pública articulada en Centros de Educación Permanente (CEPER) y Secciones de Educación Permanente (SEPER), así como Institutos Provinciales de Educación Permanente (IPEP).</li>
  <li><strong>Reglamento Orgánico (Decreto 196/2005, de 13 de septiembre):</strong> Define la tipología, competencias de los órganos unipersonales y colegiados (Dirección, Jefatura de Estudios, Consejo de Centro y Claustro) de los CEPER andaluces.</li>
</ul>

<h2 class="section-title">5. MODELOS Y PROGRAMAS DE INTERVENCIÓN SOCIOEDUCATIVA EN EDUCACIÓN PERMANENTE</h2>
<p>
  El sistema andaluz de educación permanente vertebra su intervención a través de una doble tipología de planes educativos:
</p>

<h3 class="sub-title">5.1. Planes educativos formales (conducentes a titulación oficial)</h3>
<table class="data-table">
  <thead>
    <tr>
      <th style="width: 25%;">Denominación del Plan</th>
      <th style="width: 35%;">Colectivo Destinatario y Finalidad</th>
      <th style="width: 40%;">Modalidades y Estructura Curricular</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Formación Básica de Personas Adultas</strong></td>
      <td>Personas adultas sin alfabetización inicial o con escolarización incompleta. Adquisición de competencias lectoescritoras y de cálculo.</td>
      <td>Nivel I (Iniciación / Alfabetización) y Nivel II (Consolidación). Metodología globalizada y adaptada a ritmos individuales.</td>
    </tr>
    <tr>
      <td><strong>Educación Secundaria para Personas Adultas (ESPA / ESPAD)</strong></td>
      <td>Ciudadanos mayores de 18 años que buscan obtener el título de Graduado en ESO, requisito clave para el empleo y el acceso a FP.</td>
      <td>Estructurada en tres ámbitos: Ámbito de Comunicación, Ámbito Científico-Tecnológico y Ámbito Social. Opciones presencial y a distancia (ESPAD).</td>
    </tr>
    <tr>
      <td><strong>Bachillerato para Personas Adultas</strong></td>
      <td>Adultos que precisan el título de Bachiller para inserción profesional cualificada o acceso a estudios universitarios.</td>
      <td>Organizado de forma modular por materias sueltas. Modalidades presencial (nocturno/vespertino), semipresencial y a distancia.</td>
    </tr>
    <tr>
      <td><strong>Planes de Preparación de Pruebas de Acceso</strong></td>
      <td>Personas que desean superar las pruebas de acceso a Ciclos Formativos de Grado Medio o Superior, y a la Universidad para mayores de 25 y 45 años.</td>
      <td>Cursos de refuerzo en materias comunes (Lengua, Comentario de Texto, Idioma extranjero) y materias específicas de rama.</td>
    </tr>
  </tbody>
</table>

<h3 class="sub-title">5.2. Planes educativos no formales (planes de desarrollo personal y comunitario)</h3>
<p>
  Conforme a las Instrucciones anuales de la Dirección General de Formación del Profesorado e Innovación Educativa, los CEPER imparten planes no formales de alto impacto socioeducativo:
</p>
<div class="callout">
  <div class="callout-title">Planes No Formales de Educación Permanente en Andalucía</div>
  <ul>
    <li><strong>Plan de Fomento de la Ciudadanía Activa:</strong> Cursos de debate, hábitos de consumo responsable, coeducación e igualdad, y prevención de la violencia de género.</li>
    <li><strong>Plan de Transformación Digital y TIC:</strong> Alfabetización digital desde cero: manejo de smartphones, gestión de citas médicas (ClicSalud+), certificados digitales y banca online segura.</li>
    <li><strong>Español como Lengua Vehicular para Personas Migrantes:</strong> Aprendizaje de la lengua española no como ejercicio gramatical abstracto, sino como llave de acogida, acceso al empleo y regularización administrativa.</li>
    <li><strong>Patrimonio Cultural Andaluz y Memoria Histórica Democrática:</strong> Talleres de recuperación de la tradición oral, oficios artesanales, rutas patrimoniales locales y ecología barrial.</li>
    <li><strong>Aulas de Mayores y Relaciones Intergeneracionales:</strong> Convenios entre la Consejería y las Universidades públicas andaluzas (Aulas de la Experiencia) para acercar el conocimiento científico y humanístico a los mayores de 55 años.</li>
  </ul>
</div>

<h2 class="section-title">6. LA ORGANIZACIÓN DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA</h2>
<h3 class="sub-title">6.1. La Red Territorial de Centros</h3>
<p>
  Andalucía cuenta con una de las redes públicas de educación permanente más extensas de Europa, vertebrada territorialmente para garantizar la equidad rural y urbana:
</p>
<ul>
  <li><strong>Centros de Educación Permanente (CEPER):</strong> Centros cabecera comarcales o de municipios de tamaño medio, dotados de equipo directivo propio, claustro docente y consejo de centro.</li>
  <li><strong>Secciones de Educación Permanente (SEPER):</strong> Aulas descentralizadas situadas en pedanías, pequeñas localidades rurales o barriadas periféricas dependientes pedagógica y administrativamente de un CEPER cabecera, evitando la despoblación y el desarraigo de la población rural.</li>
  <li><strong>Institutos Provinciales de Educación Permanente (IPEP):</strong> Centros ubicados en las capitales de provincia especializados en la impartición de enseñanzas formales de Bachillerato y ESPA en turnos de tarde/noche y modalidades a distancia.</li>
  <li><strong>Centros y Aulas en Establecimientos Penitenciarios:</strong> Red de unidades docentes adscritas a los CEPER que garantizan el derecho a la educación de la población reclusa en los centros penitenciarios andaluces (Albolote, Sevilla-II, Algeciras, etc.).</li>
</ul>

<h3 class="sub-title">6.2. Órganos de gobierno y participación (Decreto 196/2005)</h3>
<p>
  El gobierno de los CEPER se organiza a través de órganos unipersonales (Director/a y Jefe/a de Estudios) y órganos colegiados:
</p>
<ul>
  <li><strong>Consejo de Centro:</strong> Máximo órgano colegiado de gobierno, donde participan la dirección, el profesorado, representantes del alumnado adulto, personal de administración y servicios, y un representante del Ayuntamiento de la localidad.</li>
  <li><strong>Claustro de Profesorado:</strong> Órgano de responsabilidad técnica y planificación didáctica.</li>
</ul>

<h3 class="sub-title">6.3. El Instituto de Enseñanzas a Distancia de Andalucía (IEDA)</h3>
<p>
  Centro público específico que ofrece enseñanzas regladas semipresenciales y telemáticas a través de plataformas Moodle avanzadas, permitiendo que cualquier persona andaluza o residente en el exterior acceda a la formación con tutorización telemática síncrona y asíncrona.
</p>

<h2 class="section-title">7. EL DESARROLLO COMUNITARIO COMO FIN DE LA EDUCACIÓN PERMANENTE</h2>
<h3 class="sub-title">7.1. Conexión dialéctica entre educación y desarrollo local endógeno</h3>
<p>
  La Educación Permanente trasciende con creces los límites de la institución escolar; su horizonte ontológico es el <strong>desarrollo comunitario endógeno</strong>. Como preconizaban autores de la Pedagogía Social como Marco Marchioni o Quintana Cabanas, una comunidad que aprende es una comunidad capaz de autodeterminar su futuro económico, cultural y social.
</p>
<p>
  En los municipios andaluces, los CEPER actúan como verdaderos centros cívicos donde se articulan cooperativas de mujeres rurales, asociaciones culturales, proyectos de huertos urbanos y asambleas vecinales.
</p>

<h3 class="sub-title">7.2. Intervención en red y sinergias interinstitucionales</h3>
<p>
  El éxito socioeducativo de la educación permanente reside en su capacidad de trabajo colaborativo intersectorial:
</p>
<div class="callout">
  <div class="callout-title">Nodos de Articulación Comunitaria del CEPER</div>
  <ul>
    <li><strong>Servicios Sociales Comunitarios:</strong> Derivación de perceptores de la Renta Mínima de Inserción Social (RMISA / IMV) para el cumplimiento de sus itinerarios de inclusión social activa.</li>
    <li><strong>Centros Municipales de Información a la Mujer (CMIM):</strong> Talleres conjuntos de empoderamiento, autoestima y salida del ciclo de la violencia de género para mujeres del medio rural.</li>
    <li><strong>Centros de Salud de Atención Primaria:</strong> Programas de promoción de estilos de vida saludables, envejecimiento activo y prevención del sedentarismo.</li>
    <li><strong>Servicio Andaluz de Empleo (SAE):</strong> Coordinación para la acreditación de competencias profesionales y orientación sociolaboral.</li>
  </ul>
</div>

<h3 class="sub-title">7.3. Metodologías participativas y rol del Educador Social</h3>
<p>
  El Educador o Educadora Social aplica en este marco metodologías comunitarias avanzadas:
</p>
<ul>
  <li><strong>Investigación-Acción Participativa (IAP):</strong> Diagnósticos colectivos donde la propia población adulta investiga sus problemas y co-diseña los planes formativos.</li>
  <li><strong>Mapeo de Activos Comunitarios:</strong> Identificación de talentos vecinales, espacios públicos infrautilizados y redes informales de cuidado.</li>
  <li><strong>Proyectos de Aprendizaje-Servicio Intergeneracional:</strong> Encuentros donde personas mayores alfabetizadas transmiten la historia viva del barrio a jóvenes estudiantes de secundaria, y estos a su vez capacitan a los mayores en el uso de smartphones y redes sociales.</li>
</ul>

<h2 class="section-title">8. CONCLUSIONES Y RETOS DE LA EDUCACIÓN PERMANENTE EN ANDALUCÍA</h2>
<p>
  La Educación Permanente de personas adultas no es un apéndice secundario del sistema educativo andaluz, sino la <strong>garantía de que nadie quede atrás</strong> en una sociedad en constante metamorfosis. Es la respuesta democrática frente al fatalismo de la exclusión social, reconociendo que todo ser humano posee una capacidad inagotable de transformación a lo largo de su curso vital.
</p>
<p>
  Los retos futuros pasan por consolidar la inclusión digital ética, reforzar la oferta educativa en zonas rurales despobladas, universalizar la acogida lingüística a la población migrante y afianzar la figura del <strong>Educador y Educadora Social</strong> en los CEPER y SEPER como articulador indispensable del desarrollo comunitario y la justicia social en Andalucía.
</p>

<div style="page-break-before: always;"></div>
<h2 class="section-title">9. ANEXO: CUADRO COMPARATIVO DE LA ESTRUCTURA Y PLANES DE LA EDUCACIÓN PERMANENTE</h2>

<table class="data-table">
  <thead>
    <tr>
      <th style="width: 20%;">Tipología de Red / Plan</th>
      <th style="width: 25%;">Institución / Espacio</th>
      <th style="width: 30%;">Contenidos Formativos / Objetivos</th>
      <th style="width: 25%;">Rol del Educador/a Social</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Red Territorial Descentralizada</strong></td>
      <td><strong>CEPER y SEPER</strong><br>(Centros y Secciones de Educación Permanente)</td>
      <td>Formación básica, planes de ciudadanía activa, TIC, patrimonio y alfabetización en núcleos urbanos y rurales.</td>
      <td>Diagnóstico de necesidades vecinales, mediación intercultural y vinculación con Servicios Sociales Comunitarios.</td>
    </tr>
    <tr>
      <td><strong>Enseñanzas Regladas Avanzadas</strong></td>
      <td><strong>IPEP</strong><br>(Institutos Provinciales de Educación Permanente)</td>
      <td>Bachillerato y ESPA oficial en turnos nocturnos, semipresenciales o a distancia para personas trabajadoras.</td>
      <td>Orientación vocacional y socioeducativa, prevención del abandono escolar tardío y apoyo psicoafectivo.</td>
    </tr>
    <tr>
      <td><strong>Contextos de Privación de Libertad</strong></td>
      <td><strong>Aulas en Centros Penitenciarios</strong></td>
      <td>Garantía del derecho a la educación reglada de internos en prisiones andaluzas.</td>
      <td>Acompañamiento socioeducativo, preparación para la libertad condicional y mediación tratamental.</td>
    </tr>
    <tr>
      <td><strong>Planes No Formales Comunitarios</strong></td>
      <td><strong>Aulas Comunitarias y Convenios Locales</strong></td>
      <td>Español para personas extranjeras, brecha digital, igualdad de género y Aulas Universitarias de Mayores.</td>
      <td>Dinamización asamblearia, diseño de proyectos intergeneracionales y mapeo de activos de salud.</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""

# Write MD and HTML files
md_path = os.path.join("andalucia", f"{filename_base}.md")
html_path = os.path.join("andalucia", f"{filename_base}.html")
pdf_path = os.path.join("andalucia", f"{filename_base}.pdf")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")

compile_pdf(html_path, pdf_path)
