#!/usr/bin/env bash
# Guarda en git los ajustes de voz, subtítulos y sonido con los que se renderizaron los videos 04-07 aprobados,
# en la rama videos/shorts-05-07-nube (NO en main). Uso (Git Bash):  bash videos/guardar-ajustes-videos-04-07.sh
set -euo pipefail
cd "$(dirname "$0")/.."
[[ "$(git branch --show-current)" == "videos/shorts-05-07-nube" ]] || { echo "Primero: git checkout videos/shorts-05-07-nube"; exit 1; }
git add videos/voice4 videos/voice5 videos/voice6 videos/voice7 videos/audio4/cues.md videos/audio5/cues.md videos/audio6/cues.md videos/audio7/cues.md \
  videos/src/hijos/meta.json videos/src/hijos/subs.json videos/src/hijos/words.json videos/src/redes videos/src/accidente videos/src/aprendices \
  videos/producir-video.sh videos/videos.conf videos/guardar-ajustes-videos-04-07.sh
git commit -m "videos 04-07: tiempos de voz, subtítulos y cues de los renders finales aprobados; comando producir-video.sh"
git push origin videos/shorts-05-07-nube
echo "Listo: guardado y subido a la rama videos/shorts-05-07-nube."
