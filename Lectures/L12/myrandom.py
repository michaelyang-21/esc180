def myrandom():
    global x
    x = (a*x + b) % m
    return x / m



def initialize():
    global a, b, m, x
    a = 1664525
    b = 1013904223
    m = 2**32-1
    x = 1

def seed():


initialize()
