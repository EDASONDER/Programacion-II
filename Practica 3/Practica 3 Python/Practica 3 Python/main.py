class Pila:
    def __init__(self, n):
        self.arreglo = [0] * n 
        self.top = -1            
        self.n = n               

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("Error: Pila llena (Overflow)")

    def pop(self):
        if not self.isEmpty():
            elemento = self.arreglo[self.top]
            self.top -= 1
            return elemento
        else:
            print("Error: Pila vacía (Underflow)")
            return -1  

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.top]
        else:
            print("Error: Pila vacía")
            return -1  

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1


# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila(3)  
    pila.push(10)
    pila.push(20)
    pila.push(30)
    print("Tope actual:", pila.peek()) 
    print("Elemento eliminado:", pila.pop()) 
    print("Tope después de pop:", pila.peek())