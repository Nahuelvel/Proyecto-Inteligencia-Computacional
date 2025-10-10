from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="proyecto-inteligencia-computacional",
    version="0.1.0",
    author="Proyecto Inteligencia Computacional Contributors",
    description="Clasificadores con robustez a cambios de fase en las series de tiempo y curvas de luz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nahuelvel/Proyecto-Inteligencia-Computacional",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
