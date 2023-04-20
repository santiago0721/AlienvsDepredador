from Node import *

class Alien:
    def __init__(self):
        self.posicion = None
        self.personaje = "👽"
        self.vida: int = 50

    def iniciar_partida(self,nodo:Node):
        self.posicion = nodo
        if self.posDepredador(nodo):
            self.posicion.valor = "😡" + self.personaje
        else:
            self.posicion.valor = self.personaje
        self.puntos_vida(self.posicion)

    def finalizar_partida(self):
        if self.vida <= 0:
            return True
        return False

    def puntos_vida(self,aux):
        if aux.valor == "[+]":
            self.vida += 10
        elif aux.valor == "[-]":
            self.vida -= 10

    def posDepredador(self,pos):
        if pos.valor == "😡":
            self.vida -= 25
            return True
    def poscompartida(self):
        if self.posicion.valor == "😡"+ self.personaje:
            self.posicion.valor = "😡"
        else:
            self.posicion.valor = "[ ]"

    def movimiento_der(self):
        aux = self.posicion.der
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.der
        if self.posDepredador(aux):
            self.posicion.valor = "😡"+ self.personaje
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
        if self.posDepredador(aux):
            self.posicion.valor = "😡"+self.personaje
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False

    def movimiento_top(self):
        aux = self.posicion.top
        if aux is None:
            return True
        self.puntos_vida(aux)
        self.poscompartida()
        self.posicion = self.posicion.top
        if self.posDepredador(aux):
            self.posicion.valor = "😡"+self.personaje
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
        if self.posDepredador(aux):
            self.posicion.valor = "😡" + self.personaje
        else:
            self.posicion.valor = self.personaje
        if self.finalizar_partida():
            return False


    def disminuir_vida(self):
        self.vida -= 25

    def atacar(self):
        pass


    def menu(self):

        while True:
            print("""
            [1] derecha\n
            [2] izquierda\n
            [3] top\n
            [4] abajo\n
            """)

            x = input("ingrese el numero de la opcion que desea ")

            if x == "1":
                return self.movimiento_der()
            elif x == "2":
                return self.movimiento_izq()
            elif x == "3":
                return self.movimiento_top()
            elif x == "4":
                return self.movimiento_abajo()
            else:
                print("esta no es una opcion valida, ingrese un numero permitido")





