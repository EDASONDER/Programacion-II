from punto import Punto
from linea import Linea
from circulo import Circulo
import turtle

# Creando puntos
p1 = Punto(0, 0)
p2 = Punto(100, 100)

# Mostrando coordenadas
print(p1.coord_cartesianas())
print(p1.coord_polares())

# Inicializamos Turtle
t = turtle.Turtle()
screen = turtle.Screen()

# Creando y dibujando línea
linea = Linea(p1, p2)
print(linea)
linea.dibujaLinea(t)

# Creando y dibujando círculo
circulo = Circulo(p1, 141)
print(circulo)
circulo.dibujaCirculo(t)

# Mantenemos la ventana abierta hasta hacer clic
screen.exitonclick()
