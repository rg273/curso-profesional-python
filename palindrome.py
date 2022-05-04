"""Modulo para verificar si una palabra o texto es palindromo"""

def is_palidrome(param1: str) -> bool:
    """Retorna Falso o True si el param1 es palindromo"""
    param1 = param1.replace(" ","").lower()
    return param1 == param1[::-1]

def run():
    print(is_palidrome("2100"))


if __name__ == "__main__":
    run()