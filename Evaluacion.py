## Evaluacion sobre Estimacion Puntal y por intervalo. Jesus Antequera y Adrian Amaya
## A pesar de buscar y buscar, no se pude completar por no poseer conocimiento en programacion
from math import sqrt, ceil

def buscar_z(confianza):
	if(confianza == 99):
		valor_z = 1.645
	elif(confianza == 95):
		valor_z = 1.96
	else:
		valor_z = 2.57
	return valor_z

def calcular_muestra_infinita():
	confianza = int(input("Utilizar una confianza de:\n 90 \n 95 \n 99 \n"))
	Z = buscar_z(confianza)
	S = float(input("Que valor de varianza se va a utilizar: "))
	d = float(input("Que valor de precision se va a utilizar: "))

	muestra = ceil(((pow(Z, 2) * S)/pow(d, 2)))

	print(f'El tamano de muestra es: {muestra}')

	return muestra

def calcular_muestra_finita():
	confianza = int(input("Utilizar una confianza de:\n 90 \n 95 \n 99 \n"))
	Z = buscar_z(confianza) 
	N = int(input("Ingrese el tamaño de la población: "))
	S = float(input("Que valor de varianza se va a utilizar: "))
	d = float(input("Que valor de precision se va a utilizar: "))

	muestra = ceil((N * (pow(Z, 2)) * S)/((pow(d, 2) * (N - 1)) + (pow(Z, 2) * S)))

	print(f'El tamano de muestra es: {muestra}')

	return muestra

def llenar_datos(muestra):
	datos = []
	for i in range(muestra):
		valor = int(input("Ingrese el valor para muestra: "))
		datos.insert(valor, -1)

	print("Estos son tus datos")
	print(datos)

	return datos

def inicio():
	print("Hola, bienvenido a la calculadora de estimacion")

	infinito = input("Trabajara con una muestra infinita? S/N: ")
	infinito.lower()	

	if(infinito == "s"):
		muestra = calcular_muestra_infinita()
	else:
		muestra = calcular_muestra_finita()

	datos = llenar_datos(muestra)

inicio()
