import os

tests = {}

# ==========================================
# TEMA 9
# ==========================================
tests[9] = """# TEMA 9 — El desarrollo en la niñez intermedia (6 a 12 años). Socialización escolar y acompañamiento socioeducativo

1. En la teoría del desarrollo cognitivo de Jean Piaget, la etapa que coincide cronológicamente con la niñez intermedia (de 6 a 12 años) es:
a) El periodo sensoriomotor.
b) El periodo preoperacional.
c) El periodo de las operaciones concretas.
d) El periodo de las operaciones formales.

2. La adquisición fundamental del periodo de las operaciones concretas es:
a) La formulación de hipótesis científicas puramente abstractas sin soporte empírico.
b) La reversibilidad del pensamiento (por inversión y compensación) y la superación de las tareas de conservación (materia, peso y volumen).
c) El egocentrismo infantil radical y la incapacidad de descentración.
d) El pensamiento animista y mágico exclusivo.

3. Según la teoría psicosocial de Erik Erikson, la crisis vital característica de los niños entre 6 y 12 años es:
a) Confianza básica frente a desconfianza.
b) Autonomía frente a vergüenza.
c) Laboriosidad (o laboriosidad competente) frente a inferioridad.
d) Intimidad frente a aislamiento.

4. En el desarrollo psicosocial de la niñez intermedia, el "grupo de iguales" (peer group):
a) Deja de tener relevancia social frente al apego exclusivo a los padres.
b) Se convierte en un escenario clave para el aprendizaje de normas compartidas, la cooperación, la lealtad, la comparación social y la conformación del autoconcepto.
c) Debe evitarse para que el niño no desarrolle autonomía.
d) Se basa exclusivamente en relaciones de violencia física obligatoria.

5. El "autoconcepto" en la etapa de 6 a 12 años experimenta una transición fundamental caracterizada por:
a) Pasar de descripciones basadas en rasgos físicos concretos y posesiones externas a autodefiniciones basadas en rasgos psicológicos internos, competencias académicas y comparaciones sociales.
b) Volverse puramente mágico e irreal.
c) Disolverse completamente sin ninguna conciencia de sí mismo.
d) Depender exclusivamente del número de seguidores en redes sociales.

6. Robert Selman describe el desarrollo de la "adopción de perspectivas interpersonales" (role-taking); hacia los 8-10 años el menor alcanza:
a) La perspectiva egocéntrica indiferenciada.
b) La perspectiva autorreflexiva o mutua en segunda persona (comprende que los demás tienen puntos de vista distintos y puede verse a sí mismo desde la óptica del otro).
c) La incapacidad total de empatía social.
d) El pensamiento maquiavélico puro desprovisto de moral.

7. En el ámbito de la convivencia escolar en Educación Primaria, las dinámicas de acoso escolar (bullying) se definen técnicamente por tres notas constitutivas:
a) Intencionalidad de causar daño, reiteración temporal y asimetría o desequilibrio de poder entre agresor y víctima.
b) Discusión puntual entre dos amigos en un partido de fútbol escolar.
c) Falta de puntualidad en la entrada a clase por causas de tráfico.
d) Desacuerdo académico entre un alumno y su tutor en una calificación.

8. Según la sociometría de Jacob Levy Moreno, en un grupo-clase de educación primaria los roles de interacción social suelen clasificarse en:
a) Populares/preferidos, rechazados, ignorados/olvidados, controvertidos y promedio.
b) Militares, clérigos y campesinos.
c) Ricos y pobres exclusivamente.
d) Docentes y discentes únicamente.

9. El alumnado en situación de "rechazo sociométrico" crónico en la niñez intermedia presenta a medio y largo plazo un riesgo significativamente mayor de:
a) Éxito profesional fulgurante sin esfuerzo.
b) Desenganche escolar, absentismo, problemas de externalización conductual o depresión infantil.
c) Inmunidad biológica contra todas las enfermedades infantiles.
d) Obtener becas internacionales de excelencia académica.

10. En el desarrollo psicomotor en la etapa de 6 a 12 años:
a) Se consolida la lateralidad definitiva, mejora la coordinación viso-motriz fina y se perfecciona el esquema corporal en movimiento.
b) Se pierde el equilibrio dinámico alcanzado en la etapa previa.
c) Se detiene completamente el crecimiento de la masa muscular y ósea.
d) Se prohíbe la práctica de actividades físicas cooperativas.

11. ¿Qué es el "juego reglado" (juego con reglas) característico de la niñez intermedia según Piaget?:
a) Una actividad caótica individual sin ninguna convención.
b) Un juego colectivo estructurado donde las reglas son comprendidas como acuerdos sociales mutuos que garantizan la equidad y la competencia leal.
c) Un castigo escolar impuesto por la dirección.
d) Una prueba médica para diagnosticar la miopía infantil.

12. ¿Cuál es el papel del Educador o Educadora Social ante situaciones de exclusión relacional o dificultades de socialización en Educación Primaria?:
a) Expulsar inmediatamente al niño solitario del centro docente.
b) Aplicar técnicas sociométricas, dinamizar dinámicas de patio inclusivo, entrenar habilidades sociales y mediar con la familia y el tutor.
c) Sancionar penalmente a toda la clase con trabajos forzados.
d) Ignorar el problema esperando que se resuelva solo con la edad.

13. La teoría de las "Inteligencias Múltiples" de Howard Gardner sostiene que entre los 6 y 12 años:
a) Solo existe una única inteligencia general medida por el cociente intelectual (CI) lógico-matemático.
b) Existen al menos ocho inteligencias diferenciadas (lingüística, lógica, espacial, musical, corporal, interpersonal, intrapersonal y naturalista), que la escuela debe estimular integralmente.
c) La inteligencia se destruye si el niño juega en grupo.
d) Las artes y la música no tienen ningún valor cognitivo.

14. En la legislación andaluza (Decreto 328/2010), la tutoría en Educación Primaria tiene entre sus fines esenciales:
a) Cobrar cuotas extraordinarias a los alumnos.
b) Facilitar la integración del alumnado en el grupo-clase, fomentar el desarrollo de actitudes participativas y coordinar la acción educativa con las familias.
c) Seleccionar a los alumnos que no deben pasar al instituto.
d) Imponer castigos corporales ante la indisciplina.

15. El acompañamiento socioeducativo con familias en la etapa de niñez intermedia busca reforzar:
a) El autoritarismo punitivo inflexible sin diálogo.
b) El estilo parental democrático o inductivo, caracterizado por alto afecto y comunicación junto a límites y normas consistentes y razonadas.
c) La negligencia y el abandono total de la supervisión de deberes y amistades.
d) El aislamiento de la familia respecto a la vida comunitaria del colegio.

---

### SOLUCIONES [TEMA 9]

1. **c** — Piaget: De 6 a 12 años se desarrolla el estadio de las operaciones concretas, marcado por el pensamiento lógico aplicado a lo tangible.
2. **b** — La reversibilidad operatoria permite comprender que las transformaciones materiales pueden deshacerse o compensarse.
3. **c** — Erikson: La crisis de *Laboriosidad vs. Inferioridad* se centra en el sentimiento de competencia, laboriosidad y dominio de tareas escolares.
4. **b** — El grupo de pares es el gran laboratorio de socialización secundaria, cooperación horizontal, justicia y contraste de la autoimagen.
5. **a** — El autoconcepto se sofistica: pasa de descriptores corporales externos a rasgos de personalidad, valía social y autoeficacia.
6. **b** — Selman: En la etapa de adopción reflexiva de perspectivas (8-10 años), el niño reconoce la subjetividad y el juicio del otro.
7. **a** — Olweus: El acoso escolar exige tríada de daño intencional deliberado, persistencia temporal y asimetría de poder abusiva.
8. **a** — Moreno (Sociometría): Clasifica las posiciones relacionales en preferidos, rechazados, olvidados, controvertidos y promedio.
9. **b** — El rechazo sistemático por iguales es uno de los mayores predictores de inadaptación escolar, soledad no deseada y deserción académica.
10. **a** — En la niñez intermedia se afina la motricidad fina (escritura, dibujo), la conciencia postural y la coordinación óculo-manual.
11. **b** — Piaget (*El criterio moral en el niño*): El juego de reglas encarna la transición de la heteronomía a la autonomía moral contractual.
12. **b** — El Educador Social despliega dispositivos de recreos inclusivos, círculos de convivencia, habilidades socioafectivas y mediación.
13. **b** — Howard Gardner cuestiona el reduccionismo del CI tradicional postulando inteligencias múltiples que diversifican el talento.
14. **b** — Art. 89 Decreto 328/2010: La acción tutorial en primaria dinamiza el clima de aula, la convivencia y la relación familia-escuela.
15. **b** — Baumrind: El estilo democrático fomenta la autoestima, la competencia prosocial y el rendimiento escolar positivo.
"""

