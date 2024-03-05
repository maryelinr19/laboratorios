import pandas as pd
import plotly.express as px

# Crear el DataFrame con los datos proporcionados
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con un boxplot utilizando Plotly
fig = px.box(df, x='materia', y='nota', title='Distribución de Notas de Estudiantes por Materia')
fig.show()

# Graficar la distribución de aprobados con un pie chart utilizando Plotly
aprobados = df['aprobado'].value_counts()
fig = px.pie(aprobados, names=aprobados.index, values=aprobados.values, title='Proporción de Estudiantes Aprobados y No Aprobados')
fig.show()
