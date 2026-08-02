# Bitácora de Acompañamiento y Asistencia con Inteligencia Artificial

**Estudiante:** Mónica Chicaiza  
**Asignatura:** Econometría  
**Institución:** Universidad Técnica de Cotopaxi (UTC)  
**Proyecto:** Estimación de los Retornos a la Educación y Medición de la Brecha Salarial de Género en Ecuador mediante la Ecuación Minceriana (OLS)  

---

## 1. Alcance y Filosofía del Uso de IA
En el marco de las políticas de integridad académica, la utilización del asistente virtual se limitó de forma estricta a funciones de soporte técnico, revisión de la lógica econométrica, estructuración modular del código fuente en Python y diseño de la interfaz gráfica para la presentación web interactiva. Todo el criterio de selección metodológica, interpretación econométrica y diagnóstico de variables proviene de las directrices académicas del curso.

## 2. Registro Cronológico de Prompts y Soluciones

### Fase 1: Arquitectura de Entorno y Preprocesamiento de Variables Mincerianas
* **Consulta formulada:**  
  > *"Configura mis credenciales globales de Git a mi correo institucional monica.chicaiza9013@utc.edu.ec y ayuda a estructurar un script en Python que procese variables para la ecuación de Mincer (log de ingreso, años de educación, experiencia potencial y su término cuadrático, género y zona urbana)."*
* **Respuesta y Aplicación:**  
  Generación del entorno local y creación del módulo `src/01_procesamiento_datos.py`, asegurando la transformación matemática $experiencia = edad - escolaridad - 6$ y la escala del logaritmo del ingreso.

### Fase 2: Estimación Econométrica Mínimos Cuadrados Ordinarios (OLS)
* **Consulta formulada:**  
  > *"¿Cómo puedo comparar mediante la librería `statsmodels` dos modelos OLS: uno básico con educación y experiencia, y un modelo ampliado que evalúe la brecha salarial de género y su interacción con el nivel educativo?"*
* **Respuesta y Aplicación:**  
  Desarrollo del script `src/02_modelo_econometrico.py`. Se parametrizaron las pruebas de hipótesis ($F$-test), coeficientes ajustados ($R^2$ ajustado) y la exportación de resultados en formato JSON en la carpeta `outputs/`.

### Fase 3: Visualización de Curvas Salariales e Interfaz Web
* **Consulta formulada:**  
  > *"Escribe un script con Seaborn para graficar la forma cuadrática de la experiencia frente al salario y la brecha salarial por género. Diseña también una plantilla index.html moderna con Glassmorphism para publicar en Vercel."*
* **Respuesta y Aplicación:**  
  Construcción de `src/03_visualizacion.py` para la renderización de las imágenes `.png` y maquetación responsiva del dashboard `index.html` con soporte de gráficos dinámicos en Chart.js.

---

## 3. Matriz de Autonomía
| Módulo / Actividad | Nivel de Asistencia de IA | Validación Humana y Control |
| :--- | :---: | :--- |
| **Configuración Git/VS Code** | Técnica | Verificación de firma e identidad en GitHub |
| **Diseño del Dataset** | Asistida | Validación de rangos econométricos reales de ENEMDU |
| **Especificación OLS** | Lógica | Verificación de significancia estadística ($p$-valores) |
| **Dashboard Vercel** | Estética / HTML | Pruebas de usabilidad y renderizado responsivo |