# Project_Armageddon

## Explicación del Script "procesamiento_academico.py"
Este script en Python realiza un flujo completo de procesamiento de datos académicos de estudiantes, que incluye la carga, limpieza, integración, análisis y validación de información proveniente de múltiples fuentes.

### 📁 Archivos de Entrada
El script utiliza tres archivos CSV como entrada:

-Asistencias_corregidas.csv: Porcentajes de asistencia por alumno y materia.
-Calificaciones_corregidas.csv: Calificaciones por alumno y materia.
-Datos_demograficos.csv: Información demográfica de cada alumno (nombre, edad, sexo, grupo, semestre, etc.).

### ⚙️ Estructura del Proceso
El script se compone de 5 etapas principales:

1. Carga de Datos (cargar_datos)
-Lee los archivos CSV y los convierte en DataFrames de pandas.

2. Unificación de Datos (unificar_datos)
-Combina las tablas de asistencias, calificaciones y datos demográficos usando claves comunes como id_alumno y materia. Se emiten advertencias si hay valores nulos.

3. Limpieza de Datos (limpiar_datos)
-Elimina duplicados por alumno y materia.
-Normaliza nombres de materias.
-Valida rangos de asistencia (0-100%) y calificación (0-10).
-Informa sobre valores nulos o inconsistentes.

4. Cálculo de Métricas (calcular_metricas)
-Genera un resumen por alumno que incluye:
-Promedio de asistencia y calificaciones.
-Porcentaje de materias aprobadas.
-Clasificación de rendimiento (Excelente, Bueno, Aprobado, Reprobado).
-Indicador de asistencia adecuada (≥75%).

5. Validación de Datos (validar_datos)
Comprueba:
-Valores nulos por columna.
-Coherencia en número de materias por alumno.
-Rango válido de edades (15-19 años).
-Duplicados por alumno y materia.
-Estadísticas de distribución para asistencia y calificaciones.

6. Exportación de Resultados
-datos_unificados.csv: Datos completos, limpios y unificados.
-resumen_alumnos.csv: Métricas resumidas por alumno.


## Forma de utilización del script "procesamiento_academico.py"

### Requisitos
1. Entorno de trabajo en Google colab.
2. Script.
3. Los archivos .csv a utilizar con los nombres correspondientes.

### Procedimiento para uso.
1. Carga el script "procesamiento_academico.py" en una celda de código a Google Colab.
(Esto lo puedes hacer abriendo el script con bloc de notas y copiando el código directamente a la celda con Ctrl + V)
2. Sube los archivos requeridos al entorno de trabajo de Google Colab.
(En la barra de herramientas a tu izquierda de la pantalla tendras el icono de una carpeta, haz click en ella y dentro podrás cargar los archivos .csv que se procesaran con el script).
3. Ejecuta el Script.

Al final deberias tener 2 archivos más donde subiste los archivos .csv
Uno denominado como "datos_unificados.csv" y el otro como "datos_demograficos.csv".
Los dos archivos anteriores cuentan con la información ya procesada y lista para su uso.


## 📊 Explicación del código "dashboard_academico.py"

Este proyecto es un dashboard interactivo desarrollado con Streamlit, diseñado para visualizar el rendimiento académico de los estudiantes. Permite a los usuarios aplicar filtros, observar métricas clave y explorar gráficas dinámicas a partir de datos procesados.

### 🎯 Objetivo

Proveer una herramienta visual y accesible para analizar:
- Promedios de calificaciones
- Porcentajes de asistencia
- Tasa de materias aprobadas
- Categorías de rendimiento

### 📂 Estructura del Proyecto

- dashboard_academico.py: archivo principal que contiene el código del dashboard.
- resumen_alumnos.csv: archivo con los datos procesados (promedios, rendimiento, etc.).
- requirements.txt: archivo con las dependencias necesarias para ejecutar el proyecto.

### ▶️ Requisitos

Asegúrate de tener instalado:

- Python 3.11 (recomendado, evita 3.13 por problemas de compatibilidad)
- pip (gestor de paquetes)

### 📦 Instalación

1. Clona o descarga este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Instala las dependencias:
   pip install -r requirements.txt

### 🚀 Ejecución

1. Asegúrate de que el archivo resumen_alumnos.csv esté en la misma carpeta que el dashboard.
2. Ejecuta el dashboard con:
   streamlit run dashboard_academico.py
3. Se abrirá una ventana en tu navegador con la aplicación.

### 📊 Funcionalidades

- Filtros por grupo y semestre.
- Cálculo automático de:
  - Promedio general
  - Asistencia promedio
  - Tasa de aprobación
- Gráficos:
  - Histograma de calificaciones
  - Histograma de asistencia
  - Gráfico circular de categorías de rendimiento

### 🛠️ Tecnologías Usadas

- Streamlit
- Pandas
- Plotly

### 🧪 Datos de entrada esperados

El archivo resumen_alumnos.csv debe contener las siguientes columnas:

- id_alumno
- nombre
- grupo
- semestre
- calificacion_promedio
- asistencia_promedio
- porcentaje_aprobadas
- rendimiento

### 📌 Notas

- Si usas Python 3.13, puedes experimentar errores con algunas bibliotecas. Se recomienda usar Python 3.10 o 3.11.
- En caso de errores con DLLs o instalación, verifica que Python esté correctamente agregado al PATH.

### ✨ Autores

Proyecto desarrollado como parte de una práctica de análisis académico con enfoque en ETL, visualización de datos y desarrollo ágil por:
- Adam Rafael Calderon Godinez.
- Edwin Amitiel Montoya Aguilar.
