import math

class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a  # Vector a como lista [x, y, z]
        self.b = b  # Vector b como lista [x, y, z]
    
    # --- Métodos para perpendicularidad ---
    def perpendicular_1(self):
        """Verifica si |a + b| = |a - b|"""
        suma = [ai + bi for ai, bi in zip(self.a, self.b)]
        resta = [ai - bi for ai, bi in zip(self.a, self.b)]
        return "Sí" if math.isclose(self._magnitud(suma), self._magnitud(resta)) else "No"
    
    def perpendicular_2(self):
        """Verifica si |a - b| = |b - a|"""
        resta_ab = [ai - bi for ai, bi in zip(self.a, self.b)]
        resta_ba = [bi - ai for ai, bi in zip(self.a, self.b)]
        return "Sí" if math.isclose(self._magnitud(resta_ab), self._magnitud(resta_ba)) else "No"
    
    def perpendicular_3(self):
        """Verifica si a · b = 0 (definición clásica)"""
        return "Sí" if math.isclose(self._producto_punto(), 0.0) else "No"
    
    def perpendicular_4(self):
        """Verifica si |a + b|² = |a|² + |b|² (Teorema de Pitágoras)"""
        suma = [ai + bi for ai, bi in zip(self.a, self.b)]
        return "Sí" if math.isclose(
            self._magnitud(suma)**2,
            self._magnitud(self.a)**2 + self._magnitud(self.b)**2
        ) else "No"
    
    # --- Métodos para paralelismo ---
    def paralela_1(self):
        """Verifica si a = r * b para algún escalar r"""
        if all(bi == 0 for bi in self.b):  # Evitar división por cero
            return "No"
        ratios = [ai / bi for ai, bi in zip(self.a, self.b) if bi != 0]
        return "Sí" if all(math.isclose(r, ratios[0]) for r in ratios) else "No"
    
    def paralela_2(self):
        """Verifica si a × b = 0 (módulo del producto cruz)"""
        return "Sí" if math.isclose(self._producto_cruz(), 0.0) else "No"
    
    # --- Métodos para proyección y componente ---
    def proyeccion(self):
        """Calcula la proyección ortogonal de a sobre b: ((a·b) / |b|²) * b"""
        escalar = self._producto_punto() / (self._magnitud(self.b)**2)
        return [escalar * bi for bi in self.b]
    
    def componente(self):
        """Calcula el componente de a en la dirección de b: (a·b) / |b|"""
        return self._producto_punto() / self._magnitud(self.b)
    
    # --- Métodos auxiliares ---
    def _magnitud(self, vector):
        """Calcula la magnitud (norma) de un vector."""
        return math.sqrt(sum(vi**2 for vi in vector))
    
    def _producto_punto(self):
        """Calcula el producto punto a · b."""
        return sum(ai * bi for ai, bi in zip(self.a, self.b))
    
    def _producto_cruz(self):
        """Calcula el módulo del producto cruz (solo para R³)."""
        if len(self.a) != 3 or len(self.b) != 3:
            raise ValueError("Producto cruz solo válido en 3D.")
        cx = self.a[1] * self.b[2] - self.a[2] * self.b[1]
        cy = self.a[2] * self.b[0] - self.a[0] * self.b[2]
        cz = self.a[0] * self.b[1] - self.a[1] * self.b[0]
        return math.sqrt(cx**2 + cy**2 + cz**2)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    a = [1, 0, 0]
    b = [0, 1, 0]
    av = AlgebraVectorial(a, b)
    
    print("¿Son perpendiculares (|a+b|=|a-b|)?", av.perpendicular_1())  # Sí
    print("¿Son perpendiculares (a·b=0)?", av.perpendicular_3())        # Sí
    print("¿Son paralelos (a×b=0)?", av.paralela_2())                   # No
    print("Proyección de a sobre b:", av.proyeccion())                  # [0.0, 0.0, 0.0]
    print("Componente de a en b:", av.componente())                     # 0.0