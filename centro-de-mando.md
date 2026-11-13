# Centro de mando JustiBot

- **Página real:** https://claude.ai/artifact/NwSo9EKAAJEQm9ZyRW6SFH (slug `b1a9f8f6-8e9e-40ed-a44b-9af900b23258`)
- Maqueta aprobada: https://claude.ai/artifact/2jzSk8sq9i86jkN7iyHcAY
- Reemplaza al tablero viejo (https://claude.ai/artifact/L82r9TG3Lbd3yghzpQaH2C), que ya no se actualiza.
- Código fuente de la página: `herramientas/centro-de-mando/index.html` (se publica con publish_files sobre el mismo slug).

## Qué lee en vivo

- **Metricool** (con la cuenta de Carol): indicadores del periodo y del anterior, vistas por día y por red,
  publicaciones de la semana. TikTok: vistas por video (TKPO02 fecha, TKPO05 texto, TKPO07 vistas).
- **Registros y pagos:** pendiente de conectar Google Analytics (GA4 G-PJ9LZYFDRN).

## Base de datos del artefacto (lo que escriben los agentes)

Herramientas: `db_list`, `db_get`, `db_write` (con `ifVersion` en documentos que ya existen) y `upload_asset`
para vistas previas (JPG 540×960 o MP4 liviano `ffmpeg -vf scale=540:-2 -crf 28`; el archivo debe estar bajo /home/claude).

| Colección / documento | Campos | Quién escribe |
|---|---|---|
| `piezas/<id>` | `titulo`, `formato`, `redes`, `estado`, `fecha` (AAAA-MM-DD), `hora` ("6:30 p. m."), `uuids` (Metricool), `caption`, `preview {kind: "image"\|"video", src: "/_blob/<id>", poster}`, `archivo`, `aprobado`, `cambio`, `resultados` | Guionista, diseñador, productor, community manager. Carol: `aprobado`, `cambio` |
| `ideas/<AAAA-MM-DD>-<n>` | `titulo`, `formato`, `gancho`, `porque`, `fuentes`, `alcance` (A/M/B), `conversion`, `semana`, `orden`, `estado` (propuesta / elegida / descartada) | Investigador. Carol elige |
| `agentes/<id>` | `estado` (Listo / Trabajando / Te necesita / En espera / Error), `ahora`, `ultima` | Cada agente al terminar. ids: investigador, guionista, productor-video, disenador, community-manager, analista |
| `aprendizajes/<id>` | `orden`, `titulo`, `texto` (con el número y la fuente, y el próximo paso) | Analista |
| `plan/actual` | `mes`, `titulo`, `meta`, `texto`, `estado` (por aprobar / aprobado), `cambio` | Analista. Carol aprueba |
| `pedidos/<id>` | `texto`, `estado` (pendiente / hecho), `creado`, `respuesta` | Carol pide; el agente que lo atiende marca `hecho` y responde en una línea |

## Estados de una pieza

`idea elegida` → `guion por aprobar` → `guion aprobado` → `en producción` → `diseñada` / `listo para programar`
→ `por aprobar` (ya en Metricool como borrador) → `aprobado` → `programado` → `publicado`.

- "Aprobar" en la página: si la pieza tiene borradores en Metricool, los programa en ese momento
  (`updateScheduledPost` con `draft: false`) y deja `estado: "programado"`. Si Metricool falla, deja `aprobado: true`,
  `estado: "aprobado"` y `errorProgramar`: el community manager la programa en su revisión diaria.
- "Pedir cambio" guarda `cambio` y pone `aprobado: false`. El agente responsable lo atiende, borra `cambio`
  (`{"__delete__": true}`) y vuelve a dejar la pieza `por aprobar`.
