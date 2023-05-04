import math


## Problem 1

def find_pi_one(n):

    approx = 0
    for i in range(0, n+1):
        approx += 4*((-1)**i)/(2*i+1)

    return approx

## Problem 2

def find_pi_two(n):

    new_pi = 0
    i = 0
    while i < 1001:
        new_pi += 4*((-1)**i)/(2*i+1)
        i +=1
    return new_pi

## Problem 3

# Greatest common divisor using exhaustive search

#a)
def gcd_a(n, m):

    divisor = 1
    i = 1
    while i <= min(n, m):
        if n % i == 0 and m % i == 0:
            divisor = i
        i += 1
    return divisor

#b)
def gcd_b(n, m):

    divisor = min(n, m)
    while divisor > 0:
        if n % divisor == 0 and m % divisor == 0:
            return divisor
        divisor -= 1


##Problem 4 simplifying fractions
#
def simplify_fraction(n, m):

    gcd = gcd_b(n, m)
    num = n//gcd
    denom = m//gcd

    if num % denom == 0:
        print(num//denom)

    else:
        print(num , "/", denom, sep="")



## Problem 5 Sum more pi

def pi_digits(n):

    count = 1
    while True:
        if int(find_pi_one(count)*10**(n-1)) == int(math.pi*10**(n-1)):
             return count
        count += 1


## Problem 6 calendar

def next_day(y, m, d):

if __name__ == '__main__':

    print(gcd_a(6, 3))
    print(gcd_b(6, 3))

    simplify_fraction(6, 3)
    simplify_fraction(5, 10)


    print(pi_digits(2))
    print(find_pi_one(12))
    print(math.pi)

