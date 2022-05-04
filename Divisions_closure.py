"""This module will return the divions what we want it"""

def dividend(x):
    """this function will return the division of x and n where x is my divisor"""
    assert type(x) == int,"you should put a number"
    def divisor(n):
        assert type(n) == int,"you should put a number"
        return int(n/x)
    return divisor

##simple
# def make_division_by(n):
#    return lambda x: x/n



def run():
    division_by3 = dividend(3)
    print(division_by3(18))

    division_by5 = dividend(5)
    divide100 = division_by5(100)
    print(divide100)

    divison_by18 = dividend(18)
    print(divison_by18(54))

if __name__ == "__main__":
    run()