# ==========================================
# TEMA 10
# ==========================================
tests[10] = """# TEMA 10 — El desarrollo en la adolescencia y la juventud. Transiciones biográficas, vulnerabilidad y acompañamiento socioeducativo

1. En la teoría del desarrollo cognitivo de Jean Piaget, la etapa que culmina el desarrollo del pensamiento a partir de los 11-12 años se denomina:
a) Periodo sensoriomotor.
b) Periodo de las operaciones formales.
c) Periodo preconceptual.
d) Periodo analítico-intuitivo.

2. El pensamiento formal o hipotético-deductivo propio de la adolescencia se caracteriza por:
a) La subordinación de lo real a lo posible, el razonamiento combinatorio, la formulación y comprobación de hipótesis y el pensamiento proposicional.
b) La imposibilidad de entender metáforas o dobles sentidos.
c) El apego exclusivo a objetos materiales inmediatamente presentes ante la vista.
d) El pensamiento prelógico y la centración perceptiva.

3. Según Erik Erikson, la crisis psicosocial crucial que atraviesa el ser humano durante la adolescencia es:
a) Confianza básica frente a desconfianza.
b) Iniciativa frente a culpa.
c) Identidad frente a confusión (o difusión) de roles.
d) Generatividad frente a estancamiento.

4. James Marcia operacionalizó la teoría de la identidad de Erikson en cuatro "estados de identidad" basados en dos dimensiones (crisis/exploración y compromiso):
a) Identidad difusa, identidad moratoria, identidad hipotecada (o prestada) e identidad de logro.
b) Identidad rica, identidad pobre, identidad media e identidad marginal.
c) Identidad legal, identidad ilegal, identidad neutral e identidad procesal.
d) Identidad biológica, identidad médica, identidad química e identidad física.

5. El concepto de "moratoria psicosocial" formulado por Erikson hace referencia a:
a) Una enfermedad neurológica que impide al adolescente madurar.
b) Un periodo de tregua o compás de espera concedido por la sociedad en el que el joven puede experimentar diversos roles sin asumir compromisos adultos definitivos.
c) La obligación legal de trabajar sin remuneración durante tres años.
d) La prohibición judicial de salir del domicilio familiar.

6. David Elkind describe dos construcciones cognitivas egocéntricas típicas de la adolescencia temprana:
a) La audiencia imaginaria (creencia de que todos observan y juzgan sus actos) y la fábula personal (sentimiento de ser único, invulnerable e incomprendido).
b) La amnesia retrógrada y la afasia motora.
c) El altruismo universal y el desapego material.
d) La hipermetropía social y la ecolalia afectiva.

7. Desde la perspectiva sociológica contemporánea, la transición juvenil al mundo adulto se caracteriza hoy por:
a) Ser un tránsito lineal, homogéneo y rápido a los 18 años idéntico al de mediados del siglo XX.
b) Ser un proceso desestandarizado, fragmentado, prolongado, reversible y marcado por la precariedad laboral y la emancipación tardía ("trayectorias yo-yo").
c) La inexistencia de la juventud como categoría social.
d) El acceso universal garantizado a la vivienda en propiedad a los 20 años.

8. ¿Qué es la "resiliencia" en el marco de la intervención socioeducativa con adolescentes y jóvenes vulnerables?:
a) La resignación pasiva ante el dolor y el sufrimiento impuesto.
b) La capacidad humana individual y comunitaria para sobreponerse a situaciones de trauma o adversidad severa, saliendo fortalecido y con un desarrollo adaptativo positivo.
c) Un tipo de plástico utilizado en la construcción de pupitres escolares.
d) La ausencia total de problemas o conflictos en la vida.

9. ¿Cuál de los siguientes es un factor de RIESGO socioeducativo clave en la adolescencia que puede derivar en exclusión social?:
a) La pertenencia a asociaciones culturales juveniles o clubes deportivos de barrio.
b) El fracaso y abandono escolar temprano, la desestructuración familiar grave, el consumo abusivo de sustancias y el juego de apuestas patológico.
c) La existencia de un vínculo comunicativo fluido y cálido con los progenitores.
d) El acceso a programas de becas públicas de estudio.

10. El "grupo de iguales" (pandilla, grupo de amigos) en la adolescencia cumple una función de:
a) Destruir sistemáticamente la moral sin aportar ningún beneficio psicológico.
b) Refugio de pertenencia e identificación, plataforma de ensayo de autonomía frente a la familia y fuente primordial de apoyo emocional e identidad colectiva.
c) Sustituir obligatoriamente al centro de salud mental.
d) Convertirse exclusivamente en bandas armadas delictivas.

11. ¿En qué consiste el "acompañamiento socioeducativo" del Educador o Educadora Social con personas jóvenes?:
a) En vigilar y espiar las conversaciones privadas en los teléfonos de los menores.
b) En una relación profesional de ayuda no directiva basada en la escucha activa, el respeto a la libre toma de decisiones del joven y el andamiaje en la construcción de su proyecto vital.
c) En castigar con sanciones económicas a los adolescentes que expresen desacuerdo con el sistema.
d) En obligar a todos los jóvenes a estudiar la misma carrera universitaria.

12. Según la neurobiología del desarrollo cerebral, la corteza prefrontal (responsable del autocontrol, planificación, inhibición de impulsos y toma de decisiones racional):
a) Está completamente madura y finalizada a los 6 años de edad.
b) Es la última región cerebral en madurar, extendiéndose su desarrollo y mielinización hasta mediados de los 20 años, lo que explica la mayor impulsividad y búsqueda de sensaciones en la adolescencia.
c) No interviene en ningún proceso afectivo ni social.
d) Se destruye irreversiblemente al cumplir los 14 años.

13. El fenómeno del "desenganche escolar" o abandono educativo temprano en los institutos andaluces afecta de forma desproporcionada a:
a) Alumnos de familias con alto nivel socioeconómico y cultural.
b) Alumnos de familias en situación de vulnerabilidad económica, minorías étnicas segregadas y zonas con necesidades de transformación social.
c) Estudiantes universitarios de posgrado internacional.
d) Profesores jubilados con más de 40 años de servicio.

14. En la intervención con adolescentes en riesgo, el enfoque de la "Reducción de Daños" plantea:
a) Obligar al internamiento forzoso inmediato ante cualquier conducta de riesgo.
b) Minimizar las consecuencias negativas para la salud y el entorno derivadas de conductas de riesgo (drogas, sexualidad desprotegida) cuando el cese inmediato total no es factible a corto plazo.
c) Fomentar activamente el consumo de sustancias ilegales en la escuela.
d) Negar la atención médica a los jóvenes con adicciones.

15. La educación afectivo-sexual con perspectiva de género en la juventud andaluza busca:
a) Censurar cualquier manifestación de la diversidad sexual humana.
b) Fomentar relaciones basadas en el consentimiento explícito, los buenos tratos, la prevención de la violencia de género, la salud sexual y el respeto a la diversidad afectivo-sexual y de género.
c) Prohibir el uso de internet a las mujeres jóvenes.
d) Obligar a todos los estudiantes a contraer matrimonio canónico.

---

### SOLUCIONES [TEMA 10]

1. **b** — Piaget: A partir de los 11-12 años se alcanza el estadio de las operaciones formales, caracterizado por el pensamiento hipotético-deductivo.
2. **a** — El pensamiento formal permite concebir hipótesis abstractas, reflexionar sobre el propio pensamiento (metacognición) y razonar sistemáticamente.
3. **c** — Erikson: La crisis central de la adolescencia es *Identidad vs. Confusión de roles*, vital para definir valores, metas y autodefinición vocacional.
4. **a** — James Marcia estructuró los 4 estatus de identidad (difusión, moratoria, hipotecada y logro) combinando exploración y compromiso.
5. **b** — La moratoria psicosocial es el compás de espera legitimado socialmente para experimentar roles antes de consolidar compromisos adultos.
6. **a** — David Elkind conceptualiza la audiencia imaginaria y la fábula personal como sesgos del egocentrismo cognitivo adolescente.
7. **b** — Walther y autores contemporáneos describen las transiciones juveniles como "trayectorias yo-yo": reversibles, fragmentadas y prolongadas.
8. **b** — Rutter y Cyrulnik: La resiliencia no es invulnerabilidad genética sino plasticidad adaptativa promovida por tutores de resiliencia.
9. **b** — La convergencia de abandono escolar prematuro, precariedad sociofamiliar y adicciones cataliza espirales de marginación.
10. **b** — El grupo de iguales proporciona un espacio simétrico de pertenencia, diferenciación identitaria y ensayo de autonomía moral.
11. **b** — El acompañamiento socioeducativo es una relación horizontal de co-construcción del proyecto vital, evitando el paternalismo y la coerción.
12. **b** — Los estudios neurocientíficos demuestran que el sistema límbico madura antes que la corteza prefrontal, generando asincronía madurativa.
13. **b** — Las tasas de abandono educativo temprano en Andalucía guardan una correlación directa con la desigualdad socioeconómica estructural.
14. **b** — La reducción de daños es una estrategia pragmática de salud pública y educación social que prioriza la dignidad y la aminoración de riesgos.
15. **b** — III Plan de Igualdad en Educación de Andalucía: Coeducación basada en consentimiento, afectividad saludable y prevención de violencias machistas.
"""

