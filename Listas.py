#Nombre : Listas.py
#Objetivo : muestran el funcionamiento de las listas en python 
#Autor: karina susana alvarez lino
#Fecha : 02 de julio de 2019



lista = []

#---------------------------------------
#Funcion para agregar items a la lista
#---------------------------------------

def agregarItem(dato):
    lista.append(dato)

#---------------------------------------
#Funcion para borrar items a la lista
#---------------------------------------

def eliminarItem(dato):
    #Buscamos el item
    if (dato in lista):
     lista.remove(dato)
     print("Dato eliminado...")
    else:
        print("Item no existe en la lista ...")


#---------------------------------------
#Funcion para imprimir los elementos de la lista
#---------------------------------------

def imprimirLista():
    j=1
    for i in lista:
        print("Item: ",j,",",i)
        j=j+1
#Parte principal del programa 
def main():

    ciclo = True
    while ciclo ==True:
        print("---Script para Trabajar con Listas---")
        print("1.- Agregar Elementos a la lista")
        print("2.- Buscar un  Elementos en la lista")
        print("3.- Modificar un  Elementos en la lista")
        print("4.- Eliminar un  Elementos en la lista")
        print("5.- Imprimir la lista")
        print("6.- Salir de la aplicaciòn ")

        opc = int(input("Elija una opcion entre 1 y 6 :"))
        if(opc == 1):
            item = input("Introduce valor del elemento :")
            agregarItem(item)
        elif (opc == 2):
            print("")
        elif(opc == 3):
            print("")
        elif(opc == 4):
            print("")
        elif(opc == 5):
            imprimirLista()

        elif(opc == 6):
            print("** Fin del Programa **")
            ciclo=False

        else:
            print("Selecciona un entero entre 1 y 6 :")

if __name__ == "__main__":
 main()