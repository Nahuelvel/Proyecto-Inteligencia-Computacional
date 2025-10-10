# Guía Rápida de Inicio

Esta guía te ayudará a comenzar a trabajar en el proyecto rápidamente.

## 1. Clonar el Repositorio

```bash
git clone https://github.com/Nahuelvel/Proyecto-Inteligencia-Computacional.git
cd Proyecto-Inteligencia-Computacional
```

## 2. Configurar el Entorno

### Opción A: Usando venv (recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar el proyecto en modo desarrollo
pip install -e .
```

### Opción B: Usando conda
```bash
# Crear entorno conda
conda create -n proyecto-ic python=3.9
conda activate proyecto-ic

# Instalar dependencias
pip install -r requirements.txt
pip install -e .
```

## 3. Verificar la Instalación

```bash
# Verificar que el paquete se instaló correctamente
python -c "import src; print(src.__version__)"

# Ejecutar tests (cuando estén disponibles)
pytest
```

## 4. Comenzar a Trabajar

### Para desarrollo de código:
```bash
# Navega a la carpeta src
cd src

# Crea tus módulos aquí
```

### Para experimentación:
```bash
# Abre Jupyter
jupyter notebook

# Navega a la carpeta notebooks y crea un nuevo notebook
```

## 5. Flujo de Trabajo Git

```bash
# Crear una nueva rama para tu trabajo
git checkout -b feature/nombre-descriptivo

# Hacer cambios y commits
git add .
git commit -m "Descripción clara del cambio"

# Push de tu rama
git push origin feature/nombre-descriptivo

# Crear Pull Request en GitHub
```

## 6. Mantener tu Entorno Actualizado

```bash
# Actualizar repositorio
git pull origin main

# Actualizar dependencias
pip install -r requirements.txt --upgrade
```

## Recursos Adicionales

- [README principal](../README.md)
- [Guía de contribución](../CONTRIBUTING.md)
- [Changelog](../CHANGELOG.md)

## ¿Problemas?

Si encuentras problemas:
1. Revisa que tu versión de Python sea >= 3.8
2. Verifica que todas las dependencias se instalaron correctamente
3. Consulta los issues existentes en GitHub
4. Abre un nuevo issue si es necesario
