#Nombre : operaciones.py
#Objetivo : muestra como trabaja los metodos o funciones 
#en python
#Autor: karina susana alvarez lino
#Fecha : 29 de junio de 2019

#---------------------------------
#Funciòn para sumar dos enteros
#---------------------------------

def suma(num1, num2):
    return num1+num2

#---------------------------------
#Funciòn para restar dos enteros
#---------------------------------

def restar(num1, num2):
    return num1-num2

#---------------------------------
#Funciòn para multiplicar dos enteros
#---------------------------------

def multiplicar(num1, num2):
    return num1*num2

#---------------------------------
#Funciòn para dividir dos enteros
#---------------------------------

def dividir(num1, num2):
    return num1/num2

#---------------------------------
#Funciòn para comparar dos enteros
#---------------------------------

def comparar(num1, num2):
    if (num1> num2):
        print("El mayor es num1", num1)
    elif(num2> num1):
        print("El mayor es num2", num2)
    else:
        print("Los numeros son iguales: ",num1 ,",", num2)

#---------------------------------
#Funciòn para hacer un ciclo con for 
#---------------------------------

def cuenta(num1,num2):
        if(num2>=num1):
            for i in range(num1, num2+1): 
              print("Valir de i: ",i)

        if(num1>num2):
            for i in range(num1, num2-1,-1): 
              print("Valir de i: ",i)

#Funciòn main
def main():
    ciclo = True
    while (ciclo == True):
        print("---Operaciones Bàsicas con Enteros---")
        print("\n")
        n1 = int(input("Intrpduce primer nùmero: "))
        n2 = int(input("Introduce segundo nùmero:"))

        #Invocamos las funciones
        print("La suma es: ", str(suma(n1,n2)))
        print("La resta es: ", str(restar(n1,n2)))
        print("La multiplicaciòn es: ", str(multiplicar(n1,n2)))
        print("La diviciòn es: ", str(dividir(n1,n2)))
        comparar(n1,n2)
        cuenta(n1,n2)
        
        cad = input("Otro Calculo (s/n)? ")
        if (cad == "S" or cad =="s"):
            ciclo = True 
        else:
            ciclo = False 

if __name__ == "__main__":
        main()
    