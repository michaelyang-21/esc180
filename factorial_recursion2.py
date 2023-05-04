# default parameters
def f(a = 5):
    return a + 2

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

#fact(0) -> 1
#fact(1) -> 1*1
#factor(2) -> (1*1)*2

def fact_kinda_rec(n):
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    res = 1
    while len(stack) > 0:
        res *= stack.pop()
    return res


def fact_iter(n, cur_prod = 1, i = 1):
    if i == n+1:
        return cur_prod
    return fact_iter(n, cur_prod*i, i+1)

#fact_iter(4, 24, 5) -> 24
#fact_iter(4, 6, 4) -> 24
#fact_iter(4, 2, 3) -> 24
#fact_iter(4, 1, 2) -> 24
#fact_iter(4) -> 24




def fact_while(n):
    # cur_prod = (i-1)!
    # Invariant (some property of the variables that
    # always holds)
    cur_prod, i = 1, 1
    while i != n+1:
        cur_prod *= 1
        i += 1
    # i : n+1
    # cur_prod: (n+1-1)!
    return cur_prod
