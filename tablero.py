from  LinkedList import LinkedList
from excepciones import *

class Tablero:
    def __init__(self, tamano:int):
        self.tamano = tamano
        self.inicio = None

    def crear(self, Flag=True):
        for i in range(self.tamano):
            linkedlist = LinkedList()

            if Flag:
                aux = linkedlist.agregar("[ ]")
                self.inicio = aux
                for j in range(self.tamano - 1):
                    linkedlist.agregar("[ ]")
                Flag = False
            else:
                linkedlist.agregarsup(linkedlist.agregar("[ ]"), aux)
                for j in range(self.tamano - 1):
                    aux = aux.der
                    linkedlist.agregarsup(linkedlist.agregar("[ ]"), aux)
                aux = linkedlist.head

    def mostrar(self):
        aux = self.inicio
        aux2 = aux.abajo
        for i in range(self.tamano):
            aux2 = aux.abajo
            total = ""
            for j in range(self.tamano):
                total += aux.valor
                aux = aux.der
            print(total)
            aux = aux2

    def buscar_nodo(self, fila, columna):
        if fila < self.tamano and columna < self.tamano:
            aux = self.inicio
            for _ in range(fila):
                aux = aux.abajo
            for _ in range(columna):
                aux = aux.der
            return aux
        else:
            raise FueraDeRango("Excede el rango")










