# Nivel 8.4
# Elaborar un algoritmo que permita ingresar el nombre de N estudiantes, determine el promedio de M notas,determine que alumno tiene el mayor promedio
# y que estudiante tiene el menor promedio.
# Autor: skop
# fecha: 26 de Octubre del 2022
# acción : Determinar el promedio de M notas y determine que alumno tiene el mayor promedio y que estudiante tiene el menor promedio. 

#Datos de Entrada
numero = int(input("Ingrese el numero de alumnos : ")) 
notas = int(input(f"Ingrese la cantidad de notas de los cursos:"))

#Proceso
Pmayor = 0
Pmenor = 20
for contE in range(1,numero+1):
    nombre = input(f"Ingrese el nombre del estudiante {contE}: ")
    print(f"El alumno llamado {nombre} ")
    contI=1
    suma=0
    while contI<=notas:
        nota=int(input(f"ingrese la nota {contI}: "))
        suma=suma+nota
        contI=contI+1
        promedio=suma/notas
    print(f"El alumno {contE} tiene un promedio de :",promedio)
    if(promedio>=Pmayor):
      Pmayor=promedio
    if(promedio<Pmenor):
      Pmenor= promedio
#Datos de Salida
print("El promedio mayor es del estudiante con la nota de", Pmayor)
print("El promedio menor es del estudiante con la nota de", Pmenor)
