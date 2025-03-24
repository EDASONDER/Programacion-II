import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = sum((x - prom) ** 2 for x in self.numeros)
        return math.sqrt(suma_cuadrados / (len(self.numeros) - 1))

def main():
    numeros = []
    print("Ingrese 10 números:")
    for i in range(10):
        while True:
            try:
                numero = float(input(f"Número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")

    estadisticas = Estadisticas(numeros)
    prom = estadisticas.promedio()
    dev = estadisticas.desviacion()

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {dev:.5f}")

if __name__ == "__main__":
    main()