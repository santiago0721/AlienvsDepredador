import random

from Node import Node
from random import randint

class Depredador:
    def __init__(self):
        self.posicion = None
        self.personaje = "😡"
        self.vida: int = 50

    def puntos_vida(self,aux):
        if aux.valor == "[+]":
            self.vida += 10
        elif aux.valor == "[-]":
            self.vida -= 10

    def iniciar_partida(self, nodo: Node):
        self.posicion = nodo
        self.posicion.valor = self.personaje

    def finalizar_partida(self):
        if self.vida <= 0:
            return True
        return False

    def posAlien(self,pos):
        if pos.valor == "👽":
            return True
    def poscompartida(self):
        if self.posicion.valor == self.personaje + "👽":
            self.posicion.valor = "👽"
        else:
            self.posicion.valor = "[ ]"

    def movimiento_top(self):
        aux = self.posicion.top
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.top
        if self.posAlien(aux):
            self.posicion.valor = "👽" + self.personaje
            return 0
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False

    def movimiento_abajo(self):
        aux = self.posicion.abajo
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.abajo
        if self.posAlien(aux):
            self.posicion.valor = "👽" + self.personaje
            return 0
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False

    def movimiento_der(self):
        aux = self.posicion.der
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.der
        if self.posAlien(aux):
            self.posicion.valor = "👽" + self.personaje
            return 0
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False

    def movimiento_izq(self):
        aux = self.posicion.izq
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.izq
        if self.posAlien(aux):
            self.posicion.valor = "👽" + self.personaje
            return 0
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False

    def movimiento_diagonal1(self):     #izq-top
        try:
            aux = self.posicion.izq.top
            if aux is None:
                return True
            self.puntos_vida(aux)
            self.poscompartida()
            self.posicion = aux
            if self.posAlien(aux):
                self.posicion.valor = "👽" + self.personaje
                return 0
            else:
                self.posicion.valor = self.personaje
            if self.finalizar_partida():
                return False
        except:
            return True

    def movimiento_diagonal2(self):     #der-top
        try:
            aux = self.posicion.der.top
            if aux is None:
                return True
            self.puntos_vida(aux)
            self.poscompartida()
            self.posicion = aux
            if self.posAlien(aux):
                self.posicion.valor = "👽" + self.personaje
                return 0
            else:
                self.posicion.valor = self.personaje
            if self.finalizar_partida():
                return False
        except:
            return True

    def movimiento_diagonal3(self):   #izq-abajo
        try:
            aux = self.posicion.izq.abajo
            if aux is None:
                return True
            self.puntos_vida(aux)
            self.poscompartida()
            self.posicion = aux
            if self.posAlien(aux):
                self.posicion.valor = "👽" + self.personaje
                return 0
            else:
                self.posicion.valor = self.personaje
            if self.finalizar_partida():
                return False
        except:
            return True

    def movimiento_diagonal4(self):  #der-abajo
        try:
            aux = self.posicion.der.abajo
            if aux is None:
                return True
            self.puntos_vida(aux)
            self.poscompartida()
            self.posicion = aux
            if self.posAlien(aux):
                self.posicion.valor = "👽" + self.personaje
                return 0
            else:
                self.posicion.valor = self.personaje
            if self.finalizar_partida():
                return False
        except:
            return True

    def disminuir_vida(self):
        self.vida -= 10

    def movimiento_aleatorio(self):
        aleatorio = random.randint(0,7)
        if aleatorio == 0:
            return self.movimiento_der()
        elif aleatorio == 1:
            return self.movimiento_izq()
        elif aleatorio == 2:
            return self.movimiento_top()
        elif aleatorio == 3:
            return self.movimiento_abajo()
        elif aleatorio == 4:
            return self.movimiento_diagonal1()
        elif aleatorio == 5:
            return self.movimiento_diagonal2()
        elif aleatorio == 6:
            return self.movimiento_diagonal3()
        else:
            return  self.movimiento_diagonal4()