def find_i(L e):
    # 5 operations that are performed once: ->L, ->e, len(L), range(len(L)), return
    for i in range(len(L)): # increment the counter, put the result in i, access L[i], compare L[i] to e, execute the if
        if L[i] == e:   # assume L[i] is constant time (O(1))
            return 1
    return -1

# In the worst case, we take 5 + 5n operations for n = len(L)
#                           t(5 + 5n) secnds, where t is seconds/operation


# 1. Figure out a formula for the number of elementary operations that the functions takes, in the worst case

# 2. Simplify it


# A simple form of the upper-bound on the asymptotic worst-case runtime complexity of f, expressed in Big O notation
# O(n), n = len(L)

# 3 + 5n is proportional to n for large n
# t * (3 + 5n)      t: #seconds per operation on the particular computer, for the operation that takes the longest time


# f is O(g) "g grows at least as fast as f"
# lim_(n -> infty) f(n) / g(n) < infty

# 3 + 5n is O(3 + 5n)
# 3 + 5n is O(n)
# 3 + 5n is O(0.00000000001*n)
# 3 + 5n is O(0.00000000000000001*n^2) # technically correct (the best kind of correct)

