#algoritmo de enumeracion exaustiva
#sacando la raiz cuadrada del numero pedido
def raiz():
    target = int(input("elige un numero:  "))
    num = 0

    while(num**2 < target):
        print(num)
        num+=1
        print(num)
    if num**2 !=target:
        print("el numero solicitado no tiene una raiz cuadrada exacta")
    else:
        print("la raiz del numero es ",num)

raiz()

#algoritmo de aproximacion
obejetivo = int(input("Ingresa un nro:  "))
numero = 0.0
epsilon = 0.1
paso = epsilon**2

while abs(numero**2 - obejetivo) >= epsilon:
    print(numero,"NENA, A TU COLA LE FALTA CREMA")
    numero += paso 
    print(numero)
 
