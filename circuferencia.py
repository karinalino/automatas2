#Nombre : circuferencia.py
#Objetivo : calcula el area y diametro de una circuferencia e import 
#math 
#Autor: karina susana alvarez lino
#Fecha : 01 de julio de 2019

import math as mat
import os

#-----------------------------
#Funciòn para calcular area
#-----------------------------
def calculaArea(r):
    area=mat.pi*(mat.pow(r,2))
    return area

#-----------------------------
#Funciòn para calcular diametro
#-----------------------------
def calculaDiametro(d):
    diam= d * 2
    return diam


def main():
    ciclo = True
    while (ciclo == True):
        print("-- Script para calcular Area de circuferencia --")
        radio = float (input ("Introducce el valor del radio:"))
        #invocar un metodo
        print("El area es: ", calculaArea(radio))
        print("El diametro es: ",calculaDiametro(radio))

        resp = input("Otro Calculo (s/n)? ")
        if (resp == "S" or resp =="s"):
                ciclo = True 
        else:
                ciclo = False
        #Borrar 
        os.system("cls")        
    else:
        print("*** Fin del programa ***")

if __name__ == "__main__":
    main()