import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Dashboard Académico', layout='wide')

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv('resumen_alumnos.csv')

df = cargar_datos()

st.title('📊 Dashboard de Rendimiento Académico')
st.markdown('Este dashboard permite visualizar el rendimiento de los alumnos a partir de métricas calculadas.')

# Filtros múltiples
col1, col2 = st.columns(2)
with col1:
    grupos = st.multiselect('Selecciona uno o más grupos:', options=sorted(df['grupo'].unique()), default=sorted(df['grupo'].unique()))
with col2:
    semestres = st.multiselect('Selecciona uno o más semestres:', options=sorted(df['semestre'].unique()), default=sorted(df['semestre'].unique()))

# Aplicar filtros múltiples
df_filtrado = df[df['grupo'].isin(grupos) & df['semestre'].isin(semestres)]

# Métricas generales
st.subheader('📌 Métricas Generales')
col1, col2, col3 = st.columns(3)
col1.metric("Promedio General", f"{df_filtrado['calificacion_promedio'].mean():.2f}")
col2.metric("Asistencia Promedio", f"{df_filtrado['asistencia_promedio'].mean():.2f}%")

# Nueva lógica: porcentaje de alumnos con promedio mayor o igual a 6
total_alumnos = len(df_filtrado)
alumnos_aprobados = len(df_filtrado[df_filtrado['calificacion_promedio'] >= 6])
tasa_aprobacion = (alumnos_aprobados / total_alumnos * 100) if total_alumnos > 0 else 0
col3.metric("Tasa de Aprobación", f"{tasa_aprobacion:.1f}%")

# Gráficos
st.subheader('📈 Distribuciones')

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(df_filtrado, x="calificacion_promedio", nbins=10, title="Distribución de Calificaciones")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(df_filtrado, x="asistencia_promedio", nbins=10, title="Distribución de Asistencia")
    st.plotly_chart(fig2, use_container_width=True)

# Rendimiento por categoría
st.subheader('🎯 Categoría de Rendimiento')
fig3 = px.pie(df_filtrado, names='rendimiento', title='Distribución por Categoría de Rendimiento')
st.plotly_chart(fig3, use_container_width=True)
