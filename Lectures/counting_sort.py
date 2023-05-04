# Counting sort
# [1, 3, 2, 7, 3, 2, 1]

# counts
# 0 1 2 3 4 5 6 7
#   2 2 2
# [1, 1, 2, 2, 3, 3, 7]

def counting_sort(L):
    counts = [0] * (max(L)+1) # k1*max(K)
    for e in L:
        counts[e] += 1# K2*len(L)

    sorted_L = []
    for i in range(len(counts)):        # max(L) times. Total:k5*max(L)
        sorted_L.extend([i] * counts[i]) # k3*counts[i]

    # In total, we'll append len(L) elements to sorted_L
    # In total, this would take k3*len(L) time

    # total runtime: (1*max(L+c2*len(L)))
    # O(max(L) + len(L)

    L[:] = sorted_L