# Los hijos no son un arma
Composición Remotion `HijosShort` (código en `src/hijos/`). Voz: edge-tts `es-CO-GonzaloNeural`, una toma por escena
(`voice4/gen_voice.py`). Duración ~62 s (sale de la voz; ver `voice4/meta.json`).

## Datos verificados (no cambiar sin revisar la fuente)
- Sentencia **STC13455-2026**, Corte Suprema de Justicia, **Sala de Casación Civil, Agraria y Rural**, aprobada el
  **22 de julio de 2026** (M.P. Martha Patricia Guzmán Álvarez). Publicitada por la Corte el 7 de octubre de 2026.
- Dos niñas que estuvieron mucho tiempo con contacto restringido con su madre (entre diciembre de 2024 y marzo de 2026
  la vieron en persona en contadas ocasiones). El ICBF había ordenado **llamadas diarias** y **visitas supervisadas**.
- La Corte amparó los derechos de las niñas (tutela de la Procuraduría), dejó sin efecto la decisión del Juzgado Tercero
  de Familia de Barranquilla y le ordenó **decidir de nuevo** (valorar la conducta obstructiva como maltrato, examinar
  la afectación y adoptar medidas para restablecer el vínculo). **No definió la custodia.**
- La Corte negó la tutela del padre contra las sanciones por incumplir medidas de protección: una multa y luego
  **arrestos de 30 y 45 días**. Los arrestos **no los impuso la Corte**: ya estaban impuestos y se mantuvieron.
- La Corte aclara que la obstrucción debe probarse con **hechos verificables** (no es cualquier desacuerdo entre padres
  ni el llamado "síndrome de alienación parental").
- Fuentes: Vanguardia (18-ago y 13-oct-2026), El Heraldo (21-ago-2026), Infobae (8-oct-2026), La Veintitrés.

## Gancho (investigación)
- La gente decide en 1,5 a 2,5 s si se queda; la retención a los 3 s predice buena parte del alcance.
- Muchos ven sin sonido: el gancho tiene que estar **escrito en pantalla** desde el primer segundo, con movimiento.
- Funciona mejor la afirmación fuerte o el vacío de curiosidad que el «¿Sabías que…?» (muy gastado y lento: la idea
  llegaba al segundo 6). Por eso la frase empieza por la consecuencia y cierra con la autoridad («Lo dijo la Corte
  Suprema»), y la imagen abre con una puerta que se cierra (movimiento + símbolo de separación).
- Variantes para probar en otros cortes del mismo video (cambiar `SCENES[0]` en `gen_voice.py` y el primer título en
  `src/hijos/story.ts`):
  1. **(usada)** «Alejar a un hijo, una y otra vez, de su mamá o de su papá puede ser violencia intrafamiliar. Lo dijo la Corte Suprema.»
  2. «Dos niñas pasaron más de un año casi sin ver a su madre. La Corte Suprema dijo que eso puede ser violencia.»
  3. «Usar a los hijos contra el otro papá o la otra mamá puede salir caro. La Corte Suprema ya lo dejó claro.»

## Narración por escena
1. Alejar a un hijo, una y otra vez, de su mamá o de su papá puede ser violencia intrafamiliar. Lo dijo la Corte Suprema.
2. Dos niñas pasaron más de un año casi sin ver a su madre, pese a las visitas y llamadas que había ordenado el Bienestar Familiar.
3. En la sentencia STC13455 de 2026, la Corte explicó que obstruir ese vínculo, de forma reiterada y sin justificación, puede ser maltrato: afecta la salud emocional de los niños.
4. Amparó a las niñas y ordenó al juzgado de familia decidir de nuevo; no definió la custodia. Y mantuvo los arrestos de 30 y 45 días que ya le habían impuesto al padre por incumplir medidas de protección.
5. Ojo: no todo desacuerdo entre padres es violencia; hay que probarlo con hechos. Pero los hijos nunca deben ser un arma.
6. ¿Y cómo sabes cuándo se mueve tu proceso? JustiBot vigila tus procesos en las fuentes oficiales y te avisa por correo de cada actuación nueva. Sin perseguir portales. JustiBot: justicia al instante.

## Cambios frente al guion propuesto (y por qué)
- Gancho: sin «¿Sabías que…?»; la idea completa llega en 4 s y está escrita en pantalla.
- Escena 2: se nombra lo que había ordenado el ICBF (llamadas diarias y visitas supervisadas), que es lo que la Corte valoró.
- Escena 4: «ordenó al juzgado decidir de nuevo; no definió la custodia» separa la orden de una decisión final de custodia.
  Los arrestos «ya le habían impuesto» y la Corte «los mantuvo»: no se dice que la Corte los impuso.
- Escena 5: «no todo desacuerdo entre padres es violencia; hay que probarlo con hechos» evita presentarlo como regla automática.
- Escena 6: solo lo que JustiBot hace (vigilar procesos en fuentes oficiales y avisar por correo de actuaciones nuevas).
- Se recortó de ~200 a ~170 palabras para caber en 60-65 s sin acelerar la voz.

## Textos en pantalla
Títulos en `src/hijos/story.ts` (`TITLES`); hologramas en `src/hijos/holo4.ts`. Personas solo como siluetas abstractas;
la «foto familiar» del pasillo son manchas de color sin rostros. Las niñas no se nombran ni se recrean.
