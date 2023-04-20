from Node import Node
from excepciones import *

class LinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, value):
        if self.head is None:
            self.head = Node(value)
            return self.head
        else:
            aux = self.head
            while True:
                if aux.der is None:
                    nodo = Node(value)
                    aux.der = nodo
                    nodo.izq = aux
                    return nodo
                aux = aux.der

    def agregarsup(self,nodo_actual:Node, Nodo:Node):
        nodo_actual.top = Nodo
        Nodo.abajo = nodo_actual




    def buscarPorIndice(self,indice,head_desco= None):
        contador = 0
        aux = head_desco
        while True:
            if aux.valor is None:
                raise NoExiste("no existe")
            if contador == indice:
                return aux
            else:
                contador += 1
                aux = aux.der


    def __repr__(self):
        mostrar = ""
        aux = self.head
        while True:
            if aux is None:
                return mostrar
            else:
                mostrar += str(aux.valor) + "->"
                aux = aux.der