# ==========================================
# TEMA 11
# ==========================================
tests[11] = """# TEMA 11 — La socialización y los agentes educativos. Enfoque sistémico y pedagogías comunitarias

1. En la sociología de la educación, el proceso mediante el cual los individuos aprenden e interiorizan las normas, valores, pautas de comportamiento y cultura de su sociedad se denomina:
a) Selección genética.
b) Socialización.
c) Clonación biológica.
d) Burocratización.

2. ¿Cuál es considerado el agente primordial y paradigmático de la "socialización primaria"?:
a) Los medios de comunicación masivos.
b) La familia.
c) El sindicato obrero.
d) La universidad pública.

3. En la clásica distinción sociológica entre socialización primaria y secundaria, la socialización PRIMARIA se distingue por:
a) Desarrollarse en la adultez mediante cursos de formación profesional.
b) Tener una profunda e insustituible carga afectiva e identificatoria, estructurando el núcleo de la personalidad del niño en su primera infancia.
c) Basarse exclusivamente en contratos comerciales escritos.
d) Ser un proceso optativo que no todos los seres humanos experimentan.

4. ¿Quién formuló el "Modelo Ecológico del Desarrollo Humano", concibiendo el entorno social como una serie de estructuras concéntricas interrelacionadas?:
a) Urie Bronfenbrenner.
b) Jean-Jacques Rousseau.
c) Auguste Comte.
d) René Descartes.

5. En el modelo ecológico de Bronfenbrenner, el nivel que comprende el patrón de actividades, roles y relaciones interpersonales que la persona experimenta en un entorno cara a cara determinado (ej. el hogar, el aula, el grupo de amigos) es:
a) El macrosistema.
b) El exosistema.
c) El microsistema.
d) El cronosistema.

6. Conforme a Bronfenbrenner, el "MESOSISTEMA" está constituido por:
a) Las interrelaciones entre dos o más entornos en los que la persona en desarrollo participa activamente (ej. la relación fluida o conflictiva entre la familia y la escuela).
b) El sistema económico internacional exclusivamente.
c) Las normas constitucionales del Estado.
d) Los traumas genéticos heredados de los abuelos.

7. En la ecología social de Bronfenbrenner, el "EXOSISTEMA" hace referencia a:
a) La relación biológica entre las células del cuerpo.
b) Uno o más entornos que no incluyen a la persona en desarrollo como participante activo, pero en los cuales se producen hechos que afectan a lo que ocurre en su entorno inmediato (ej. el horario y estrés laboral de los padres o las políticas municipales de servicios sociales).
c) El sistema planetario solar.
d) Las clases lectivas de educación física.

8. El "MACROSISTEMA" en la teoría ecológica abarca:
a) El cuarto de juegos del menor en su casa.
b) El marco cultural global, el sistema de creencias, la ideología dominante, las leyes, las políticas económicas y las pautas socioculturales compartidas de una sociedad.
c) Las calificaciones trimestrales del boletín escolar.
d) El horario de comidas del comedor del colegio.

9. ¿Qué añade la dimensión del "CRONOSISTEMA" al modelo ecológico del desarrollo?:
a) El precio de los relojes de pared en los institutos.
b) La influencia del tiempo y del contexto histórico social en el que transcurre la vida del individuo (ej. vivir una guerra, una pandemia o la irrupción masiva de la digitalización).
c) El cronometraje de carreras de atletismo de 100 metros lisos.
d) La fecha de caducidad de los libros de texto escolares.

10. Los medios de comunicación de masas y las plataformas digitales de redes sociales (TikTok, Instagram, YouTube) actúan en la actualidad como:
a) Agentes de socialización de enorme potencia que compiten directamente con la familia y la escuela en la transmisión de valores, modelos de belleza y pautas de consumo.
b) Herramientas neutrales que carecen de cualquier impacto sobre las creencias juveniles.
c) Dispositivos que solo usan las personas mayores de 65 años.
d) Agentes de socialización primaria formal reconocidos en la Constitución.

11. La "socialización terciaria" o resocialización se refiere a:
a) El aprendizaje de la lectura en niños de 3 años.
b) El proceso mediante el cual un individuo adulto o joven desaprende pautas desviadas o delictivas y readopta normas de convivencia integradas, habitualmente en contextos reeducativos, terapéuticos o penitenciarios.
c) La elección del menú en un restaurante comunitario.
d) El juego infantil en el recreo escolar.

12. Las "Pedagogías Comunitarias" postulan que la educación:
a) Debe recluirse exclusivamente dentro de los muros perimetrales del centro docente sin contaminación con el barrio.
b) Es un proceso colectivo, corresponsable y territorializado donde toda la comunidad (vecinos, entidades, instituciones) se constituye en agente educativo activo y transformador.
c) Debe privatizarse y entregarse a corporaciones financieras transnacionales.
d) Tiene que suprimirse a partir de los 12 años de edad.

13. Marco Marchioni es un referente indiscutible de la intervención comunitaria por su modelo basado en la interacción armónica de tres protagonistas:
a) Los jueces, los policías y los carceleros.
b) La Administración pública, los Recursos técnicos/profesionales y la Población/Ciudadanía.
c) Los bancos, las inmobiliarias y las grandes constructoras.
d) El profesorado, la inspección y el ministerio exclusivamente.

14. ¿Cuál es el papel nuclear del Educador o Educadora Social desde una perspectiva ecosistémica en un barrio o municipio andaluz?:
a) Gestionar de forma aislada expedientes sancionadores en un despacho cerrado.
b) Tejer redes de conexión e interdependencia positiva entre los distintos sistemas (familia-escuela-barrio), articulando recursos comunitarios y empoderando a la ciudadanía.
c) Vigilar que ningún vecino hable en la vía pública sin permiso previo.
d) Impartir clases particulares a domicilio previo pago de honorarios privados.

15. El concepto de "capital cultural" acuñado por Pierre Bourdieu se manifiesta en tres estados:
a) Estado líquido, estado sólido y estado gaseoso.
b) Estado incorporado (disposiciones duraderas, habitus), estado objetivado (bienes culturales, libros, cuadros) y estado institucionalizado (títulos académicos oficiales).
c) Estado estatal, estado autonómico y estado provincial.
d) Estado bancario, estado crediticio y estado bursátil.

---

### SOLUCIONES [TEMA 11]

1. **b** — La socialización es el proceso sociológico y pedagógico de transmisión, asimilación e interiorización de la cultura y pautas sociales.
2. **b** — La familia es la agencia primaria universal donde se forjan las primeras relaciones de apego, comunicación y matriz identitaria.
3. **b** — Berger y Luckmann: La socialización primaria es insustituible por su arraigo afectivo incuestionado y su eficacia constitutiva del yo.
4. **a** — Urie Bronfenbrenner formuló en 1979 la *Ecología del desarrollo humano*, superando los modelos unidireccionales de laboratorio.
5. **c** — El microsistema es el escenario inmediato de relaciones interpersonales cara a cara (familia, aula, club deportivo).
6. **a** — El mesosistema comprende las interconexiones vivas entre los microsistemas del sujeto (ej. coordinación o fractura familia-escuela).
7. **b** — El exosistema influye decisivamente en el desarrollo aunque el sujeto no esté presente físicamente (empleo materno, servicios sociales).
8. **b** — El macrosistema engloba la cultura, ideología, valores axiológicos, legislación y sistema sociopolítico transversal.
9. **b** — El cronosistema integra el vector temporal histórico y los hitos vitales biográficos que condicionan los demás sistemas.
10. **a** — Las tecnologías digitales operan como un "currículo invisible" masivo con capacidad hegemónica de modelado conductual juvenil.
11. **b** — La socialización terciaria implica la reestructuración de roles y desaprendizaje de pautas desadaptadas o penitenciarias.
12. **b** — La pedagogía comunitaria (Marchioni, Freire) democratiza la acción educativa integrando territorio, activos barriales y participación.
13. **b** — Marchioni: El triángulo relacional comunitario lo integran Administraciones, Recursos Técnicos y Ciudadanía autoorganizada.
14. **b** — El Educador Social actúa como bisagra intersistémica, dinamizando sinergias entre los microsistemas y el entorno institucional.
15. **b** — Bourdieu distingue el capital cultural en tres estados: incorporado (habitus), objetivado (recursos materiales) e institucionalizado (títulos).
"""

