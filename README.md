# Determinantes de los Ingresos Laborales y Brecha Salarial en Ecuador (Ecuación Minceriana)

Este repositorio contiene el código y artefactos del proyecto de Econometría enfocado en estimar y comparar los retornos a la educación y la brecha salarial de género mediante **Mínimos Cuadrados Ordinarios (OLS)** utilizando datos de la ENEMDU.

## 📁 Estructura del Proyecto

- `data/`: Dataset procesado (`enemdu_mincer_clean.csv`).
- `src/`: Scripts modulares en Python:
  - `01_procesamiento_datos.py`: Depuración y preparación del dataset Minceriano.
  - `02_modelo_econometrico.py`: Estimación OLS del Modelo Básico vs. Ampliado.
  - `03_visualizacion.py`: Gráficos de perfil experiencia-ingreso y brecha de género.
- `outputs/`: Coeficientes guardados en JSON y gráficos exportados.
- `prompts/`: Bitácora de registro de uso de Inteligencia Artificial (`registro_uso_ia.md`).
- `index.html`: Dashboard web interactivo para despliegue en Vercel.

## 👤 Autora
- **Mónica Chicaiza** - Universidad Técnica de Cotopaxi (UTC)