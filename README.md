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


## Explicación del código "dashboard_academico.py"

### Inserte titulo acá
