"""This Python module will print a string on screen as many times as you want"""

def name(strign):

    def veces(num:int):
        assert type(strign) == str, "Solo puedes ingresar Strings"
        return strign*num

    return veces

closure = name("ala")
print(closure(3))

