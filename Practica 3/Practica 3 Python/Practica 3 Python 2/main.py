class Cola:
    def __init__(self, n):
        self.arreglo = [0] * n  # Arreglo de longitud 'n'
        self.inicio = 0        
        self.fin = -1           
        self.n = n             
        self.contador = 0     

    def insert(self, e):
        if not self.isFull():
            self.fin = (self.fin + 1) % self.n  
            self.arreglo[self.fin] = e
            self.contador += 1
        else:
            print("Error: Cola llena (Overflow)")

    def remove(self):
        if not self.isEmpty():
            elemento = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n 
            self.contador -= 1
            return elemento
        else:
            print("Error: Cola vacía (Underflow)")
            return -1  

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        else:
            print("Error: Cola vacía")
            return -1

    def isEmpty(self):
        return self.contador == 0

    def isFull(self):
        return self.contador == self.n

    def size(self):
        return self.contador


# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola(3) 
    cola.insert(10)
    cola.insert(20)
    cola.insert(30)
    print("Frente actual:", cola.peek()) 
    print("Elemento removido:", cola.remove())  
    print("Nuevo frente:", cola.peek())  
    print("Tamaño actual:", cola.size())  