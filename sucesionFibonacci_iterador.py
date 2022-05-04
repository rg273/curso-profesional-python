from itertools import count
from time import sleep
import time
class Fibonacci():
    def __init__(self,max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        self.limite = self.max
        return self

    def __next__(self):
        if self.count == 0:
            self.count+=1
            return self.n1
        elif self.count == 1:
            self.count +=1
            return self.n2
        try:
            self.aux = self.n1 + self.n2
            #   2         1           1
            self.n1=self.n2
            self.n2=self.aux
            self.count +=1
            if self.limite != None:
                if self.n2 > self.limite:
                    raise StopIteration("La secuencia ha llegado al limite solicitado")
        except StopIteration as st:
            print(st)
        else:
            return self.n2

#verificar si se paso
#lanzar error


ler = Fibonacci(38)
for elemento in ler:
    print(elemento)
    time.sleep(0.5)

my = [1,2,3,4,5]
iter = iter(my)

print(next(iter))