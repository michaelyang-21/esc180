# Fermat's Last Theorem:
# There are no natural number soutions to the equation
# i^p + j^k = k^p for p > 2

# 1 <= i <= n, 1 <= j <= n, 1 <= k <= n
def fermat(p):
    n = 1
    #dovetailing
    while True:
        for i in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1
