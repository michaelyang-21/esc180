# We are given a list L that contains every integer
# between 1 and n, except that k is missing
# (so len(L) == n - 1)
# Want to efficiently find what k is

[1 3]

def missing_k(L):
    for k in range(1, len(L)+1):
        if k not in L:
            return k

# [1, 2, 3, 5, 6]
def missing_k_1(L):
    sorted_L = sorted(L)
    for i in range(1, len(L)):
        if L[i] - L[i-1] == 2:
            return i + 1


