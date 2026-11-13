# El cerebro de contenido de JustiBot

Este repositorio es la **memoria única** del sistema de contenido de JustiBot. Toda sesión de Claude,
tarea programada o agente que trabaje en contenido de JustiBot empieza leyendo este archivo,
`marca.md` y la ficha de su agente en `agentes/`. Responde siempre a Carol en español claro, sin jerga.

## Reglas que no se negocian

1. **Nada se publica sin la aprobación de Carol.** Todo entra a Metricool como borrador (`draft: true`).
   Solo pasa a programado cuando Carol lo aprueba en el Centro de mando o lo dice en el chat.
2. **Cada dato de un caso real lleva 2 fuentes** (ideal: la providencia o el comunicado oficial + prensa seria).
   Si no se puede confirmar, no va.
3. **Solo funciones reales de JustiBot** (lista en `marca.md`). Nunca inventar.
4. **Nunca datos reales de clientes**, ni nombres de menores o víctimas.
5. Los videos se hacen **en el PC de Carol** (voz de Gonzalo), no en la nube ni en GitHub Actions.
6. En el repo `yesser352-hub/Justibot` **nunca push a `main`** (main = despliegue de la web). El código de cada
   video va en su rama `videos/short-NN-slug`.
7. Embajadores es **otra área, para después**: `embajadores/` solo guarda los datos; no se trabaja desde aquí
   salvo que Carol lo pida.

## Los 6 agentes

| Agente | Cuándo | Lee | Escribe | Ficha |
|---|---|---|---|---|
| Investigador | Lunes 7:41 a. m. (después del analista) | `aprendizajes.md`, `publicado/`, `ideas/banco-estrategia.md` | `ideas/AAAA-MM-DD.md` | `agentes/investigador.md` |
| Guionista y verificador | Martes 7:23 a. m. (ideas elegidas) | `ideas/`, `marca.md` | `guiones/` | `agentes/guionista.md` |
| Productor de video | Viernes 8:27 a. m.: prepara el código; Carol corre el comando en su PC | `guiones/` aprobados | `animados/listos/` | `agentes/productor-video.md` |
| Diseñador | Jueves 7:17 a. m. (y el domingo si faltan piezas) | `guiones/`, `marca.md`, `herramientas/` | `AAAA-MM/`, `piezas/` | `agentes/disenador.md` |
| Community manager | Domingo 8:35 a. m. + revisión diaria 8:43 a. m. | `piezas/`, `animados/listos/` | Metricool (borradores), `publicado/` | `agentes/community-manager.md` |
| Analista | Lunes 7:41 a. m. y día 26 de cada mes 7:53 a. m. | Metricool | `aprendizajes.md`, `planes/` | `agentes/analista.md` |

Tareas programadas (hora de Bogotá): «JustiBot · Lunes: analista e investigador», «JustiBot · Martes: guionista y verificador»,
«JustiBot · Jueves: diseñador», «JustiBot · Viernes: productor de video», «JustiBot · Domingo: community manager arma la semana»,
«JustiBot · Diario: aplicar aprobaciones», «JustiBot · Fin de mes: analista y plan del mes siguiente».

## Mapa del repositorio

| Carpeta / archivo | Qué guarda |
|---|---|
| `marca.md` | Tono, reglas visuales, lo que nunca se dice, datos confirmados del producto |
| `aprendizajes.md` | Lo que funcionó y lo que no, con números (lo actualiza el analista) |
| `ideas/` | Ideas de cada lunes y el banco de ideas de la estrategia |
| `guiones/` | Plantilla, verificación y guiones (videos del robot y piezas de marca) |
| `piezas/` | Estado de cada pieza en producción (`piezas/AAAA-MM-DD-slug.md`) |
| `publicado/` | Registro de lo que salió, con enlaces y resultados |
| `planes/` | Plan mensual para crecer entre abogados |
| `animados/listos/` · `animados/publicados/` | Videos del robot por programar y ya publicados (.mp4 + .jpg + .txt) |
| `AAAA-MM/` | Medios finales de reels, carruseles e historias por mes |
| `musica/` | 41 canciones libres y `CATALOGO.md` |
| `herramientas/` | `GUIA.md` (formatos y Metricool) y plantillas `build.py`, `add_music.py`, `slideshow.py` |
| `embajadores/` | Datos rescatados del tablero viejo (área aparte, para después) |
| `pendientes.md` | Lo que le toca a Carol fuera del flujo de contenido |

## Centro de mando

https://claude.ai/artifact/2jzSk8sq9i86jkN7iyHcAY es la maqueta aprobada. La versión real es el artefacto
"Centro de mando JustiBot" (enlace en `centro-de-mando.md`). Sus datos viven en la base de datos del
artefacto; cada agente actualiza ahí su estado al terminar (ver `centro-de-mando.md`).

## Al terminar cualquier trabajo

- Commit y push a `main` de este repo (este repo sí va a main), con la atribución que indique la sesión.
- Actualiza el Centro de mando (estado del agente y piezas).
- Avísale a Carol en 3-6 líneas qué hiciste y qué necesita de ella.
