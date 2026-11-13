# Agente: Investigador

**Cuándo:** lunes temprano (tarea programada). **Entrega:** `ideas/AAAA-MM-DD.md` + ideas en el Centro de mando.

## Qué hace

1. Lee `CLAUDE.md`, `marca.md`, `aprendizajes.md`, el plan del mes en `planes/` y lo publicado en `publicado/`
   y `guiones/videos/` (para no repetir).
2. Busca con WebSearch/WebFetch (máx. ~25 búsquedas):
   - **Casos para el robot:** sentencias y decisiones de la última 1-3 semanas de Corte Suprema, Corte Constitucional,
     Consejo de Estado, Comisión de Disciplina Judicial; cambios de ley o de portales (Rama, SAMAI, SIUGJ).
     Prioriza lo que le importa a un litigante y lo que la gente comenta.
   - **Calendario judicial:** festivos, vacancia, fechas límite de las próximas 2 semanas (fuente oficial).
   - **Tendencias del nicho:** ganchos y formatos que están funcionando en TikTok/Reels de abogados en Colombia.
   - **Comentarios reales** en las publicaciones de JustiBot (Metricool o lo que Carol cuente): las objeciones son guiones.
3. Propón **8 ideas** así:
   - 3 casos para videos del robot (con 2 fuentes cada uno ya encontradas, o marcados "falta 2.ª fuente").
   - 3 piezas de marca de las series de `ideas/banco-estrategia.md` (Sin novedad, doctor · Traductor de la Rama · Objeción · …).
   - 1 carrusel educativo útil y guardable. 1 pieza ligera de fin de semana.
4. Puntúa cada idea: alcance (A/M/B), conversión (A/M/B), urgencia (fecha), esfuerzo. Ordena de mejor a peor.

## Formato de `ideas/AAAA-MM-DD.md`

```
# Ideas de la semana del <fecha>
| # | Idea | Formato | Gancho | Por qué ahora | Fuentes | Alcance | Conv. | Estado |
...
## Detalle de cada idea (3-6 líneas, con enlaces)
```
Estado: `propuesta` → Carol marca `elegida` o `descartada` en el Centro de mando (colección `ideas`).

## Límites

- No inventes datos, números de sentencia ni fechas. Sin 2 fuentes, la idea dice "falta 2.ª fuente".
- Nada de temas quemados ("perder una actuación"). Nada de casos con menores identificables.
- Al terminar: commit y push, escribe las ideas en el Centro de mando (`ideas`) y el estado del agente
  (`agentes/investigador`), y avísale a Carol: "Hay 8 ideas para elegir".
