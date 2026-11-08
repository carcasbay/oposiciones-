import os
from build_theme import compile_pdf

md_content = """# TEMA 22: El Maltrato Infantil y Juvenil. Definición y Tipos de Maltrato en la Infancia y en la Adolescencia. Detección del Maltrato en el Ámbito Educativo. Acción Socioeducativa en Situaciones de Maltrato Infantil y Juvenil desde el Centro Educativo. Normativa, Planes y Protocolos Específicos de Acción Socioeducativa. Planes Integrales y Coordinación Institucional. El Papel del Educador o Educadora Social con Alumnado y Familias

---

## FICHA TÉCNICA DEL TEMA
* **Cuerpo:** Cuerpo Técnico Facultativo de la Junta de Andalucía
* **Especialidad:** Educación Social (A2.2018)
* **Carácter:** Materias Específicas del Programa Oficial
* **Marco Legal y Documental:**
  - Convención sobre los Derechos del Niño (ONU, 1989, arts. 19 y 34).
  - Ley Orgánica 1/1996, de Protección Jurídica del Menor, modificada por la Ley 26/2015.
  - Ley Orgánica 8/2021, de 4 de junio, de Protección Integral a la Infancia y la Adolescencia frente a la Violencia (LOPIVI).
  - Ley 4/2021, de 27 de julio, de Infancia y Adolescencia de Andalucía.
  - Orden de 20 de junio de 2011 (Protocolo de actuación sobre maltrato infantil en el ámbito educativo en Andalucía).
  - Hoja de Notificación del Maltrato Infantil y Sistema de Información SIMIA de la Junta de Andalucía.
  - Instrucciones de 17 de septiembre de 2010 de la Dirección General de Participación e Innovación Educativa.
* **Autores y Doctrinas de Referencia:** Jorge Barudy y Maryorie Dantagnan (Los buenos tratos a la infancia y parentalidad positiva), Félix López Sánchez (Prevención de abusos sexuales y necesidades infantiles), Boris Cyrulnik (Resiliencia y trauma infantil), FICE (Federación Internacional de Comunidades Educativas).

---

## ÍNDICE DE CONTENIDOS
1. Introducción y contextualización del maltrato infantojuvenil en la Educación Social.
2. Definición, modelos explicativos y tipología del maltrato en la infancia y adolescencia:
   - 2.1. Maltrato físico.
   - 2.2. Maltrato emocional y psicológico.
   - 2.3. Negligencia o abandono (físico, higiénico, afectivo y formativo).
   - 2.4. Abuso y explotación sexual infantil (ASI).
   - 2.5. Violencia vicaria y exposición a la violencia de género.
   - 2.6. Violencia digital: Ciberacoso, grooming y sextorsión.
3. Detección del maltrato en el centro educativo: Indicadores físicos, conductuales y relacionales.
4. Marco normativo y protocolos de protección a la infancia:
   - 4.1. La Ley Orgánica 8/2021 (LOPIVI) y la figura del Coordinador/a de Bienestar y Protección.
   - 4.2. La Ley 4/2021 de Infancia y Adolescencia de Andalucía.
   - 4.3. El Sistema de Información sobre Maltrato Infantil de Andalucía (SIMIA).
5. Acción socioeducativa y protocolo de actuación en el centro escolar:
   - 5.1. Detección y valoración inicial por el equipo docente.
   - 5.2. Cumplimentación y remisión de la Hoja de Notificación SIMIA.
   - 5.3. Medidas inmediatas de protección y salvaguarda de urgencia.
6. Coordinación interinstitucional y planes integrales:
   - 6.1. Servicios de Protección de Menores y Equipos de Tratamiento Familiar (ETF).
   - 6.2. Coordinación sanitaria, policial y judicial (Fiscalía de Menores).
7. Papel del educador o educadora social con el alumnado y las familias:
   - 7.1. Acompañamiento socioemocional y no revictimización.
   - 7.2. Fomento de la parentalidad positiva en escuelas de familias.
8. Conclusión.
9. Anexo: Mapa conceptual y tabla sinóptica del Tema 22.

---

## 1. Introducción y contextualización del maltrato infantojuvenil en la Educación Social

El maltrato a la infancia y adolescencia constituye una de las **violaciones más destructivas de los derechos humanos**, cuyas secuelas traumáticas alteran el desarrollo neurológico, psicoafectivo y social del ser humano a lo largo de toda su vida (Boris Cyrulnik). Los menores de edad, por su condición de vulnerabilidad intrínseca y dependencia evolutiva, precisan de un entorno de apego seguro y de cuidados incondicionales para estructurar su personalidad (Jorge Barudy).

La escuela es la institución universal por excelencia donde las infancias conviven a diario. Por ello, el centro docente se erige en el **espacio privilegiado de detección precoz y escudo de protección de menores frente a la violencia intrafamiliar o comunitaria**. El profesorado y el personal socioeducativo se encuentran en una posición idónea para observar cambios bruscos de conducta, lesiones inexplicables o indicadores de desatención grave.

Para la **Educación Social**, el abordaje del maltrato infantil combina el **rigor protector y la denuncia obligatoria de situaciones delictivas** con una profunda **intervención reparadora y socioeducativa**: construir espacios seguros de resiliencia, evitar la revictimización del menor, orientar a las familias en pautas de parentalidad positiva y coordinar la respuesta con la red de servicios sociales y judiciales andaluces.

---

## 2. Definición, modelos explicativos y tipología del maltrato

El maltrato infantil abarca toda acción, omisión o trato negligente, no accidental, que prive al menor de sus derechos y su bienestar, o que amenace su desarrollo físico, psíquico o social, perpetrado por sus progenitores, tutores o cualquier persona adulta (Consejo de Europa y LOPIVI).

```
                        TIPOLOGÍA DE MALTRATO INFANTIL
 ┌──────────────────────┬──────────────────────┬──────────────────────┐
 │ MALTRATO FÍSICO      │ MALTRATO EMOCIONAL   │ NEGLIGENCIA / ABANDONO│
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ • Golpes, castigo    │ • Humillaciones públ.│ • Falta de alimento/ │
 │   corporal, quemad.  │ • Insultos crónicos  │   higiene continuada │
 │ • Síndrome del niño  │ • Amenazas y rechazo │ • Desatención médica │
 │   zarandeado         │ • Aislamiento social │ • No escolarización  │
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ ABUSO SEXUAL (ASI)   │ VIOLENCIA VICARIA    │ VIOLENCIA DIGITAL    │
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ • Tocamientos, porno │ • Violencia machista │ • Ciberbullying      │
 │ • Coacción sexual    │   presenciada por el │ • Grooming y chantaje│
 │ • Corrupción menores │   menor para dañar   │ • Sextorsión y fotos │
 └──────────────────────┴──────────────────────┴──────────────────────┘
```

### 2.1. Maltrato Físico
Uso deliberado de la fuerza física contra el menor que le provoca daño corporal evidente (hematomas, quemaduras, fracturas, laceraciones) o riesgo inminente de padecerlo.

### 2.2. Maltrato Emocional y Psicológico
Pauta persistente de hostilidad, desprecio, rechazo sistemático, amenazas o aislamiento forzado que destruye el autoconcepto y la seguridad afectiva del menor.

### 2.3. Negligencia o Abandono
Forma más frecuente pero más invisible de maltrato. Falta de respuesta a las necesidades primarias del niño: alimentación inadecuada, vestimenta andrajosa, falta continuada de higiene corporal, abandono de tratamientos médicos prescritos o desatención de la escolaridad obligatoria.

### 2.4. Abuso y Explotación Sexual Infantil (ASI)
Involucración de un menor de edad en actividades sexuales (con o sin contacto físico, pornografía, exhibicionismo) que no comprende plenamente, para las que no puede prestar consentimiento válido o que infringen las leyes.

### 2.5. Violencia Vicaria y Violencia de Género
La Ley Orgánica 8/2021 (LOPIVI) reconoce expresamente que los niños y niñas que viven en hogares donde se ejerce violencia de género contra sus madres son **víctimas directas de maltrato infantil**, sufriendo gravísimas repercusiones emocionales.

### 2.6. Violencia en el Entorno Digital
Nuevas modalidades potenciadas por las TIC: *grooming* (engaño pederasta por internet), *ciberbullying* reiterado, difusión de imágenes íntimas sin consentimiento (*sexting* no consentido) y chantaje sexual digital (*sextorsión*).

---

## 3. Detección del maltrato en el centro educativo: Indicadores clave

La detección temprana exige identificar indicadores cruzados en el menor y en sus cuidadores:

### 3.1. Indicadores Físicos
* Lesiones o hematomas inexplicables en zonas poco expuestas a caídas habituales (espalda, muslos, mejillas, cuello).
* Marcas con formas de objetos concretos (hebillas de cinturón, quemaduras circulares de cigarrillo).
* Desnutrición visible, cansancio extremo, sueño continuo en el aula por falta de descanso.
* Infecciones genitales recurrentes o dolores inexplicables al sentarse o caminar (alerta de abuso sexual).

### 3.2. Indicadores Conductuales y Afectivos
* **Hipervigilancia y Sobresalto:** Miedo extremo al contacto físico o a los movimientos repentinos del adulto.
* **Temor Angustioso a Volver a Casa:** Reticencia a abandonar el centro docente al finalizar la jornada escolar.
* **Retraimiento Repentino o Depresión:** Aislamiento súbito de los amigos, mutismo selectivo o llanto inmotivado.
* **Sexualización Precoz en Juegos y Dibujos:** Conocimiento explícito de conductas sexuales impropias de la etapa evolutiva.
* **Agresividad Desmedida:** Descarga de violencia contra iguales como reproducción del patrón violento vivido en el hogar.

---

## 4. Marco normativo y protocolos de protección a la infancia

### 4.1. La Ley Orgánica 8/2021 (LOPIVI)
Hito legislativo estatal que establece un marco integral frente a la violencia sobre menores:
* **Deber de Denuncia Obligatorio (art. 15 y 16):** Cualquier persona, y en particular los profesionales del ámbito educativo, sanitario o social, tiene la obligación legal de denunciar de inmediato cualquier indicio de violencia contra un menor ante la autoridad policial o judicial.
* **Figura del Coordinador/a de Bienestar y Protección:** Figura obligatoria en todos los centros educativos para garantizar entornos escolares seguros, coordinar la aplicación de protocolos y canalizar las notificaciones.

### 4.2. Ley 4/2021 de Infancia y Adolescencia de Andalucía
Consagra el principio del **Interés Superior del Menor**, el derecho a ser escuchado en todos los procesos que le afecten y el fortalecimiento de la prevención de situaciones de riesgo y desamparo.

### 4.3. El Sistema de Información sobre Maltrato Infantil de Andalucía (SIMIA)
Instrumento oficial técnico y digital de la Junta de Andalucía para la recogida homogénea de datos y notificación inmediata de situaciones de maltrato detectadas desde la educación, la salud, la policía y los servicios sociales.

---

## 5. Acción socioeducativa y protocolo de actuación en el centro escolar

El protocolo andaluz regulado por la **Orden de 20 de junio de 2011** establece una secuencia clara:

```
                  PROTOCOLO DE ACTUACIÓN ANTE MALTRATO INFANTIL
 ┌──────────────────────┬──────────────────────┬──────────────────────┐
 │ FASE 1: DETECCIÓN    │ FASE 2: VALORACIÓN   │ FASE 3: NOTIFICACIÓN │
 ├──────────────────────┼──────────────────────┼──────────────────────┤
 │ • Observación de     │ • Equipo Directivo,  │ • Cumplimentación de │
 │   indicadores físicos│   Orientador/a y     │   la Hoja SIMIA.     │
 │   o emocionales.     │   Educador/a Social. │ • Remisión a los     │
 │ • Escucha empática   │ • Recogida objetiva  │   Servicios Sociales │
 │   sin interrogar al  │   de datos sin       │   o Fiscalía si hay  │
 │   menor.             │   prejuzgar.         │   delito inminente.  │
 └──────────────────────┴──────────────────────┴──────────────────────┘
```

1. **Detección y Escucha Activa:** Si el menor confiesa un maltrato, se le escucha con afecto y credibilidad, sin presionarlo con interrogatorios invasivos para no revictimizarlo ni contaminar su relato.
2. **Reunión Técnica Interna:** Equipo Directivo, Orientador/a escolar, Coordinador/a de Bienestar y Educador/a Social analizan la información con estricta confidencialidad.
3. **Notificación en SIMIA:** La Dirección del centro cumplimenta la **Hoja de Notificación SIMIA** y la remite telemáticamente a la Delegación Territorial de Inclusión Social y a los Servicios Sociales Municipales.
4. **Actuación de Urgencia:** Si el menor presenta lesiones físicas graves o abuso sexual flagrante, se contacta de inmediato con los servicios médicos de urgencia (061), la Policía Nacional / Guardia Civil y el Juzgado de Guardia / Fiscalía de Menores.

---

## 6. Coordinación interinstitucional y planes integrales

La protección efectiva del menor maltratado exige la acción coordinada de una red multiagencial:
* **Servicio de Protección de Menores de la Junta de Andalucía:** Órgano competente para declarar la situación de **desamparo** y asumir la tutela legal del menor en caso de desprotección grave, adoptando medidas de acogimiento familiar prioritario o residencial.
* **Servicios Sociales Comunitarios y Equipos de Tratamiento Familiar (ETF):** Intervención intensiva de apoyo y capacitación parental con la familia biológica para corregir dinámicas de maltrato leve o moderado antes de requerir la separación del menor.
* **Fiscalía de Menores y Juzgados:** Supervisión jurídica de la legalidad de las medidas y persecución penal de los agresores.

---

## 7. Papel del educador o educadora social con el alumnado y las familias

En virtud de las **Instrucciones de 17 de septiembre de 2010**, el Educador/a Social despliega una labor imprescindible:
1. **Espacio Escolar Seguro y Acompañamiento Socioemocional:** El educador actúa como referente afectivo estable (*tutor de resiliencia* - Cyrulnik) que brinda al menor un refugio de calma, confianza y validación emocional.
2. **Asesoramiento Técnico en la Cumplimentación de SIMIA:** Redacción objetiva y rigurosa de los indicadores sociales y familiares para fundamentar la notificación oficial.
3. **Coordinación con el Coordinador de Bienestar y el ETF:** Seguimiento compartido del caso para evitar duplicidades y garantizar la continuidad formativa del menor si cambia de domicilio o centro.
4. **Escuelas de Familias sobre Parentalidad Positiva (Jorge Barudy):** Talleres preventivos comunitarios dirigidos a padres y madres sobre estilos de crianza no violentos, gestión de rabietas, límites con afecto y erradicación del castigo físico.

---

## 8. Conclusión

Ningún dolor es más injusto ni deja cicatrices más hondas que la violencia padecida por un niño a manos de quienes tenían la obligación sagrada de protegerlo y amarlo. La indiferencia o el silencio institucional convierten al sistema en cómplice del agresor.

El **Educador y la Educadora Social** encarna la mirada protectora, ética y valiente de la escuela pública andaluza: detecta el sufrimiento oculto tras el silencio infantil, activa con firmeza los mecanismos de salvaguarda legal y devuelve a cada menor la esperanza y el derecho a crecer en paz, dignidad y amor.

---

## 9. Anexo: Mapa conceptual y tabla sinóptica del Tema 22

| Eje Temático | Normativa / Doctrinas Clave | Conceptos e Implicación Práctica |
| :--- | :--- | :--- |
| **Concepto de Maltrato** | CDN (arts. 19 y 34) • LOPIVI 8/2021 | Toda acción, omisión o trato negligente que vulnera la integridad física, psicológica o sexual del menor. |
| **Buenos Tratos y Apego** | Jorge Barudy • Maryorie Dantagnan | Parentalidad positiva, apego seguro y resiliencia frente a pautas de castigo corporal o desprecio. |
| **Tipología de Violencias** | LOPIVI • Ley 4/2021 de Andalucía | Físico, emocional, negligencia (la más frecuente), abuso sexual (ASI), violencia vicaria y ciberacoso/grooming. |
| **Indicadores Escolares** | Indicadores físicos y conductuales | Lesiones inexplicables, hipervigilancia, miedo a volver a casa, sexualización precoz y cambios bruscos. |
| **Protocolo y Sistema SIMIA** | Orden 20 de junio de 2011 • SIMIA | Notificación oficial obligatoria telemática de la situación de riesgo ante Servicios Sociales. |
| **Coordinador de Bienestar** | LOPIVI (arts. 34-35) | Nueva figura escolar obligatoria encargada de los protocolos de protección y entornos seguros. |
| **Rol del Educador/a Social** | Instrucciones de 17 de septiembre de 2010 | Tutor de resiliencia, redacción técnica de SIMIA, escuelas de parentalidad positiva y coordinación con ETF. |
"""

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tema 22 - Maltrato Infantil y Juvenil. Detección Escolar. Protocolos y Sistema SIMIA. LOPIVI. Rol del Educador Social</title>
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
    <h1>TEMA 22</h1>
    <h2>El maltrato infantil y juvenil. Definición y tipos de maltrato en la infancia y en la adolescencia. Detección del maltrato en el ámbito educativo. Acción socioeducativa desde el centro educativo. Normativa, planes y protocolos específicos. Planes integrales y coordinación institucional. El papel del educador o educadora social</h2>
    
    <div class="meta-box">
      <p><strong>Cuerpo:</strong> Técnico Facultativo • Especialidad Educación Social (A2.2018)</p>
      <p><strong>Ámbito:</strong> Materias Específicas del Programa Oficial</p>
      <p><strong>Marco Normativo:</strong> Convención Derechos Niño; LOPIVI 8/2021; Ley 4/2021 de Infancia de Andalucía; Orden 20 de junio de 2011; Sistema de Información SIMIA; Instrucciones 17 de septiembre de 2010</p>
      <p><strong>Referentes:</strong> Jorge Barudy (Buenos tratos a la infancia), Boris Cyrulnik (Resiliencia), Félix López Sánchez</p>
    </div>
  </div>

  <!-- ÍNDICE DE CONTENIDOS -->
  <div class="toc-container">
    <div class="toc-title">Índice del Tema 22</div>
    <ul class="toc-list">
      <li class="toc-item"><span class="toc-num">01</span><span class="toc-text">Introducción y contextualización del maltrato infantil en la Educación Social</span></li>
      <li class="toc-item"><span class="toc-num">02</span><span class="toc-text">Definición, modelos explicativos y tipología del maltrato infantojuvenil</span></li>
      <li class="toc-item"><span class="toc-num">03</span><span class="toc-text">Detección del maltrato en el centro educativo: Indicadores físicos y conductuales</span></li>
      <li class="toc-item"><span class="toc-num">04</span><span class="toc-text">Marco normativo y protocolos de protección a la infancia: LOPIVI y SIMIA</span></li>
      <li class="toc-item"><span class="toc-num">05</span><span class="toc-text">Acción socioeducativa y protocolo de actuación en el centro escolar</span></li>
      <li class="toc-item"><span class="toc-num">06</span><span class="toc-text">Coordinación interinstitucional: Servicios de Protección, ETF y Fiscalía</span></li>
      <li class="toc-item"><span class="toc-num">07</span><span class="toc-text">Papel del educador o educadora social con el alumnado y las familias</span></li>
      <li class="toc-item"><span class="toc-num">08</span><span class="toc-text">Conclusión</span></li>
      <li class="toc-item"><span class="toc-num">★</span><span class="toc-text">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 22</span></li>
    </ul>
  </div>

  <!-- SECCIÓN 1 -->
  <h2 class="section-title">1. Introducción y contextualización del maltrato infantil en la Educación Social</h2>
  <p>
    El maltrato a la infancia y adolescencia constituye una de las <strong>vulneraciones más destructivas de los derechos humanos</strong>. Por su condición de vulnerabilidad física y dependencia evolutiva, los menores necesitan un entorno de apego seguro y de cuidados incondicionales para estructurar sanamente su cerebro y su afectividad (Jorge Barudy). El daño infligido en los primeros años de vida genera traumas relacionales severos que impactan directamente en el aprendizaje, la socialización y la salud mental (Boris Cyrulnik).
  </p>
  <p>
    La escuela es el entorno privilegiado para la <strong>detección precoz del maltrato y la activación del escudo protector de la infancia</strong>: es el único espacio donde los menores acuden diariamente fuera del control de su núcleo familiar agresor o negligente.
  </p>
  <p>
    Para la <strong>Educación Social</strong>, la respuesta frente al maltrato infantil combina el cumplimiento estricto del deber de notificación con una labor pedagógica reparadora: ofrecer un refugio afectivo seguro, prevenir la revictimización y capacitar a las familias en pautas de parentalidad positiva.
  </p>

  <!-- SECCIÓN 2 -->
  <h2 class="section-title">2. Definición, modelos explicativos y tipología del maltrato infantojuvenil</h2>
  <p>
    El maltrato abarca toda acción, omisión o trato negligente que vulnere la integridad, el desarrollo físico o socioafectivo del menor. Se clasifica en:
  </p>
  <div class="compare-container">
    <div class="compare-box compare-purple">
      <h4 style="color: #6d28d9;">MALTRATO FÍSICO Y EMOCIONAL</h4>
      <p>
        • <em>Físico:</em> Golpes, quemaduras deliberadas o síndrome del niño zarandeado.<br>
        • <em>Emocional:</em> Humillaciones, insultos crónicos, rechazo sistemático y amenazas que destruyen el autoconcepto del menor.
      </p>
    </div>
    <div class="compare-box compare-rose">
      <h4 style="color: #be123c;">NEGLIGENCIA, ABUSO Y VIOLENCIA DIGITAL</h4>
      <p>
        • <em>Negligencia:</em> Desatención continuada en alimentación, higiene o salud.<br>
        • <em>Abuso Sexual (ASI):</em> Cualquier conducta sexual impuesta.<br>
        • <em>Violencia Digital:</em> Grooming, sextorsión y ciberacoso organizado.
      </p>
    </div>
  </div>

  <!-- SECCIÓN 3 -->
  <div class="page-break"></div>
  <h2 class="section-title">3. Detección del maltrato en el centro educativo: Indicadores clave</h2>

  <h3 class="sub-title">3.1. Indicadores Físicos</h3>
  <ul>
    <li>Lesiones o hematomas en zonas poco expuestas a caídas accidentales (espalda, muslos, mejillas o glúteos).</li>
    <li>Marcas con forma geométrica de objetos (hebillas, cables, quemaduras circulares de cigarrillos).</li>
    <li>Falta extrema de higiene corporal continuada, malnutrición visible y ropa andrajosa o inadecuada para la climatología.</li>
    <li>Dolores genitales o infecciones recurrentes sin explicación médica.</li>
  </ul>

  <h3 class="sub-title">3.2. Indicadores Conductuales y Emocionales</h3>
  <ul>
    <li><strong>Hipervigilancia defensiva:</strong> Temor extremo a los movimientos repentinos del adulto o al contacto físico.</li>
    <li><strong>Angustia por volver al hogar:</strong> Resistencia a abandonar el centro docente al acabar la jornada.</li>
    <li><strong>Sexualización precoz inapropiada:</strong> Lenguaje, dibujos o juegos con contenido sexual explícito para su edad.</li>
    <li><strong>Retraimiento súbito o agresividad extrema:</strong> Descarga de frustración contra compañeros o mutismo selectivo.</li>
  </ul>

  <!-- SECCIÓN 4 -->
  <h2 class="section-title">4. Marco normativo y protocolos de protección a la infancia</h2>
  <div class="callout">
    <div class="callout-title">Legislación Protectora y Obligaciones Legales</div>
    <p>
      • <strong>Ley Orgánica 8/2021 (LOPIVI):</strong> Establece el deber legal de denuncia inmediata de cualquier sospecha (arts. 15-16) y crea la figura del <strong>Coordinador/a de Bienestar y Protección</strong> en todos los centros docentes.<br>
      • <strong>Ley 4/2021 de Infancia de Andalucía:</strong> Interés superior del menor y prioridad al acogimiento familiar frente al residencial.<br>
      • <strong>Orden de 20 de junio de 2011 y Sistema SIMIA:</strong> Protocolo oficial andaluz y plataforma informática para la cumplimentación de la Hoja de Notificación de Maltrato Infantil.
    </p>
  </div>

  <!-- SECCIÓN 5 -->
  <div class="page-break"></div>
  <h2 class="section-title">5. Acción socioeducativa y protocolo de actuación en el centro escolar</h2>
  <ol>
    <li><strong>Detección y Escucha Activa:</strong> Si el menor verbaliza la agresión, se le acoge con afecto y credibilidad absoluta, evitando interrogarlo para no contaminar el testimonio ni revictimizarlo.</li>
    <li><strong>Reunión Técnica de Urgencia:</strong> Equipo Directivo, Orientador/a escolar, Coordinador de Bienestar y Educador/a Social analizan objetivamente las evidencias.</li>
    <li><strong>Notificación en el Sistema SIMIA:</strong> Cumplimentación oficial de la Hoja SIMIA y remisión inmediata telemática a la Delegación Territorial y Servicios Sociales.</li>
    <li><strong>Derivación Urgente en Delito Flagrante:</strong> Si hay riesgo vital inminente o lesiones graves, se avisa inmediatamente al 061 (urgencias sanitarias), Policía y Fiscalía de Menores.</li>
  </ol>

  <!-- SECCIÓN 6 -->
  <h2 class="section-title">6. Coordinación interinstitucional: Servicios de Protección, ETF y Fiscalía</h2>
  <ul>
    <li><strong>Servicio de Protección de Menores de la Junta de Andalucía:</strong> Competente para decretar el <strong>desamparo</strong> y la tutela pública de menores en desprotección grave, priorizando el acogimiento familiar.</li>
    <li><strong>Equipos de Tratamiento Familiar (ETF) de los Servicios Sociales:</strong> Intervención psicoterapéutica y socioeducativa intensiva con familias en riesgo moderado para evitar la retirada de los menores.</li>
    <li><strong>Fiscalía de Menores y Juzgados:</strong> Tutela de los derechos procesales del menor y adopción de órdenes de alejamiento frente al agresor.</li>
  </ul>

  <!-- SECCIÓN 7 -->
  <div class="page-break"></div>
  <h2 class="section-title">7. Papel del educador o educadora social con el alumnado y las familias</h2>
  <p>
    De acuerdo con las <strong>Instrucciones de 17 de septiembre de 2010</strong>, el Educador Social ejerce funciones especializadas:
  </p>
  <ul>
    <li><strong>Tutor de Resiliencia (Boris Cyrulnik):</strong> Proveer al menor maltratado de un vínculo afectivo seguro, estable y reparador en el centro educativo.</li>
    <li><strong>Redacción Técnica de la Notificación SIMIA:</strong> Descripción exhaustiva, neutra y objetiva de los hechos observables y factores de riesgo sociofamiliar.</li>
    <li><strong>Coordinación Continua con el ETF:</strong> Seguimiento semanal del plan de intervención sociofamiliar para evaluar avances o recaídas en el hogar.</li>
    <li><strong>Escuelas de Familias sobre Parentalidad Positiva:</strong> Talleres de resolución pacífica de conflictos, límites sin castigo físico y fomento del apego seguro (Jorge Barudy).</li>
  </ul>

  <!-- SECCIÓN 8 -->
  <h2 class="section-title">8. Conclusión</h2>
  <p>
    El silencio ante el maltrato infantil es la peor forma de complicidad. La escuela pública debe ser para todo niño y niña el lugar más seguro del mundo: una fortaleza donde la violencia no tiene cabida y donde su voz es siempre escuchada y creída.
  </p>
  <p>
    El <strong>Educador y la Educadora Social</strong> es el guardián de la dignidad de las infancias más quebradas: rescata el dolor invisible, activa el amparo de la ley y acompaña la sanación de las heridas con la fuerza transformadora de la pedagogía y el amor incondicional.
  </p>

  <!-- ANEXO TABLA -->
  <div class="page-break"></div>
  <h2 class="section-title">Anexo: Mapa Conceptual y Tabla Sinóptica del Tema 22</h2>
  <p>Resumen estructurado de tipologías de maltrato, indicadores, marco legislativo y praxis socioeducativa:</p>

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
        <td><strong>Concepto de Maltrato</strong></td>
        <td>CDN • LOPIVI 8/2021<br>Jorge Barudy (Buenos Tratos)</td>
        <td>Vulneración de la integridad del menor. Apego seguro y parentalidad positiva frente a la violencia.</td>
      </tr>
      <tr>
        <td><strong>Tipología</strong></td>
        <td>Física • Emocional • Negligencia • Abuso</td>
        <td>Negligencia (la más frecuente e invisible), abuso sexual (ASI), violencia vicaria y ciberacoso/grooming.</td>
      </tr>
      <tr>
        <td><strong>Indicadores Escolares</strong></td>
        <td>Físicos y Conductuales</td>
        <td>Lesiones geométricas en zonas cubiertas, hipervigilancia, fobia a volver a casa y sexualización precoz.</td>
      </tr>
      <tr>
        <td><strong>Marco Protector LOPIVI</strong></td>
        <td>LOPIVI (Ley Orgánica 8/2021)</td>
        <td>Deber obligatorio de denuncia y creación del Coordinador/a de Bienestar y Protección escolar.</td>
      </tr>
      <tr>
        <td><strong>Protocolo Andaluz SIMIA</strong></td>
        <td>Orden 20 de junio de 2011 • SIMIA</td>
        <td>Plataforma digital unificada de la Junta de Andalucía para notificación obligatoria inmediata.</td>
      </tr>
      <tr>
        <td><strong>Coordinación en Red</strong></td>
        <td>Protección Menores • ETF • Fiscalía</td>
        <td>Declaración de desamparo, acogimiento familiar prioritario e intervención sociofamiliar con ETF.</td>
      </tr>
      <tr>
        <td><strong>Rol del Educador/a Social</strong></td>
        <td>Instrucciones de 17 de septiembre de 2010</td>
        <td>Tutor de resiliencia, rigor en SIMIA, escuelas de parentalidad positiva y coordinación comunitaria.</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

md_path = "andalucia/Tema_22_Maltrato_Infantil_Juvenil_Protocolos_SIMIA.md"
html_path = "andalucia/Tema_22_Maltrato_Infantil_Juvenil_Protocolos_SIMIA.html"
pdf_path = "andalucia/Tema_22_Maltrato_Infantil_Juvenil_Protocolos_SIMIA.pdf"

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written: {md_path} and {html_path}")
compile_pdf(html_path, pdf_path)
