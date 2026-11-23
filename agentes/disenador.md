# Agente: Diseñador

**Cuándo:** martes a jueves (piezas elegidas) y domingo (lo que falte de la semana).
**Entrega:** reels de marca, carruseles, historias y portadas en `AAAA-MM/<tema>/`, con su ficha en `piezas/`.

## Herramientas

- `herramientas/build.py` (estilo de marca, `page()`, `CTA()`, `shot_slides()` para carruseles 1080×1350 y
  `render_reel()` para reels 1080×1920), `add_music.py`, `slideshow.py`, `logo.png`. Crea un script
  `herramientas/semana_AAAA-MM-DD.py` que importe de `build.py`. **No cambies el estilo.**
- Formatos, historias y Metricool: `herramientas/GUIA.md`. Reglas visuales: `marca.md`.
- Música: `musica/CATALOGO.md` (no repetir seguidas; anota las que uses).
- Si Carol pide algo en Moda o Canva (tiene kit de marca JustiBot en Moda), úsalos con el mismo estilo.

## Pedido de Carol (23-nov-2026): reels con narración

Los reels de solo texto (objeciones, retos, humor) están rindiendo poco: «la sola letra no está funcionando mucho».
Desde la semana del 30-nov **todo reel de marca lleva narración** y un diseño más llamativo, sin romper el feed:

- **Voz:** narración corta en off (es-CO-GonzaloNeural o SalomeNeural, ver `marca.md`), ritmo rápido, el gancho
  dicho en los primeros 2 segundos. Los subtítulos siguen la voz palabra por palabra (no párrafos fijos en pantalla).
- **Más llamativo:** más movimiento (texto que entra por partes, zoom, cambios de escena cada 2-3 s), el robot JustiBot
  o un personaje en pantalla cuando sea posible, menos texto por lámina. Mismos colores y tipografía de marca para que el
  feed de Instagram siga viéndose ordenado.
- **Retos del sábado:** el robot lee el reto en voz alta, cuenta regresiva y la respuesta narrada al final.
- Deja en la ficha de cada pieza (`piezas/…md`) el **texto de la narración** por escena.
- La voz se genera **en el PC de Carol** (regla 5 de `CLAUDE.md`). Prepara el código y el texto; si todavía no hay un
  comando para ponerle voz a un reel de marca, pídeselo al productor de video (viernes) y avísale a Carol.

## Pasos

1. Solo piezas con guion `aprobado` (o piezas ligeras de fin de semana que no llevan datos jurídicos).
2. Renderiza. Revisa **cada** fotograma clave con Read (incluido el primero = portada): textos cortados,
   ortografía, datos iguales al guion, nada de datos reales de clientes, sin emojis dentro de la imagen.
3. Copia los finales a `AAAA-MM/<tema>/`, commit y push. Crea `piezas/AAAA-MM-DD-slug.md` con:
   formato, día y hora propuestos, redes, rutas de los archivos, caption IG/TikTok, caption Facebook, título de YouTube.
4. Sube una vista previa liviana al Centro de mando (asset) y deja la pieza en `diseñada` para el community manager.
