# Comandos de video (copia de referencia)

Los originales viven en el PC de Carol, en `C:\Users\carol\Justibot\videos\` (repo Justibot). Esta copia es para
que cualquier agente sepa qué hacen. Se corren en **Git Bash** en ese PC:

| Comando | Qué hace |
|---|---|
| `cd ~/Justibot/videos && bash producir-video.sh 08` | Voz de Gonzalo, música, render, unión, portada, revisión de calidad y archivos finales en `out/listos/` (≈5-10 min) |
| `bash producir-video.sh 08 unir` | Solo une imagen y sonido, portada y revisión (sin repetir voz ni render) |
| `bash guardar-ajustes-videos-04-07.sh` | Una sola vez: guarda en git los ajustes de los videos 04-07 en la rama `videos/shorts-05-07-nube` y la sube |

Para un video nuevo: su código en una rama `videos/short-NN-slug` y una línea en `videos.conf`.
Revisión: `out/qaNN/` (informe y hojas de contacto). Archivos para subir: `out/listos/justibot-NN-slug.mp4/.jpg`.
