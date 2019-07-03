#Nombre : factorial.py
#Objetivo : Factorial de un nùmero
#math 
#Autor: karina susana alvarez lino
#Fecha : 01 de julio de 2019

# Metodo recursivo
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Funcion principal
def main():
	num = int(input('Numero: '))
	print('El factorial es: ', str(factorial(num)))

if __name__ == '__main__':
	main()
