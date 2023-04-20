import random


from tablero import Tablero
from Alien import *
from Depredador import *
from excepciones import *

class juego:

    def __init__(self):
        self.alien = Alien()
        self.depredador = Depredador()
        self.inicio_tablero()
        self.inicio_alien()
        self.jugar()

    def inicio_tablero(self):
        try:
            self.tamano = int(input("Ingrese el tamaño del tablero:\n"))
            self.tablero = Tablero(self.tamano)
            self.head = self.tablero.inicio
            self.tablero.crear()
            self.inicio_depredador()
            self.inicio_puntos()
            self.tablero.mostrar()

        except ValueError:
            print("Ingrese números")
            self.inicio_tablero()


    def inicio_alien(self):
        try:
            fila = int(input("Ingrese el número de la fila:\n"))
            columna = int(input("Ingrese el número de la columna:\n"))
            if self.alien.iniciar_partida(self.tablero.buscar_nodo(fila, columna)):
                print("no se puede hacer este movimiento por bloqueo")
                self.inicio_alien()
            self.puntuacion()
            self.tablero.mostrar()

        except ValueError:
            print("Ingrese números")
            self.inicio_alien()
        except FueraDeRango:

            print("Ingrese números válidos")
            self.inicio_alien()

    def inicio_depredador(self):
        fila = random.randint(0,self.tamano - 1)
        columna = random.randint(0,self.tamano - 1)
        self.depredador.iniciar_partida(self.tablero.buscar_nodo(fila, columna))

    def inicio_puntos_mas(self):
        for i in range(self.tamano):
            while True:
                fila = random.randint(0, self.tamano - 1)
                columna = random.randint(0, self.tamano - 1)
                nodo = self.tablero.buscar_nodo(fila, columna)
                if nodo.valor == "[ ]":
                    nodo.valor = "[+]"
                    break
    def inicio_bloqueo(self):
        for i in range(self.tamano//2):
            while True:
                fila = random.randint(0, self.tamano - 1)
                columna = random.randint(0, self.tamano - 1)
                nodo = self.tablero.buscar_nodo(fila, columna)
                if nodo.valor == "[ ]":
                    nodo.valor = "[#]"
                    break

    def inicio_puntos_menos(self):
        for i in range(self.tamano):
            while True:
                fila = random.randint(0, self.tamano - 1)
                columna = random.randint(0, self.tamano - 1)
                nodo = self.tablero.buscar_nodo(fila, columna)
                if nodo.valor == "[ ]":
                    nodo.valor = "[-]"
                    break

    def inicio_puntos(self):
        self.inicio_puntos_mas()
        self.inicio_puntos_menos()
        self.inicio_bloqueo()

    def puntuacion(self):
        print(f"Alien: {self.alien.vida}------- depredador: {self.depredador.vida}")


    def jugar(self):
        jugador = 0
        stop = True
        while True:
            self.puntuacion()
            if jugador == 0:
                while True:
                    aux = self.depredador.movimiento_aleatorio()
                    if aux is None:
                        break
                    if aux is False:
                        print(" GANADOR ALIEN !!")
                        stop = False
                        break

                    elif aux == 0:
                        self.alien.disminuir_vida()
                        break
                jugador = 1
                self.tablero.mostrar()

            else:
                if self.alien_menu() is False:
                    break
                jugador = 0


    def alien_menu(self):
        resultado = self.alien.menu()
        print(resultado)

        if resultado is True:
            print("no se puede realizar este movimiento; ingrese un movimiento valido segun el tablero")
            self.alien.menu()
        if resultado is False:
            print(" GANADOR depredador !!")
            return False

        if resultado == "atacar":
            self.depredador.disminuir_vida()



