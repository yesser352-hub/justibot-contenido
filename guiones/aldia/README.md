# JUSTIBOT AL DÍA: cómo se escribe un episodio

Cada episodio es un archivo `episodio.json` que se copia a `videos/src/aldia/episodios/ADNN/` en la rama `videos/aldia`
del repo Justibot. Aquí queda una copia de cada episodio aprobado (`ADNN-slug.json`). Reglas editoriales: `marca.md`,
sección "JUSTIBOT AL DÍA". Ejemplo real: `AD01-caso-char.json`.

## Campos

- `id` ("AD02"), `numero` (2), `titulo` (interno), `ticker` (3 frases cortas en MAYÚSCULAS para la cinta de abajo).
- `lineas`: 9 a 12, en orden. Cada una:
  - `quien`: `ella` (Carol Rodríguez), `el` (Yesser Palacios) o `robot` (JustiBot, analista jurídico).
  - `texto`: lo que dice. Números en letras ("once años", "dos mil dieciocho"). Frases cortas.
  - `gesto` (opcional): `mesa`, `abierta`, `senala`, `juntas`, `explica`. `lado`: -1 o 1 cuando señala.
  - `cara` (opcional): `neutral`, `sonrisa`, `seria`, `sorpresa`, `duda`.
  - `pantalla` (opcional), lo que muestra el LED grande:
    - `{"tipo":"caso","lugar":"…","fecha":"…","titular":"≤ 70 letras","fuente":"Medio · Medio"}`
    - `{"tipo":"estado","etapa":"investigado|imputado|acusado|condenado|absuelto","nota":"≤ 35 letras"}`
    - `{"tipo":"norma","norma":"Artículo N · Ley","titulo":"Figura","texto":"cita literal ≤ 80 letras"}`
    - `{"tipo":"pregunta","texto":"la pregunta final"}`
  - `zocalo` (opcional): franja roja de ÚLTIMA HORA, una sola vez, en la línea del caso.
  - `toma` (opcional): forzar plano (`pantalla`, `dos`, `ella`, `el`, `robot`). Usa `pantalla` si el robot habla de
    una norma, para que se lea el LED.
- `pregunta`: la misma pregunta final (sale en grande en el cierre).
- `fuentes`: lista de las fuentes de cada dato (2 por dato). No sale en pantalla.
- `SAY` (opcional): cómo se pronuncia una palabra rara, por ejemplo `{"SIC": "sic"}`.

## Estructura recomendada (≈ 80 s)

1. Saludo de Carol (siempre: "Buenas noches. Esto es JustiBot al día: historias reales y debates sin filtros. Soy Carol Rodríguez.")
2. Yesser se presenta y dice el tema en una frase.
3. El caso, con pantalla `caso` y zócalo.
4. Un dato más.
5. La etapa procesal, con pantalla `estado` ("No ha sido condenado" si es así).
6. Contexto (otra parte, otra decisión).
7. Robot: presunción de inocencia o el punto jurídico.
8. Robot: la norma con pantalla `norma` y `toma: pantalla`.
9. La versión de la defensa y la de la autoridad.
10. Qué sigue en el proceso.
11. Carol: la pregunta a los abogados, con pantalla `pregunta`.
