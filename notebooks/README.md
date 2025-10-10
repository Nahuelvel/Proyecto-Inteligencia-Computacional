# Notebooks

Esta carpeta contiene Jupyter notebooks para experimentación, análisis exploratorio y documentación de resultados.

## Estructura Recomendada

Nombra tus notebooks de forma descriptiva y usa un prefijo numérico para ordenarlos:

```
01_exploracion_datos.ipynb
02_preprocesamiento.ipynb
03_modelo_baseline.ipynb
04_modelo_avanzado.ipynb
05_evaluacion_resultados.ipynb
```

## Buenas Prácticas

1. **Limpieza**: Limpia los outputs antes de hacer commit (excepto si son importantes para documentación)
2. **Documentación**: Usa celdas markdown para explicar tu proceso de pensamiento
3. **Modularidad**: Si el código se vuelve complejo, considera moverlo a módulos en `src/`
4. **Reproducibilidad**: Fija las semillas aleatorias para resultados reproducibles
5. **Organización**: Mantén un notebook por tarea principal

## Convertir Notebooks a Scripts

Si un notebook contiene código que será reutilizado, conviértelo a un módulo Python:

```bash
jupyter nbconvert --to script notebook.ipynb
mv notebook.py ../src/
```
