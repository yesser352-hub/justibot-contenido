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
- Agrega el uuid del Short al documento de `piezas` de esa pieza.

## Videos animados del robot (carpeta `animados/listos/`)
- Carol los genera en otra sesión de Claude y los sube aquí: cada video .mp4 con un .txt del mismo nombre (caso, fuentes) y su portada .jpg. Son el formato con más enganche.
- Cada domingo, ANTES de armar el resto, revisa `animados/listos/`. Por cada video:
  1. Verifica el caso con búsqueda web (número de sentencia, fecha, sala, cifras). Si algo del video no coincide con las fuentes, NO lo programes: déjalo en el Centro de mando con estado "Te necesita" en el agente y explícale a Carol qué corregir.
  2. Si el primer fotograma no tiene texto, antepón la portada (0,15 s, audio con retraso de 150 ms) como en las otras piezas.
  3. Prográmalo (borrador) en Instagram + TikTok y Facebook a las 6:30 p. m., y como Short de YouTube al día siguiente. Caption con el caso, la sentencia y "no todo es X" si aplica; nunca inventes datos que no estén en las fuentes.
  4. Muévelo a `animados/publicados/` (git mv) y haz push.
- Meta: 2 videos animados por semana (por ejemplo martes y viernes), intercalados con los demás formatos. Si hay más de 2, deja el resto para la semana siguiente.

## Centro de mando (reemplaza al tablero viejo)
Todo lo de aprobar, ideas, estados de agentes y aprendizajes vive en el Centro de mando:
https://claude.ai/artifact/NwSo9EKAAJEQm9ZyRW6SFH. Esquema de datos, estados y cómo subir vistas previas: `centro-de-mando.md`.
- Cada pieza nueva: documento en `piezas` con su vista previa, uuids de Metricool y `estado: "por aprobar"`.
- Carol aprueba ahí; la revisión diaria del community manager programa lo aprobado que no se haya programado solo.
- El tablero viejo (L82r9TG3Lbd3yghzpQaH2C) ya no se actualiza.

## Historias de Instagram (2 o 3 por semana)
- Formato 1080x1920, mismo estilo de marca. Deja libre una franja de unos 400 px en la parte baja (y 250 px arriba) para que Carol ponga el sticker de enlace o de encuesta.
- Tipos que rotan: (1) encuesta o pregunta a la comunidad ("¿Cuántos procesos llevas?", "¿Qué portal te saca más canas?"), con el texto "Responde aquí 👇" encima del espacio libre; (2) dato o fecha del calendario judicial de esa semana; (3) recordatorio de la publicación más fuerte de la semana ("Nuevo Reel 👉").
- Renderízalas como PNG con shot_slides cambiando el alto a 1920 (o con page() en un viewport 1080x1920). Súbelas al repo en AAAA-MM/historias/.
- No van a Metricool: los stickers de enlace y encuesta solo se ponen a mano en la app. Súbelas como assets al Centro de mando y crea en `piezas` un documento por historia con format "Historia · súbela tú", uuids [] y en caption qué sticker poner (por ejemplo: "Sticker de encuesta: Menos de 50 / Más de 50" o "Sticker de enlace: https://www.justibot.com.co/").
- En el resumen a Carol di qué día va cada historia.
- Recuérdale a Carol en el resumen: cada publicación nueva se comparte en historias el mismo día con el sticker de enlace.
