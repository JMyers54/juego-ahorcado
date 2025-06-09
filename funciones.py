import random

class Funcion():
    def __init__(self):
        pass

    def palabrasAleatoria(self):
        self.palabras=["perro","marciano","codigo","casa"]
        self.palabrasAleatoria=random.choice(self.palabra)
        return self.palabrasAletoria

    def mostrarTablero(palabraSecerta, letraAdivinada):
        tablero=""
        for letra in palabraSecerta:
            if letra in letraAdivinada:
                tablero+=letra
            else:
                tablero+="_"
            print(tablero)

    def jugarAhoracado(self):
        self.palabraAleatoria=self.palabrasAleatoria()
        self.letraAdivinada=[]
        self.intentos_restantes=6
