# Autor: skop
# fecha: 12 de Octubre del 2022
# acción: Hallar el porcentaje de alumnos aprobados y el número de desaprobados si se ingresa el número de alumnos y su nota final.

# Leer datos de entrada
nalumnos= int(input("ingrese el número de estudiantes: "))

# Proceso
cont=0
aprobados=0
desaprobados=0
# Estructura repetitiva para
for cont in range(1,nalumnos+1):
  notas=int(input("ingrese las notas: "))
  if(14<=notas<=20):
    aprobados=aprobados+1
    porcentaje= ((aprobados/nalumnos)*100)
  else:
    desaprobados=desaprobados+1
# Imprimir resultado
print(f"El porcentaje de los alumnos aprobados es del {porcentaje} % y el numero de alumnos desaprobados es {desaprobados}")