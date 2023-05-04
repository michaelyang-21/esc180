## Lecture 10
## 09/29/2022

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    k = 2
    sqrt_n = int(n**.5)
    while k <= sqrt_n:
        if n % k == 0:
            return False
        k += 1
    return True

def find_first_odd_prime(limit):
    for i in range(limit + 1):
        is_prime(i) and i %2 == 1:


if __name__ == '__main__':
    print(is_prime(150))
    print(is_prime(151))

    # find the first odd prime, but avoid an infinite
    # by just trying 0...100

    for i in range(101):
        if is_prime(i) and i % 2 == 1:
            break
    print(i)

