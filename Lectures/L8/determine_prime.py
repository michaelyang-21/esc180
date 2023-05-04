def is_prime(n):
    '''Return True iff (if and only if) n is prime'''

    if n <= 1:
        return False
    if n == 2:
        return True

    # n % i == 0
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

