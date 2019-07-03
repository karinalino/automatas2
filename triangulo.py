#Nombre : triangulo.py
#Objetivo : Identifica el tipo de triangulo de acuerdo al valor de sus lados 
#math 
#Autor: karina susana alvarez lino
#Fecha : 01 de julio de 2019

#----------------------------------------------
#Funcion para identificar el tipo de triangulo
#----------------------------------------------

def identificar(l1,l2,l3):
    #Equilatero
    if(l1 == l2 and l1 == l3):
     print("El triangulo es equilatero: ",l1,",",l2,",",l3)
    elif(l1 == l2 or l1 == l3 or l2 == l3):
       print("El triangulo es isoseles: ",l1,",",l2,",",l3)
    elif(l1!=l2 or l1!=l3 or l3!=l2):
     print("El triangulo es escaleno: ",l1,",",l2,",",l3)

def calcularPerimetro(l1,l2,l3):
    perimetro=l1+l2+l3
    return perimetro
    
def main():
    print("--- Script para identificar triangulos ---")
    lado1=float(input("Introduce lado 1:"))
    lado2=float(input("Introduce lado 2:"))
    lado3=float(input("Introduce lado 3:"))
    # Invocar Funciòn
    identificar(lado1,lado2,lado3)
    print("El perimetro es: ",calcularPerimetro(l1,l2,l3))


if __name__ == "__main__":
  main()