from ast import arg
from datetime import datetime
from mimetypes import init
from random import randint, random

def decorador(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()        
        func(*args,**kwargs)
        print("rogelio acaba de ganar la loteria a las --",initial_time,"-- una cantidad de "+str(args))
    return wrapper

random= randint(0,10000)
let = randint(1,10)
@decorador
def loteria(param1,param2):
    return (param1 * param2)

loteria(random,let)