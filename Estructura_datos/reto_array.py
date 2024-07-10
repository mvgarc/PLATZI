import random
class Array:
    def __init__(self, size):
        self.size: size
        self.elements= []

    def populate(self, metodo="random", start=0, step=1):
        if metodo == "random":
            self.elements = [random.randint(0,100) for_ in range(self.size)]
        elif metodo == "sequential":
            self.elements = [start + step * i for i in range(self.size)]