# CANTIDAD DE SEGUNDOS Y DE SU EQUIVALENTE EN SEMANAS, DÍAS, HORAS, MINUTOS Y SEGUNDOS 
# Autor: skop
# fecha: 23 de agosto 2022
# acción: Hallar la equivalencia de un numero de segundos en semanas, dias, horas, minutos y segundos.

#leer datos de entrada

numero= int(input('Ingresa la cantidad de los Segundos: '))

#proceso

segundos = (((numero % 604800) % 86400) % 3600) % 60
minutos = (((numero % 604800) % 86400) % 3600) // 60
horas = ((numero % 604800) % 86400) // 3600
dias = (numero % 604800) // 86400
semanas = numero // 604800


# mostrar resultado
print("Los segundos son:", segundos )
print("los minutos son:", minutos )
print("las horas son:", horas )
print("los dias son:", dias )
print("las semanas son:", semanas )