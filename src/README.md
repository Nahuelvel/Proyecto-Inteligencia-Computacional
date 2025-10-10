# Código Fuente

Esta carpeta contiene el código fuente principal del proyecto.

## Estructura Recomendada

```
src/
├── __init__.py              # Hace que src sea un paquete Python
├── data/                    # Módulos para carga y procesamiento de datos
│   ├── __init__.py
│   ├── load.py             # Funciones para cargar datos
│   └── preprocess.py       # Funciones de preprocesamiento
├── models/                  # Definiciones de modelos
│   ├── __init__.py
│   ├── classifiers.py      # Clasificadores personalizados
│   └── utils.py            # Utilidades para modelos
├── features/                # Ingeniería de características
│   ├── __init__.py
│   └── extraction.py       # Extracción de features
├── visualization/           # Funciones de visualización
│   ├── __init__.py
│   └── plots.py            # Gráficos y visualizaciones
└── utils/                   # Utilidades generales
    ├── __init__.py
    └── helpers.py          # Funciones auxiliares
```

## Convenciones

- Usa nombres descriptivos en inglés o español (pero sé consistente)
- Cada módulo debe tener docstrings claros
- Funciones deben ser pequeñas y hacer una sola cosa
- Usa type hints cuando sea posible
- Incluye tests para funciones críticas
