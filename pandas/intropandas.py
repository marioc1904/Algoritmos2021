import pandas as pd 
listaVariada = ['a', 1, 2, 3, 4, 5]
print (listaVariada)
seriesPandas = pd.Series ([1,2,5])
print (seriesPandas)
seriesPandas = pd.Series ([1,2,'a'])
print (seriesPandas)
dicGanancias ={}
dicGanancias['Enero'] = 4300
dicGanancias['Febrero'] = 4243
dicGanancias['Marzo'] = 3248
dicGanancias['Abril'] = 3910
seriesGananciaspormes = pd.Series([4300,4243,3248,3910])
print (seriesGananciaspormes)

seriesGananciaspormesDic = pd.Series (dicGanancias)
print (seriesGananciaspormesDic)

print ('Enero', seriesGananciaspormesDic['Enero'])
print (seriesGananciaspormesDic['Enero':'Marzo'])

nombres = [['Juan', 'Karla'], ['Arturo', 'Laura']]
dataFramenombres = pd.DataFrame(nombres)
print (dataFramenombres)



matrizEstudiantes = { 
                        'Grupo1' : ['Karla', 'Mario', 'Laura'],
                        'Grupo2' :['Santi', 'Arturo', 'Vale'],
                        'Grupo3' :['Juan', 'Melany', 'Laura'],
                        'Grupo4' :['Mafer', 'Esteban', None],
                    }
dataFrameNombres = pd.DataFrame(matrizEstudiantes)
print (dataFrameNombres)
dataFrameNombresDic = pd.DataFrame(matrizEstudiantesDic)

print('#'*60)
print (dataFrameNombresDic)
print('#'*60)
print (dataFrameNombresDic['grupo1'])
print('#'*60)
print (dataFrameNombresDic['grupo2'])
print('#'*60)
print (dataFrameNombresDic)
print('#'*60)
print (dataFrameNombresDic.iloc[1:])

dicVentaspormes = {
    'Marzo' : [1234, 4235, 3920],
    'Abril' : [3920, 9493, 9995], 
    'Mayo' : [1930, 4905, 8573]
}
dataFrameVentas = pd.DataFrame(dicVentaspormes, index= ['tomates', 'yuca', 'papa'])
print(dataFrameVentas)