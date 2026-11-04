# Guía de la tarea semanal de contenido JustiBot

Esta guía la sigue la tarea automática de los domingos. Todo lo necesario está en este repositorio.

## Preparar el entorno (cada vez)
```bash
git clone https://github.com/yesser352-hub/justibot-contenido.git /home/claude/justibot-contenido   # si no existe
cd /home/claude/justibot-contenido/herramientas && npm install --silent
```
- `build.py`: estilos de marca (HEAD con tokens), `page()`, `CTA()`, `shot_slides()` (carruseles 1080x1350 PNG) y `render_reel()` (Reels 1080x1920 MP4 con animación `ANIM_JS`). Úsalo como plantilla: importa `HEAD, page, CTA, shot_slides, render_reel, OUT, LOGO` desde un script nuevo de la semana y define ahí las láminas/escenas nuevas. No cambies el estilo.
- `add_music.py video.mp4 ../musica/<canción>.mp3 salida.mp4`: pone música (-16 LUFS, fade).
- `slideshow.py carpeta_png salida.mp4 4.5`: convierte un carrusel en video 1080x1920 para TikTok.
- `../musica/CATALOGO.md`: canciones por tipo de pieza y registro de las ya usadas (no repetir la misma en dos piezas seguidas; anota las nuevas).
- `logo.png`: logo blanco oficial. Siempre en el cierre.
- Las fuentes Inter vienen del sistema; IBM Plex Mono por npm. No uses emojis dentro de imágenes o videos (no se ven).

## Reglas de marca y contenido (no negociables)
- Estilo: fondo azul marino #0a1525 con brillo azul, acento #3b82f6, tipografía Inter gruesa. Que no se vea "hecho con IA": sobrio, profesional, nada de imágenes generadas.
- Cierre: logo + "Pruébalo gratis · www.justibot.com.co" (siempre con www).
- Nunca inventar funciones. Hechos confirmados: JustiBot consulta fuentes oficiales (Rama Judicial, SAMAI, SIUGJ, SIC, Supersociedades, Supersalud, Superfinanciera, Contraloría, Fiscalía, Policía); envía el reporte por correo TODOS los días haya o no novedades (nunca decir "solo te escribe cuando pasa algo"); envía fecha y descripción de cada actuación, NO el auto escaneado; no cobra por radicado; calculadora de términos en días hábiles con festivos y vacancia; pantalla "Tu día"; importar procesos desde Excel; planes Starter (1 mes gratis), Municipal $19.900, Circuito $39.900, Distrito $64.900.
- El reporte NO se puede reenviar al cliente (trae procesos de varios clientes).
- El tema "perder una actuación/término" está quemado: no usarlo. Sí gusta el humor del día a día del litigio.
- Nunca mostrar datos reales de clientes (radicados, partes, juzgados): usar las capturas pixeladas de `capturas/` o ejemplos claramente ficticios.
- Español de Colombia, trato de "tú" al público; "Dr./Dra." solo en mensajes a embajadores.

## Formatos por red (Metricool, blogId 6544004, zona America/Bogota)
- Cada pieza va en DOS publicaciones de Metricool:
  1. Instagram + TikTok: texto termina en "Pruébalo gratis 👉 enlace en el perfil".
  2. Facebook sola: el mismo texto pero con "Pruébalo gratis 👉 https://www.justibot.com.co/".
- Carruseles: Instagram (POST con las PNG) y Facebook (POST) como carrusel; para TikTok, publicación aparte solo TikTok con el video de `slideshow.py` + música.
- Reels: la PORTADA es el primer fotograma. render_reel ya pone la primera escena completa al inicio; si usas un video de Carol u otro, agrega al inicio un fotograma con el título visible (nunca un fondo vacío).
- Publica también sábado y domingo: el calendario semanal debe cubrir de lunes a domingo (fines de semana con piezas ligeras: humor, fechas, tips).
- Reels: con música de la biblioteca; Instagram REEL, Facebook REEL, TikTok con `tiktokData.title` obligatorio.
- Medios: sube los archivos a este repo en `AAAA-MM/...`, haz push y usa la URL raw fijada al commit: `https://raw.githubusercontent.com/yesser352-hub/justibot-contenido/<sha>/<ruta>`.
- Crea todo con `draft: true` (Carol revisa y aprueba). Horarios que funcionan: 12:15 y 18:30; 7:00 para piezas de "mañana".
- 4 a 8 hashtags: #abogadoscolombia #litigio #ramajudicial #derechocolombia #justibot + 1 o 2 del tema.

