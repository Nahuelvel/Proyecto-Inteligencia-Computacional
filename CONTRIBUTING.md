# Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Esta guía te ayudará a entender cómo colaborar de manera efectiva.

## Código de Conducta
- Sé respetuoso con todos los colaboradores
- Acepta críticas constructivas
- Enfócate en lo mejor para el proyecto

## Cómo Contribuir

### Reportar Bugs
1. Verifica que el bug no haya sido reportado previamente en los Issues
2. Abre un nuevo Issue con una descripción clara del problema
3. Incluye:
   - Descripción del comportamiento esperado vs. el actual
   - Pasos para reproducir el problema
   - Versión de Python y dependencias utilizadas
   - Screenshots o logs si son relevantes

### Sugerir Mejoras
1. Abre un Issue describiendo la mejora propuesta
2. Explica por qué sería útil para el proyecto
3. Discute con el equipo antes de implementar cambios grandes

### Pull Requests

#### Proceso de desarrollo
1. **Fork y clona** el repositorio
   ```bash
   git clone https://github.com/Nahuelvel/Proyecto-Inteligencia-Computacional.git
   ```

2. **Crea una rama** para tu contribución
   ```bash
   git checkout -b feature/nombre-descriptivo
   # o para correcciones
   git checkout -b fix/nombre-descriptivo
   ```

3. **Realiza tus cambios**
   - Escribe código limpio y bien documentado
   - Sigue las convenciones de estilo del proyecto
   - Añade tests si es apropiado
   - Actualiza la documentación si es necesario

4. **Commits**
   - Haz commits pequeños y frecuentes
   - Usa mensajes descriptivos en español
   - Formato sugerido:
     ```
     Tipo: Descripción breve
     
     Descripción detallada si es necesaria
     ```
   - Tipos comunes: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

5. **Actualiza CHANGELOG.md**
   - Añade tus cambios en la sección "Unreleased"
   - Describe qué se agregó, cambió o corrigió

6. **Push y crea Pull Request**
   ```bash
   git push origin tu-rama
   ```
   - Crea un PR en GitHub con una descripción clara
   - Referencia issues relacionados con `#numero-issue`
   - Espera revisión del equipo

### Revisión de Código
- Todos los PRs requieren al menos una aprobación
- Responde a los comentarios de manera constructiva
- Realiza los cambios solicitados cuando sea necesario

## Estándares de Código

### Python
- Sigue PEP 8 para estilo de código
- Usa nombres descriptivos para variables y funciones
- Documenta funciones y clases con docstrings
- Mantén funciones pequeñas y enfocadas

### Jupyter Notebooks
- Incluye markdown explicativo entre celdas de código
- Limpia outputs antes de hacer commit (excepto si son importantes para la documentación)
- Nombra notebooks de forma descriptiva

### Documentación
- Documenta decisiones de diseño importantes
- Mantén el README actualizado
- Comenta código complejo o no intuitivo

## Estructura de Commits
Preferimos commits atómicos que:
- Resuelven un problema específico
- Tienen mensajes claros y descriptivos
- Son fáciles de revertir si es necesario

## Preguntas
Si tienes preguntas sobre cómo contribuir:
1. Revisa la documentación existente
2. Busca en Issues cerrados
3. Abre un nuevo Issue con tu pregunta

¡Gracias por contribuir al proyecto!
