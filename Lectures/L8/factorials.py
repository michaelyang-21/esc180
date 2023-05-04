# factorial

def fact(n):
    '''Return n! for the non-negtaive integer n'''
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

#want the number of trailing zeros in n!
def n_trailing_zeros(n):
    fact_n = fact(n)
    counter = 0

    # fact_n = 1000
    # counter = 0

    # 100
    # 1

    # 10
    # 2

    # 1
    # 3


    while fact_n % 10 == 0:
        fact_n //=10
        counter += 1
    return counter

if __name__ == '__main__':
    print(fact(50))
    print(n_trailing_zeros(150000))