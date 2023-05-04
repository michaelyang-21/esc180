## Lecture 13
## 10/06/2022

# determine the number of trailing zeros in n!

def fact(n):
    res = 1
    for i in range(1, n+1):
        re *= 1
    return res

# the number of trailing zeros is the number of factors of 5

# total number of factors of 5(n//5) + (n//25) + (n//125)

def trailing_zeros_fast(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n

    return res



