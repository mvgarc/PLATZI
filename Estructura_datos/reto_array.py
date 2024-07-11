import random
class Array:
    def __init__(self, size):
        self.size: size
        self.elements= []

    def populate(self, metodo="random", start=0, step=1):
        if metodo == "random":
            self.elements = [random.randint(0,100) for _ in range(self.size)]
        elif metodo == "sequential":
            self.elements = [start + step * i for i in range(self.size)]
        else:
            raise ValueError("El Metodo a aplicar debe de ser random o secuencial")
    def sum_elements(self):
        return sum(self.elements)
    
array = Array(10)
array.populate(metodo="random")
print("Array que contiene los números aleatorios:", array.elements)
print("Suma de los elementos del array:", array.sum_elements())

array.populate(metodo="sequential", star=1, step=1)
print("Array que contiene los números secuenciales:", array.elements)
print("Suma de los elementos del array:", array.sum_elements())