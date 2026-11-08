import os
from build_theme import compile_pdf

md_content = """# TEMA 36: Las Redes Sociales. Características y Elementos de las Redes Sociales. Redes Sociales en el Contexto Urbano y Rural. La Comunidad Educativa como Red Social: Agentes, Relaciones de Comunicación y Estrategias para la Formación. Factores que Favorecen las Relaciones en la Comunidad Educativa

---

## FICHA TÉCNICA DEL TEMA
* **Cuerpo:** Cuerpo Técnico Facultativo de la Junta de Andalucía
* **Especialidad:** Educación Social (A2.2018)
* **Carácter:** Materias Específicas del Programa Oficial
* **Marco Legal y Documental:**
  - Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA), arts. 14 a 19 (Comunidad educativa y participación).
  - Ley Orgánica 2/2006 (LOE), modificada por la LOMLOE 3/2020.
  - Decreto 327/2010 y Decreto 328/2010 (Reglamentos Orgánicos de Centros Docentes en Andalucía).
  - Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales.
  - Instrucciones de 17 de septiembre de 2010 de la Dirección General de Participación e Innovación Educativa.
* **Autores y Doctrinas de Referencia:** Mark Granovetter (La fuerza de los lazos débiles), Manuel Castells (La sociedad red), Barry Wellman (El individualismo en red), Robert Putnam (Capital social y redes comunitarias), Carlos Lozares (Teoría y análisis de redes sociales - ARS).

---

## ÍNDICE DE CONTENIDOS
1. Introducción y fundamentación sociológica del concepto de red social en la Educación Social.
2. Características y elementos estructurales de las redes sociales:
   - 2.1. Nodos, vínculos, aristas, densidad y centralidad.
   - 2.2. Tipología de vínculos: Lazos fuertes vs. lazos débiles (Mark Granovetter).
   - 2.3. Redes naturales primarias, redes institucionales y redes digitales.
3. Las redes sociales en el contexto territorial andaluz:
   - 3.1. Ecosistema urbano: Complejidad, anomia, fragmentación y recursos especializados.
   - 3.2. Ecosistema rural: Capital social de proximidad, apoyo mutuo y el papel de los Colegios Públicos Rurales (CPR).
4. La Comunidad Educativa entendida como red social integrada:
   - 4.1. Agentes y nodos de la red escolar (alumnado, familias, claustro, PAS, barrio).
   - 4.2. Flujos y dinámicas de comunicación formal e informal (Plataformas Séneca e iPasen vs. comunicación presencial).
5. Estrategias socioeducativas para la formación y alfabetización en redes:
   - 5.1. Competencia digital crítica frente a las redes sociales digitales (ciberacoso, huella digital).
   - 5.2. Escuelas de Familias y formación intergeneracional en entornos virtuales.
6. Factores que favorecen y dinamizan las relaciones en la Comunidad Educativa:
   - 6.1. Clima de confianza institucional y liderazgo distribuido.
   - 6.2. Metodologías comunitarias: Comunidades de Aprendizaje y Aprendizaje-Servicio (ApS).
7. Actuación e intervención del educador o educadora social como dinamizador/a de redes.
8. Conclusión.
9. Anexo: Mapa conceptual y tabla sinóptica del Tema 36.

---

## 1. Introducción y fundamentación sociológica del concepto de red social

El concepto de **red social** no nació con las plataformas digitales del siglo XXI; constituye una categoría sociológica clásica fundamental formulada por la antropología social y la sociología comunitaria para explicar cómo se estructura la vida humana, cómo circula la información y cómo se genera la solidaridad y el apoyo mutuo (Carlos Lozares, Robert Putnam).

En la era contemporánea, caracterizada por la **sociedad red y el individualismo conectado** (Manuel Castells, Barry Wellman), los seres humanos construyen sus identidades y afectos en una constante articulación entre redes territoriales de proximidad y redes virtuales globales.

Para la **Educación Social**, concebir el centro escolar y su territorio como una **red social viva** supone superar la visión cerrada de la escuela como un edificio estático para entenderla como un **ecosistema dialógico de relaciones, apoyos y sinergias**. El Educador y la Educadora Social ejerce como el "tejedor de redes" (*networker social*) que conecta los nodos aislados, fortalece el capital social comunitario y garantiza que ningún estudiante o familia caiga en el vacío del desarraigo.

---

## 2. Características y elementos estructurales de las redes sociales

El Análisis de Redes Sociales (ARS) define la red como un conjunto delimitado de actores interconectados:
* **Nodos o Vértices:** Actores individuales (un alumno, una madre, un maestro) o colectivos (un aula, el AMPA, un centro de salud).
* **Vínculos o Aristas:** Lazos relacionales que unen a los nodos (comunicación, afecto, parentesco, ayuda económica, intercambio de información).
* **Densidad:** Proporción entre los vínculos existentes y los vínculos teóricamente posibles; una alta densidad favorece la cohesión y el apoyo mutuo.
* **Centralidad:** Grado de influencia o intermediación de un nodo para conectar a otros miembros de la red.

```
                      LA TEORÍA DE LOS LAZOS (GRANOVETTER)
 ┌────────────────────────────────────┬────────────────────────────────────┐
 │ LAZOS FUERTES (Afecto / Familia)   │ LAZOS DÉBILES (Conexión / Puente)  │
 ├────────────────────────────────────┼────────────────────────────────────┤
 │ • Relaciones íntimas y cotidianas  │ • Contactos esporádicos con otros  │
 │ • Alta reciprocidad y apoyo en     │   círculos sociales e instituciones│
 │   crisis inmediatas                │ • Puerta al empleo, a la cultura   │
 │ • Redundancia de información       │   y a la movilidad social          │
 └────────────────────────────────────┴────────────────────────────────────┘
```

Mark Granovetter demostró en su célebre tesis sobre *La fuerza de los lazos débiles* que, aunque los lazos fuertes proporcionan seguridad emocional básica, **son los lazos débiles los que permiten salir de la exclusión**, acceder a nuevas oportunidades laborales y ensanchar los horizontes culturales.

---

## 3. Las redes sociales en el contexto territorial andaluz: Urbano vs. Rural

Andalucía presenta una acusada diversidad sociodemográfica que modula la naturaleza de las redes:

### 3.1. Ecosistema Urbano y Barrios Desfavorecidos
* Ciudades medias y grandes áreas metropolitanas donde abunda una densa red de servicios especializados (hospitales, USMIJ, centros cívicos, ONGs).
* Riesgo de **anomia social, atomización, soledad no deseada y guetización** de zonas vulnerables, donde los lazos comunitarios tradicionales se han erosionado por la precariedad y el individualismo.

### 3.2. Ecosistema Rural y Pueblos Andaluces
* Fuerte arraigo de **redes primarias de apoyo vecinal e intergeneracional**, gran solidaridad en situaciones de enfermedad y control social informal protector.
* Riesgos asociados a la dispersión geográfica, el aislamiento de comarcas de montaña, la brecha de infraestructuras y el peligro de mayor control moral asfixiante sobre la diversidad.
* **Papel Vertebrador de los Colegios Públicos Rurales (CPR):** En el mundo rural andaluz, la escuela no es solo un lugar de clases; es el corazón social, cívico y cultural que mantiene vivo al pueblo y frena la despoblación.

---

## 4. La Comunidad Educativa entendida como red social integrada

La Comunidad Educativa regulada en el artículo 14 de la LEA es una red social compleja:
* **Nodos Nucleares:** Alumnado, profesorado, familias, personal de administración y servicios (PAS) y equipo directivo.
* **Nodos Comunitarios:** Servicios Sociales Comunitarios, centros de salud, Policía Local (Agente Tutor), bibliotecas de barrio, clubes deportivos y asociaciones de vecinos.
* **Canales de Comunicación:**
  - *Canales Formales Digitales:* Plataforma corporativa **Séneca** y la aplicación para familias **iPasen**, que agilizan las justificaciones de faltas y la comunicación de notas.
  - *Canales Presenciales e Informales:* La puerta de entrada del colegio a las 9:00, las tutorías presenciales y los encuentros en las actividades extraescolares.

---

## 5. Estrategias socioeducativas para la formación en redes

La irrupción masiva de las redes sociales virtuales (Instagram, TikTok, WhatsApp) en la infancia y adolescencia exige una intervención educativa decidida:
* **Alfabetización Mediática y Digital Crítica:** Capacitar a los jóvenes no solo en el uso técnico del móvil, sino en la **deconstrucción de la tiranía del "like", la prevención del ciberacoso escolar y la protección de su intimidad**.
* **Escuelas de Familias sobre Higiene Digital:** Asesoramiento a progenitores para establecer límites razonables de uso, desactivar pantallas en las horas de sueño y detectar precozmente adicciones a videojuegos o apuestas online.

---

## 6. Factores que favorecen las relaciones en la Comunidad Educativa

La literatura socioeducativa identifica factores indispensables para tejer una red escolar sólida:
1. **Clima Institucional de Confianza y Transparencia:** La dirección y el claustro deben acoger a las familias con escucha honesta, superando la desconfianza burocrática.
2. **Liderazgo Distribuido y Democrático:** Apertura de espacios reales donde el alumnado y las familias tomen decisiones significativas.
3. **Metodologías Cooperativas y Comunitarias:**
   - *Comunidades de Aprendizaje:* Actuaciones de éxito que sientan a familias y vecinos en las aulas ordinarias.
   - *Aprendizaje-Servicio (ApS):* Proyectos escolares que vinculan el currículo con una mejora tangible del entorno barrial (ejemplo: alumnado que enseña competencias digitales a personas mayores del barrio).

---

## 7. Actuación e intervención del educador o educadora social

De acuerdo con las **Instrucciones de 17 de septiembre de 2010**, el Educador Social despliega funciones vertebrales como nodo conector:
* **Mapeo de Redes Comunitarias (Ecomapa Escolar):** Diagnóstico visual de los recursos territoriales disponibles y de las conexiones débiles o rotas de las familias en riesgo.
* **Tejedor de Vínculos Puente:** Acompañamiento a menores vulnerables hacia recursos de ocio saludable, clubes deportivos y bibliotecas públicas para ampliar sus lazos débiles emancipadores.
* **Intervención Preventiva en Ciberviolencias:** Dinamización de talleres sobre huella digital, respeto en grupos de WhatsApp y prevención de la sextorsión.
* **Coordinación de Mesas Técnicas de Barrio:** Liderazgo técnico en la conexión semanal entre el centro educativo, los Servicios Sociales Comunitarios y las entidades locales.

---

## 8. Conclusión

Ninguna escuela puede tener éxito como un búnker aislado del mundo; su fuerza reside en la riqueza y solidez de la red humana que la sostiene.

El **Educador y la Educadora Social** encarna la inteligencia relacional de la escuela pública andaluza: une lo que la desigualdad separa, tiende lazos de confianza entre el aula y la calle, y hace de la Comunidad Educativa una red viva y solidaria donde nadie queda desamparado.

---

## 9. Anexo: Mapa conceptual y tabla sinóptica del Tema 36

| Eje Temático | Normativa / Doctrinas Clave | Conceptos e Implicación Práctica |
| :--- | :--- | :--- |
| **Concepto de Red Social**| Carlos Lozares • Manuel Castells | Nodos (actores), aristas (vínculos), densidad relacional y centralidad en la sociedad red. |
| **Teoría de Lazos** | Mark Granovetter | Lazos fuertes (seguridad afectiva primaria) vs. lazos débiles (oportunidades y movilidad social). |
| **Contexto Urbano y Rural**| Realidad territorial andaluza | Anomia urbana vs. capital social de cercanía rural; papel vertebrador de los CPR andaluces. |
| **La Escuela como Red** | LEA (art. 14) • Séneca / iPasen | Interconexión entre nodos internos (docentes, familias, alumnos) y externos (salud, SSCC). |
| **Higiene Digital** | Ley Orgánica 3/2018 de Protección Datos | Alfabetización mediática crítica frente al ciberacoso y dependencia a pantallas. |
| **Dinamización Comunit.**| ApS • Comunidades de Aprendizaje | Metodologías que vinculan el aprendizaje con el servicio solidario al territorio. |
| **Rol del Educador/a Social** | Instrucciones de 17 de septiembre de 2010 | Tejedor de redes, mapeo de recursos barriales, dinamizador de lazos débiles y coordinación local. |
"""

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 36 - Las Redes Sociales. Elementos. Contexto Urbano y Rural. La Comunidad Educativa como Red. Rol del Educador Social</title>
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
    <h1>TEMA 36</h1>
    <h2>Las redes sociales. Características y elementos de las redes sociales. Redes sociales en el contexto urbano y rural. La Comunidad Educativa como red social: Agentes, relaciones de comunicación y estrategias para la formación. Factores favorecedores</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> Ley 17/2007 (LEA, arts. 14-19); Decretos 327 y 328 de 2010; Ley Orgánica 3/2018 de Protección de Datos; Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Mark Granovetter (Lazos débiles), Manuel Castells (Sociedad red), Barry Wellman, Robert Putnam</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 36</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y fundamentación sociológica del concepto de red social</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">Características y elementos estructurales de las redes: Nodos, aristas y lazos</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">Las redes sociales en el contexto andaluz: Ecosistema urbano vs. ecosistema rural</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">La Comunidad Educativa entendida como red social integrada: Agentes y flujos</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">Estrategias socioeducativas para la formación y alfabetización en redes digitales</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">Factores que favorecen y dinamizan las relaciones en la Comunidad Educativa</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">Actuación e intervención del educador o educadora social como tejedor/a de redes</span></li>
      <li class="toc-item"><span class="toc-num">08</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 36</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y fundamentación sociológica del concepto de red social</h2>
  <p>
    El concepto de <strong>red social</strong> no nació con internet ni con las plataformas móviles; constituye una categoría sociológica fundamental formulada para explicar cómo los vínculos interpersonales generan apoyo mutuo, identidad colectiva y capital social (Robert Putnam, Carlos Lozares).
  </p>
  <p>
    En la **sociedad red contemporánea** (Manuel Castells), la Educación Social concibe al centro escolar no como un recinto aislado, sino como un **ecosistema dinámico de relaciones humanas e institucionales interdependientes**.
  </p>
  <p>
    El Educador y la Educadora Social ejerce de "tejedor de redes", fortaleciendo los lazos debilitados de las familias vulnerables y conectando el aula con el territorio.
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. Características y elementos estructurales de las redes: Nodos, aristas y lazos</h2>
  <p>
    El Análisis de Redes Sociales (ARS) delimita elementos canónicos:
  </p>
  <ul>
    <li><strong>Nodos:</strong> Actores individuales (estudiante, docente) o colectivos (AMPA, equipo directivo, centro de salud).</li>
    <li><strong>Aristas o Vínculos:</strong> Canales de comunicación, afecto o ayuda mutua.</li>
    <li><strong>Densidad y Centralidad:</strong> Nivel de cohesión global y posición estratégica de intermediación técnica.</li>
  </ul>

  <div class="callout">
    <div class="callout-title">La Tesis de Mark Granovetter (La Fuerza de los Lazos Débiles)</div>
    <p>
      • <strong>Lazos Fuertes:</strong> Familia y amigos íntimos; brindan apego y seguridad inmediata.<br>
      • <strong>Lazos Débiles:</strong> Conexiones externas esporádicas; son los que permiten romper el círculo de la exclusión, acceder a empleos y promover la movilidad social ascendente.
    </p>
  </div>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. Las redes sociales en el contexto andaluz: Ecosistema urbano vs. ecosistema rural</h2>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">CONTEXTO URBANO</h4>
      <p>
        • Abundancia de servicios especializados (hospitales, USMIJ, centros cívicos).<br>
        • Riesgo de anomia, soledad no deseada, individualismo y fragmentación en barrios desfavorecidos.
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">CONTEXTO RURAL</h4>
      <p>
        • Lazos comunitarios y vecinales muy sólidos, solidaridad espontánea y cercanía.<br>
        • Riesgo de aislamiento geográfico.<br>
        • <em>Colegios Públicos Rurales (CPR):</em> Corazón social que vertebra y fija la población al territorio.
      </p>
    </div>
  </div>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. La Comunidad Educativa entendida como red social integrada: Agentes y flujos</h2>
  <p>
    El centro docente es el nodo central de una red multinivel:
  </p>
  <ul>
    <li><strong>Nodos Internos:</strong> Alumnado, claustro docente, familias y personal no docente.</li>
    <li><strong>Nodos Comunitarios:</strong> Servicios Sociales Comunitarios (SSCC), Salud Primaria, Policía Local (Agente Tutor), asociaciones gitanas y clubes deportivos.</li>
    <li><strong>Canales de Comunicación:</strong> Vías telemáticas corporativas (<em>Séneca</em> e <em>iPasen</em>) combinadas con el calor insustituible de la tutoría presencial y la mediación cara a cara.</li>
  </ul>

  <!-- SECCIÓN 5 -->
  <div class="page-break"></div>
  <h2 class="section-title">5. Estrategias socioeducativas para la formación y alfabetización en redes digitales</h2>
  <ul>
    <li><strong>Competencia Digital Crítica para Menores:</strong> Desmitificación de la tiranía del «like», prevención del ciberacoso escolar y concienciación sobre la huella digital.</li>
    <li><strong>Escuelas de Familias sobre Higiene Digital:</strong> Asesoramiento para regular el tiempo de uso, evitar pantallas nocturnas y supervisar el acceso a contenidos violentos o adictivos.</li>
  </ul>

  <!-- SECCIÓN 6 -->
  <h2 class="section-title">6. Factores que favorecen y dinamizan las relaciones en la Comunidad Educativa</h2>
  <p>
    Condiciones para consolidar una red escolar protectora:
  </p>
  <div class="callout">
    <div class="callout-title">Factores Facilitadores de la Red Escolar</div>
    <p>
      • <strong>Confianza y Transparencia:</strong> Trato cercano y desprovisto de condescendencia hacia las familias.<br>
      • <strong>Metodologías Comunitarias:</strong> Aprendizaje-Servicio (ApS) que vincula las materias con mejoras en el barrio, y Comunidades de Aprendizaje con voluntariado vecinal en el aula.
    </p>
  </div>

  <!-- SECCIÓN 7 -->
  <div class="page-break"></div>
  <h2 class="section-title">7. Actuación e intervención del educador o educadora social como tejedor/a de redes</h2>
  <p>
    Conforme a las <strong>Instrucciones de 17 de septiembre de 2010</strong>, el Educador Social despliega funciones vertebrales:
  </p>
  <ul>
    <li><strong>Mapeo de Recursos y Ecomapas Familiares:</strong> Diagnóstico de las carencias relacionales de los estudiantes más vulnerables.</li>
    <li><strong>Dinamización de Lazos Débiles:</strong> Conexión del alumnado en riesgo con entidades culturales, deportivas y bibliotecas para ampliar sus expectativas de futuro.</li>
    <li><strong>Prevención de Ciberodio en Redes:</strong> Talleres de sensibilización sobre respeto e igualdad en grupos de mensajería instantánea.</li>
    <li><strong>Liderazgo en Mesas Técnicas Locales:</strong> Articulación semanal de la red entre centro educativo, Servicios Sociales y ayuntamiento.</li>
  </ul>

  <!-- SECCIÓN 8 -->
  <h2 class="section-title">8. Conclusión</h2>
  <p>
    Ningún centro escolar puede prosperar como una fortaleza cerrada; su verdadera fuerza reside en la densidad y calidad de las relaciones que es capaz de tejer con su comunidad.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> es el mediador de la conectividad humana: conecta a los desconectados, rompe el aislamiento del dolor y convierte a la escuela pública andaluza en un refugio comunitario donde nadie queda a la deriva.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 36</h2>
  <p>Resumen estructurado de redes sociales, Granovetter, contexto territorial y rol dinamizador:</p>

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
        <td><strong>Concepto de Red</strong></td>
        <td>Carlos Lozares • Manuel Castells</td>
        <td>Nodos, vínculos, densidad relacional y centralidad en la sociedad red contemporánea.</td>
      </tr>
      <tr>
        <td><strong>Lazos Fuertes y Débiles</strong></td>
        <td>Mark Granovetter</td>
        <td>Lazos fuertes (seguridad afectiva primaria) frente a lazos débiles (movilidad social y oportunidades).</td>
      </tr>
      <tr>
        <td><strong>Urbano vs. Rural</strong></td>
        <td>Realidad territorial andaluza</td>
        <td>Anomia urbana vs. solidaridad comunitaria rural; papel vertebrador de los CPR andaluces.</td>
      </tr>
      <tr>
        <td><strong>Comunidad Educativa</strong></td>
        <td>LEA (art. 14) • Séneca / iPasen</td>
        <td>Red integrada de nodos internos (claustro, familias, alumnado) y nodos externos (salud, SSCC).</td>
      </tr>
      <tr>
        <td><strong>Higiene Digital</strong></td>
        <td>Ley Orgánica 3/2018 de Protección Datos</td>
        <td>Alfabetización mediática crítica frente al ciberacoso y tiranía de la validación virtual.</td>
      </tr>
      <tr>
        <td><strong>Proyectos Comunitarios</strong></td>
        <td>Aprendizaje-Servicio (ApS) • CdA</td>
        <td>Metodologías pedagógicas que conectan los aprendizajes del aula con las necesidades del barrio.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Tejedor de redes, diagnóstico mediante ecomapas, dinamizador de lazos débiles y coordinación local.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

md_path = "andalucia/Tema_36_Redes_Sociales_Contexto_Urbano_Rural_Comunidad_Educativa.md"
html_path = "andalucia/Tema_36_Redes_Sociales_Contexto_Urbano_Rural_Comunidad_Educativa.html"
pdf_path = "andalucia/Tema_36_Redes_Sociales_Contexto_Urbano_Rural_Comunidad_Educativa.pdf"

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")
compile_pdf(html_path, pdf_path)
