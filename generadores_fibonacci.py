def my_gen():
    """Un ejemplo de generadores"""
    print("Hello wolrd!")
    n = 0
    yield n
    
    print("Hello heaven!")
    n = 1
    yield n 

    print("Hello hell!")
    n = 2
    yield n
    
a = my_gen()

print(next(a))
print(next(a))
print(next(a))

#generator expression 

my_list=[0,1,4,7,9,10]

my_second_list =[x*2 for x in my_list]
print(my_second_list)

my_second_gen = (x*2 for x in my_list)

# Replicando fibonacci con iteradores pero ahora con generadores
from itertools import count
import time

def fibo_gen():
    n1 = 0
    n2 = 1
    count = 0
    while True:
        if count == 0:
            count +=1
            yield n1
        elif count ==1:
            count+=1
            yield n2
        else:
            n_aux = n1 + n2
            n1 = n2
            n2 = n_aux
            count+=1
            yield n2

for i in fibo_gen():
    print(i)
    time.sleep(1)
