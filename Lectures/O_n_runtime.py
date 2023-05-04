
# The index of the max(L)
def find_max_i(L):
    cur_max = L[0] # the largest element so far
    cur_max_i = 0  #  the location of cur_max
    for i in range(1, len(L)):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i

def find_i(L, e):
    '''Return the index of e in L'''
    for i in range(len(L)):
        if L[i] == e:
            return i


# A simple form of a tight upper bound on the worst-case asymptotic runtime complexity

# For a list of size n, what is the runtime proportional to

# O(n), n = len(L)

# n = 1000, res = 0
# n = 100, r
def log10(n):
    '''Return log10(n), assuming it's an integer, for a float n'''
    res = 0.0

    # The loop runs log10(n) times
    while n > 1:
        n /= 10
        res += 1es = 1
# n = 10, res = 2
# n = 1, res = 3

    return res

# Complexity of log10: O(log n)

def quadratic(L):
    for i in range(len(L)):
        # Repeats len(L) // 2 times
        for j in range(len(L)//2):
            pass # runs len(L)*(len(L)//2) times
            # for n = len(L), this n^2/2

# Complexity: O(n^2)