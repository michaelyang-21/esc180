# efficiency of algorithms

L = [6, 1, 20, 2, 15, 6]
e = 2
e in L

def find_i(L):
    # 1 op for len(L), 1 op for create range(len(L))
    for i in range(len(L)): # 1 op
        if L[i] == e:          # 1 op for L[i], 1 op L[i] == e, 1 op for the if
            return i # 1 op
    return -1        # 1 op

# In the worst case, for input of size n, what is the
# number of operation that find_i takes?
#
#
# 2 + 4*n operations

# On a particular computer, the runtime in the worst
# case for len(lL) == n is (2+4*n)*c, where c is
# sec/operation for the particular computer

# (2+4*n)*c < (2n+4n)*c = (6c)*n

# The worst_case runtime complexity of find_i(L, e) is O(n)
# n = len(L)
# The worst-case runtime of find_i will be proportional to n