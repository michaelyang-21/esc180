def halt(f, x):
    '''return True if f halts (doesn't loop infinitely) if given input x'''
    #...

def confused(f):
    if halt(f, f): # is f(f) an infinite loop?
        while True:
            pass
    else:
        return False

# confused(confused) is not false
# => confused(confused) produced an infinite loop
# => halt(confused ,confused) is True
# => confused(confused) does not produce an infinite loop
# Contradiction

# confused(confused) is False
# => halt(confused, confused) is False
# => confused(confused) produces an infinite loop
# => halt(confused, confused) is True

# The assumption that halt was possible to write is false

# The Halting Problem, Alan Turing

# Goedel's Incompleteness Theorem
# There are true mathematical statements that cannot be proven

# Assume every mathematical statements that's true can be proven
# => f halts x can either be proven or disproven
# => I can write halt()
# => contradiction

def halt(f, x):
    Generate all strings over te latin alphabet of length 1, 2, 3, 4 ...
    If s is a proof that f halts on x, return True
    Is s is a proof that f doesn't halt on x, return False