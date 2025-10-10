# Tests

Esta carpeta contiene los tests del proyecto.

## Estructura

```
tests/
├── __init__.py
├── test_data/              # Tests para módulos de datos
│   ├── test_load.py
│   └── test_preprocess.py
├── test_models/            # Tests para modelos
│   └── test_classifiers.py
└── test_features/          # Tests para features
    └── test_extraction.py
```

## Ejecutar Tests

### Todos los tests
```bash
pytest
```

### Tests con cobertura
```bash
pytest --cov=src --cov-report=html
```

### Tests específicos
```bash
pytest tests/test_data/test_load.py
```

### Tests con output verbose
```bash
pytest -v
```

## Escribir Tests

### Convenciones
- Nombra archivos de test como `test_*.py`
- Nombra funciones de test como `test_*`
- Usa fixtures para datos de prueba reutilizables
- Mantén tests independientes y reproducibles

### Ejemplo
```python
import pytest
from src.data.load import load_data

def test_load_data():
    """Test que la función load_data carga datos correctamente"""
    data = load_data("test_file.csv")
    assert data is not None
    assert len(data) > 0
```

## Buenas Prácticas
- Escribe tests antes o junto con el código
- Apunta a una cobertura de al menos 80%
- Tests deben ser rápidos (usa mocks para operaciones lentas)
- Tests deben ser determinísticos