## YouTube Shorts (canal conectado en Metricool)
- Cada Reel de la semana va también como Short: publicación aparte solo YouTube (provider "youtube"), el mismo video, a las 6:00 p. m. (domingos 6:30 p. m.), un Short por día.
- youtubeData: {"title": "<título corto> #Shorts" (máx. 100 caracteres), "type": "short", "privacy": "public", "madeForKids": false, "category": "EDUCATION" (humor: "COMEDY"), "tags": [4 o 5 palabras clave]}. Sin videoThumbnailUrl.
- Texto: el caption de Facebook (con https://www.justibot.com.co/) y hashtags empezando por #Shorts.
- Intercala los videos animados del robot (los de más enganche) con los demás formatos. Si en la semana hay pocos Reels nuevos, completa los días con Reels anteriores que no hayan salido en YouTube (no los de fechas ya pasadas como festivos o Halloween).
- Agrega el uuid del Short al documento de `posts` de esa pieza.

## Tablero de pendientes
URL: https://claude.ai/artifact/L82r9TG3Lbd3yghzpQaH2C (ArtifactData; colecciones `posts` y `tasks`).
- Carol revisa y APRUEBA desde el tablero: el botón "Aprobar y programar" cambia los borradores de Metricool a programados. Por eso cada pieza necesita su vista previa y los uuid de Metricool.
- Vistas previas: haz versiones livianas (videos `ffmpeg -vf scale=540:-2 -crf 28`, láminas JPG 540x675), primero lee el artefacto con la herramienta Artifact (`action: "read"`, url de arriba) y luego súbelas con Artifact `action: "publish"`, `url`, `asset: true`, `file_paths`. Guarda los `id` que devuelve.
- `posts` (un documento por pieza, id libre): {date "AAAA-MM-DD", time "12:15 p. m.", title, format, uuids: [uuid de CADA publicación de Metricool de esa pieza, incluida la de Facebook y la de TikTok aparte], preview: {kind "video"|"images", ids: [ids de assets]}, caption: texto de Instagram}. Puedes borrar las de hace más de 3 semanas (y sus assets con `delete`).
- Cambios pedidos: Carol puede tocar "Pedir cambio" en una publicación. Eso guarda `change` en el documento de `posts` y crea en `tasks` (col "claude") una tarjeta con `postId`. Cada domingo, ANTES de crear piezas nuevas, atiende esos cambios si la publicación aún no ha salido: rehaz la pieza, reemplaza el medio y el texto en Metricool (updateScheduledPost, dejándola en borrador), sube la nueva vista previa, actualiza el `posts` (borra `change` con {"__delete__": true}) y mueve la tarjeta a "hecho". Cuéntalo en el resumen.
- `leads` (prospectos) y `ambassadors` (embajadoras) también viven aquí; no los cambies salvo que la tarea lo pida.
- `tasks`: {title, note, due "AAAA-MM-DD" opcional, area contenido|embajadoras|ventas|producto|web|otros, col tuyo|claude|espera|hecho, order}. Agrega en `tuyo` una tarjeta "Revisar y aprobar las piezas de la semana del …". Lee siempre antes de escribir y usa if_version.

## Historias de Instagram (2 o 3 por semana)
- Formato 1080x1920, mismo estilo de marca. Deja libre una franja de unos 400 px en la parte baja (y 250 px arriba) para que Carol ponga el sticker de enlace o de encuesta.
- Tipos que rotan: (1) encuesta o pregunta a la comunidad ("¿Cuántos procesos llevas?", "¿Qué portal te saca más canas?"), con el texto "Responde aquí 👇" encima del espacio libre; (2) dato o fecha del calendario judicial de esa semana; (3) recordatorio de la publicación más fuerte de la semana ("Nuevo Reel 👉").
- Renderízalas como PNG con shot_slides cambiando el alto a 1920 (o con page() en un viewport 1080x1920). Súbelas al repo en AAAA-MM/historias/.
- No van a Metricool: los stickers de enlace y encuesta solo se ponen a mano en la app. Súbelas como assets al tablero y crea en `posts` un documento por historia con format "Historia · súbela tú", uuids [] y en caption qué sticker poner (por ejemplo: "Sticker de encuesta: Menos de 50 / Más de 50" o "Sticker de enlace: https://www.justibot.com.co/").
- Agrega en `tasks` (col "tuyo", area "contenido", due = el día de la primera) una tarjeta "Subir las historias de la semana" que diga qué día va cada una.
- Recuérdale a Carol en el resumen: cada publicación nueva se comparte en historias el mismo día con el sticker de enlace.