# ==========================================
# TEMA 12
# ==========================================
tests[12] = """# TEMA 12 — La dimensión moral de la educación. Valores, ciudadanía crítica y dilemas socioeducativos

1. En la teoría del desarrollo del juicio moral de Jean Piaget (*El criterio moral en el niño*, 1932), el paso fundamental que se produce entre los 6-7 años y los 10-12 años es:
a) El tránsito de la moral de heteronomía (o realismo moral) a la moral de autonomía (o reciprocidad y cooperación).
b) El paso de la bondad infinita a la maldad congénita.
c) El abandono de cualquier principio moral en beneficio del egoísmo puro.
d) La asimilación forzada del dogma inquisitorial medieval.

2. En la "moral heterónoma" o de coacción descrita por Piaget:
a) Las reglas son vistas como sagradas, inmutables y de origen exterior incuestionable (adulto/dios), y la justicia se juzga por las consecuencias materiales del acto (responsabilidad objetiva) y no por la intención.
b) El niño juzga los actos atendiendo exclusivamente a la intención del autor.
c) Las normas se pactan democráticamente entre iguales.
d) La justicia se define como equidad compasiva contextualizada.

3. Lawrence Kohlberg amplió y universalizó las tesis de Piaget estructurando el desarrollo del juicio moral en:
a) Dos etapas biológicas.
b) Tres niveles (Preconvencional, Convencional y Postconvencional), cada uno subdividido en dos estadios (un total de 6 estadios).
c) Diez mandamientos invariables.
d) Cuatro temperamentos humorales hipocráticos.

4. En el NIVEL PRECONVENCIONAL de Kohlberg (típico de niños pequeños y algunos adolescentes/adultos):
a) La persona actúa según principios éticos universales de justicia y dignidad humana.
b) Las normas se respetan primordialmente para evitar el castigo físico de la autoridad (Estadio 1) o para obtener recompensas y beneficios inmediatos (Estadio 2: instrumental individualista).
c) El individuo prioriza el bien común de la sociedad por encima de su supervivencia.
d) Se defiende la desobediencia civil pacífica ante leyes injustas.

5. En el NIVEL CONVENCIONAL de Kohlberg:
a) El sujeto se conforma y acata activamente las expectativas de su grupo social de pertenencia (Estadio 3: "buen chico/buena chica") y las leyes del orden social establecido para mantener la estabilidad del sistema (Estadio 4: ley y orden).
b) El sujeto vive al margen de la ley cometiendo delitos sin remordimiento.
c) El individuo no reconoce la existencia de normas sociales.
d) Se aplican únicamente las normas de la naturaleza animal salvaje.

6. El NIVEL POSTCONVENCIONAL o de principios éticos universales (Estadios 5 y 6 de Kohlberg) se caracteriza por:
a) La comprensión de que las leyes son contratos sociales basados en derechos fundamentales que pueden modificarse democráticamente (Estadio 5) y la adhesión a principios éticos universales de justicia, equidad y dignidad humana que superan a cualquier ley formal injusta (Estadio 6).
b) La obediencia ciega y sumisa al líder dictatorial.
c) El miedo al encarcelamiento como único freno a la conducta.
d) La satisfacción inmediata de los impulsos biológicos primarios.

7. Carol Gilligan criticó el modelo de desarrollo moral de Lawrence Kohlberg argumentando que:
a) Había sido investigado exclusivamente con varones, sesgando la teoría hacia una "ética de la justicia y los derechos formales abstractos", e invisibilizando la "ética del cuidado y la responsabilidad vincular", más desarrollada en las mujeres por su socialización.
b) Kohlberg era demasiado indulgente con los delincuentes.
c) La moral no existe en los seres humanos.
d) Los dilemas morales deben resolverse mediante el lanzamiento de una moneda al aire.

8. En el ámbito de la intervención socioeducativa, los "dilemas morales" (como el célebre dilema de Heinz):
a) Son pruebas médicas de rayos X cerebrales.
b) Son situaciones conflictivas ficticias o reales que enfrentan dos valores legítimos en pugna, utilizadas como técnica pedagógica dialógica para provocar desequilibrios cognitivos y ascender en el razonamiento moral.
c) Son castigos escolares que implican la copia de frases cien veces.
d) Son encuestas electorales de intención de voto para partidos políticos.

9. La "clarificación de valores" (Raths, Harmin y Simon) como metodología educativa plantea que:
a) El profesor debe adoctrinar e inculcar sus propios valores personales obligatoriamente a los alumnos.
b) El estudiante debe aprender a elegir libremente sus valores entre alternativas, reflexionar críticamente sobre las consecuencias de su elección y actuar coherentemente con ellos en su vida cotidiana.
c) No existen valores legítimos en una sociedad democrática.
d) Se debe prohibir la discusión de temas éticos en la escuela.

10. Una "educación para la ciudadanía crítica" busca formar personas que:
a) Acepten pasivamente las noticias falsas y la manipulación informativa de las redes sociales.
b) Desarrollen juicio crítico propio, cuestionen las desigualdades estructurales, participen activamente en la vida pública y promuevan los derechos humanos y la justicia distributiva.
c) Se nieguen a convivir con personas de diferente procedencia cultural o religión.
d) Defiendan el uso de la violencia para imponer sus opiniones particulares.

11. El concepto de "aporofobia", acuñado por la filósofa española Adela Cortina, define:
a) El rechazo, aversión, odio y desprecio hacia las personas pobres y desfavorecidas.
b) El miedo patológico a volar en aviones comerciales.
c) La fobia a los espacios cerrados en centros penitenciarios.
d) La alergia alimentaria a los frutos secos.

12. En la educación en valores en el sistema educativo andaluz, el enfoque de la "transversalidad" implica que:
a) Los valores democráticos, la igualdad, la paz y la sostenibilidad no se imparten como una asignatura aislada, sino que deben impregnar todo el currículo, el clima de centro y la práctica docente diaria.
b) Solo se habla de valores un día al año en el festival de fin de curso.
c) Los valores se sortean en una tómbola al inicio del curso.
d) La moral se delega en empresas de seguridad privada.

13. ¿Qué postura ética debe adoptar el Educador o Educadora Social frente a los dilemas morales de las personas con las que interviene?:
a) Imponer de forma dogmática su moral personal o religiosa.
b) El respeto a la dignidad y autodeterminación de la persona, garantizando la justicia distributiva, la no maleficencia y el acompañamiento reflexivo sin juzgar moralísticamente.
c) Desentenderse del caso para no asumir responsabilidades profesionales.
d) Denunciar penalmente a quien mantenga opiniones ideológicas diferentes a las suyas.

14. Jürgen Habermas fundamenta su "Ética del Discurso" en el principio de que:
a) Las normas morales legítimas son aquellas que resultan de un diálogo racional y simétrico en una comunidad ideal de comunicación, donde todos los afectados tienen voz en igualdad de condiciones.
b) La fuerza militar es la única que tiene derecho a decidir qué es bueno y malo.
c) La moral la dicta el mercado bursátil de forma automática.
d) El silencio absoluto es superior a la deliberación colectiva.

15. La educación para el pensamiento crítico en la era de los algoritmos y la infoxicación mediática debe capacitar al alumnado para:
a) Compartir de forma compulsiva cualquier bulo en redes sociales sin verificar su veracidad.
b) Contrastar fuentes, detectar sesgos cognitivos, diferenciar hechos objetivos de opiniones interesadas y sostener argumentos fundados con rigor lógico y ético.
c) Creer ciegamente en todo lo que afirmen los influencers de moda.
d) Dejar de leer libros y prensa para informarse solo por memes.

---

### SOLUCIONES [TEMA 12]

1. **a** — Piaget (*El criterio moral en el niño*): La evolución moral progresa desde la heteronomía coactiva hacia la autonomía de cooperación.
2. **a** — La moral heterónoma juzga por la gravedad material física del resultado (responsabilidad objetiva) sin considerar la intencionalidad subjetiva.
3. **b** — Lawrence Kohlberg sistematiza tres niveles universales (Preconvencional, Convencional, Postconvencional) divididos en seis estadios.
4. **b** — El nivel preconvencional basa el juicio moral en el principio hedonista de evitar castigos físicos o maximizar ventajas egoístas inmediatas.
5. **a** — El nivel convencional legitima la moral en la conformidad social ("ser buen chico") y la preservación incuestionada del orden y la ley.
6. **a** — El nivel postconvencional comprende el contrato social garantista de derechos y la primacía ética de la dignidad humana universal.
7. **a** — Carol Gilligan (*In a Different Voice*): Revela el sesgo patriarcal de Kohlberg y reivindica la Ética del Cuidado y los vínculos afectivos.
8. **b** — Los dilemas morales son catalizadores didácticos deliberativos para suscitar conflicto sociocognitivo y maduración axiológica.
9. **b** — La clarificación de valores (Raths) entrena el proceso de valorar: elección libre y ponderada, aprecio público y acción coherente.
10. **b** — La ciudadanía crítica combina deliberación democrática, alfabetización cívica, no violencia y compromiso solidario activo.
11. **a** — Adela Cortina forjó el término *aporofobia* para evidenciar que el odio xenófobo o discriminatorio radica nuclearmente en la pobreza.
12. **a** — La transversalidad curricular (LOMLOE y LEA) impregna todas las áreas, la convivencia de centro y el proyecto institucional.
13. **b** — Código Deontológico de ASEDES: Respeto escrupuloso a la autodeterminación del sujeto, no maleficencia y neutralidad confesional.
14. **a** — Habermas (*Teoría de la acción comunicativa*): La validez ética reside en el consenso racional intersubjetivo sin coacciones.
15. **b** — El pensamiento crítico emancipa a la persona frente a la desinformación, las cámaras de eco digitales y la polarización tóxica.
"""

# Write batch 3 to files
for num in range(9, 13):
    path = os.path.join("tests_andalucia", f"test_tema_{num:02d}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(tests[num].strip() + "\n")
    print(f"Written: {path}")
