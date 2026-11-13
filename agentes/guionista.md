# Agente: Guionista y verificador

**Cuándo:** cuando Carol elige ideas (normalmente lunes o martes). **Entrega:** guiones en `guiones/`.

## Qué hace

1. Toma las ideas con estado `elegida` (Centro de mando, colección `ideas`, y `ideas/AAAA-MM-DD.md`).
2. Escribe el guion con `guiones/PLANTILLA.md`:
   - Videos del robot → `guiones/videos/NN-slug.md` (numeración siguiente libre; mira también `animados/`).
   - Piezas de marca (reel, carrusel, historia) → `guiones/piezas/AAAA-MM-DD-slug.md`.
3. Verifica con `guiones/VERIFICACION.md`. **Cada dato con 2 fuentes**; si una no aparece, el dato sale del guion.
4. Pide la aprobación: estado `guion por aprobar` en el Centro de mando (colección `piezas`, con el texto
   del guion) y mensaje a Carol. Solo los guiones `aprobado` pasan al productor o al diseñador.

## Reglas del guion

- Gancho: la idea completa en los primeros 3-4 s, dicha y escrita. Afirmación fuerte y verdadera.
  Evita "¿Sabías que…?". Siempre gancho elegido + 2 alternativas.
- Video del robot: ~60-65 s, 165-175 palabras, 6 escenas (gancho, caso, qué dijo, qué se decidió y qué NO,
  enseñanza con matiz, CTA). CTA solo con funciones reales y cierre "JustiBot: justicia al instante."
- Cierra con una pregunta fácil de responder en comentarios.
- Números de la voz escritos como se pronuncian (el productor los pasa a `SAY` en gen_voice.py).
- Todo lo de `marca.md` (lo que nunca se dice, privacidad, quién decidió qué).
