import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # --- Sobrecarga de operadores ---
    def __add__(self, other):
        """Suma de vectores: a + b."""
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __mul__(self, scalar):
        """Multiplicación por escalar: r * a."""
        return Vector3D(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )
    
    def __truediv__(self, scalar):
        """División por escalar: a / r."""
        return Vector3D(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar
        )
    
    # --- Operaciones vectoriales ---
    def longitud(self):
        """Calcula la longitud (módulo) del vector: |a|."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalizar(self):
        """Devuelve el vector normalizado: a / |a|."""
        return self / self.longitud()
    
    def producto_escalar(self, other):
        """Producto escalar: a · b."""
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )
    
    def producto_vectorial(self, other):
        """Producto vectorial: a × b."""
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    # --- Métodos adicionales ---
    def es_perpendicular(self, other):
        """Verifica si a es perpendicular a b (a · b = 0)."""
        return math.isclose(self.producto_escalar(other), 0.0)
    
    def proyeccion(self, other):
        """Proyección ortogonal de a sobre b: ((a · b) / |b|²) * b."""
        escalar = self.producto_escalar(other) / (other.longitud()**2)
        return other * escalar
    
    def __str__(self):
        """Representación del vector como cadena."""
        return f"({self.x}, {self.y}, {self.z})"

# --- Ejemplo de uso ---
if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    
    print("Vector a:", a)
    print("Vector b:", b)
    print("Suma a + b:", a + b)
    print("Multiplicación 2 * a:", a * 2)
    print("Longitud de a:", a.longitud())
    print("Vector a normalizado:", a.normalizar())
    print("Producto escalar a · b:", a.producto_escalar(b))
    print("Producto vectorial a × b:", a.producto_vectorial(b))
    print("¿Son perpendiculares a y b?", "Sí" if a.es_perpendicular(b) else "No")
    print("Proyección de a sobre b:", a.proyeccion(b))