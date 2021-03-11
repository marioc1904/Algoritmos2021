import pandas as pd 
# punto 1 
pacientesTratadosMed = {}
pacientesTratadosMed ['Enero'] = 32121
pacientesTratadosMed ['Febrero'] = 14564
pacientesTratadosMed ['Marzo'] = 65465
pacientesTratadosMed ['Abril'] = 85202
pacientesTratadosMed ['Mayo'] = 93213
pacientesTratadosMed ['Junio'] = 100231
pacientesTratadosMed ['Julio'] = 120213
pacientesTratadosMed ['Agosto'] = 65421
pacientesTratadosMed ['Septiembre'] = 46546
pacientesTratadosMed ['Octubre'] = 46547
pacientesTratadosMed ['Noviembre'] = 84651
pacientesTratadosMed ['Diciembre'] = 140521

SeriesPacientesTratadosMed = pd.Series (pacientesTratadosMed)
print (SeriesPacientesTratadosMed)

# punto 2 

print(SeriesPacientesTratadosMed['Enero':'Abril'])
print(SeriesPacientesTratadosMed['Mayo':'Agosto'])
print(SeriesPacientesTratadosMed['Septiembre':'Diciembre'])

# punto 4 

MatrizEnfermedades = {
                        'Enfermedad General' : [32121,14564,65465,85202,93213,100231],
                        'COVID-19': [0,0,223,3453,4543,43643],
                        'Traumatismo': [6545,43243,67657,435435,345345,43543],
                        'Cáncer': [6541,4334,4323,34545,5454,7675]
}

dataFrameMatriz = pd.DataFrame(MatrizEnfermedades, index= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'])
print (dataFrameMatriz)

print(dataFrameMatriz['Traumatismo'] ['Enero': 'Marzo'])

# funcion filter 

EnfermedadGenMayor = lambda valor: valor >= 40000
listaEnfermedadGenMayor = list(filter(EnfermedadGenMayor, dataFrameMatriz ['Enfermedad General']))
print (listaEnfermedadGenMayor)

# funcion map 

MultiplicacionCancer = lambda multiplicar: multiplicar * 0.1
listaMultiplicacionCancer = list(map(MultiplicacionCancer, MatrizEnfermedades['Cáncer']))
print (listaMultiplicacionCancer)

# funcion reduce 
from functools import reduce 

SumaTraumatismo = lambda acumulador = 0, elemento = 0: acumulador + elemento
ResultadoTraumatismo = reduce (SumaTraumatismo, MatrizEnfermedades['Traumatismo'])
print(ResultadoTraumatismo)