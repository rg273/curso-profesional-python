def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #Acciones adicionales que decoran

        print("Vamos a realizar un cálculo: ")

        funcion_parametro()

        #Acciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior


# Para llamar la función decoradora se usa el carácter "@" y a continuación el nombre de esta.
# Python entiende que la función adyacente hacia abajo es la función a decorar y la toma como parametro.

@funcion_decoradora
def suma():
    print(15+20)

suma()