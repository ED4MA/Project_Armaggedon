
import pandas as pd
import numpy as np

# 1. Extracción de datos
def cargar_datos():
    # Cargar los archivos CSV
    asistencias = pd.read_csv('asistencias_corregidas.csv')
    calificaciones = pd.read_csv('calificaciones_corregidas.csv')
    demograficos = pd.read_csv('datos_demograficos.csv')

    return asistencias, calificaciones, demograficos

# 2. Unificación de datos
def unificar_datos(asistencias, calificaciones, demograficos):
    datos_completos = pd.merge(asistencias, calificaciones, 
                              on=['id_alumno', 'materia'], 
                              how='outer')

    if datos_completos.isnull().any().any():
        print("Advertencia: Hay valores nulos después de unir asistencias y calificaciones")

    datos_finales = pd.merge(datos_completos, demograficos,
                            on='id_alumno',
                            how='left')

    return datos_finales

# 3. Limpieza de datos
def limpiar_datos(df):
    duplicados = df.duplicated(subset=['id_alumno', 'materia']).sum()
    if duplicados > 0:
        print(f"Se encontraron {duplicados} registros duplicados. Eliminando...")
        df = df.drop_duplicates(subset=['id_alumno', 'materia'])

    nulos = df.isnull().sum()
    if nulos.any():
        print("Valores nulos encontrados:")
        print(nulos[nulos > 0])

    df['materia'] = df['materia'].str.capitalize()

    if ((df['asistencia_porcentaje'] < 0) | (df['asistencia_porcentaje'] > 100)).any():
        print("Advertencia: Hay valores de asistencia fuera del rango 0-100%")

    if ((df['calificacion'] < 0) | (df['calificacion'] > 10)).any():
        print("Advertencia: Hay calificaciones fuera del rango 0-10")

    return df

# 4. Cálculo de métricas
def calcular_metricas(df):
    resumen_alumnos = df.groupby('id_alumno').agg({
        'asistencia_porcentaje': 'mean',
        'calificacion': 'mean',
        'nombre': 'first',
        'sexo': 'first',
        'grupo': 'first',
        'semestre': 'first',
        'edad': 'first'
    }).rename(columns={
        'asistencia_porcentaje': 'asistencia_promedio',
        'calificacion': 'calificacion_promedio'
    }).reset_index()

    aprobadas = df[df['calificacion'] >= 6].groupby('id_alumno')['materia'].count()
    total_materias = df.groupby('id_alumno')['materia'].count()
    resumen_alumnos['porcentaje_aprobadas'] = (aprobadas / total_materias * 100).fillna(0)

    resumen_alumnos['asistencia_adecuada'] = resumen_alumnos['asistencia_promedio'] >= 75

    condiciones = [
        (resumen_alumnos['calificacion_promedio'] >= 8.5),
        (resumen_alumnos['calificacion_promedio'] >= 7),
        (resumen_alumnos['calificacion_promedio'] >= 6),
        (resumen_alumnos['calificacion_promedio'] < 6)
    ]
    categorias = ['Excelente', 'Bueno', 'Aprobado', 'Reprobado']
    resumen_alumnos['rendimiento'] = np.select(condiciones, categorias, default='Desconocido')

    return resumen_alumnos

# 5. Validación de datos
def validar_datos(df):
    print("\n=== Validación de Calidad de Datos ===")

    print("\n1. Completitud:")
    print(df.isnull().sum())

    print("\n2. Coherencia:")
    conteo_materias = df.groupby('id_alumno')['materia'].count()
    if not all(conteo_materias == 5):
        print("Advertencia: No todos los alumnos tienen 5 materias registradas")
        print(conteo_materias.value_counts())

    edades_validas = df['edad'].between(15, 19)
    if not edades_validas.all():
        print("Advertencia: Hay edades fuera del rango esperado (15-19)")
        print(df[~edades_validas]['id_alumno'].unique())

    print("\n3. Duplicados:")
    duplicados = df.duplicated(subset=['id_alumno', 'materia']).sum()
    print(f"Registros duplicados (mismo alumno y materia): {duplicados}")

    print("\n4. Valores atípicos:")
    print("Asistencia - Describe:")
    print(df['asistencia_porcentaje'].describe())
    print("\nCalificaciones - Describe:")
    print(df['calificacion'].describe())

# Función principal
def main():
    print("Cargando datos...")
    asistencias, calificaciones, demograficos = cargar_datos()

    print("\nUnificando datos...")
    datos_unificados = unificar_datos(asistencias, calificaciones, demograficos)

    print("\nLimpieza de datos...")
    datos_limpios = limpiar_datos(datos_unificados)

    print("\nCalculando métricas...")
    metricas = calcular_metricas(datos_limpios)

    validar_datos(datos_limpios)

    print("\nGuardando resultados...")
    datos_limpios.to_csv('datos_unificados.csv', index=False)
    metricas.to_csv('resumen_alumnos.csv', index=False)

    print("\nProceso completado. Archivos generados:")
    print("- datos_unificados.csv")
    print("- resumen_alumnos.csv")

    print("\nResumen de métricas:")
    print(metricas.describe())

    return datos_limpios, metricas

if __name__ == "__main__":
    datos, metricas = main()
