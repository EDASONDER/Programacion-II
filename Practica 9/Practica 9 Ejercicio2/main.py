import tkinter as tk
from tkinter import ttk
import random
import math
from abc import ABC, abstractmethod

# Interfaz Coloreado
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self):
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color="sin color"):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Clase Cuadrado que implementa Coloreado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - Lado: {self.lado}, {super().__str__()}"

# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio, color="azul"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo - Radio: {self.radio}, {super().__str__()}"

# Funcion para generar 5 figuras aleatorias
def generar_figuras():
    figuras = []
    for _ in range(5):
        tipo = random.randint(1, 2)
        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio)
        figuras.append(figura)
    return figuras

# Funcion para mostrar los resultados
def mostrar_resultados(figuras):
    texto = ""
    for figura in figuras:
        texto += str(figura) + "\n"
        texto += f"Area: {figura.area():.2f}, Perimetro: {figura.perimetro():.2f}\n"
        if isinstance(figura, Coloreado):
            texto += f"Como colorear: {figura.comoColorear()}\n"
        texto += "-"*40 + "\n"
    return texto

# Funcion que se llama al hacer clic
def ejecutar():
    figuras = generar_figuras()
    resultado = mostrar_resultados(figuras)
    resultado_label.config(text=resultado)

# Interfaz grafica
ventana = tk.Tk()
ventana.title("Figuras Geometricas")

titulo = ttk.Label(ventana, text="Figuras Geometricas Aleatorias", font=("Arial", 14))
titulo.pack(pady=10)

boton = ttk.Button(ventana, text="Generar Figuras", command=ejecutar)
boton.pack()

resultado_label = ttk.Label(ventana, text="", justify="left", font=("Courier", 10))
resultado_label.pack(pady=10)

ventana.mainloop()
