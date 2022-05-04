"""Python Module to know if a number is prime"""

def es_primo(param1:int) -> bool:
    """Return False if the param1 isn't palindrome otherwise return True"""
    for i in range(2,param1):
        print(i)
        if param1 % i:
            return False
    return True