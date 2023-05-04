# MergeSort
# CPython's sort and sorted use TimSort

# [10, 2, 4, 15, 20, 1, 2, -1]

# 1. sort the first half
# 2. sort the second half
# 3. merge the two sorted halves

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    mid = len(L) // 2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

# runtime inside each call: k*len(L)
# number of calls is log(2n) + 1
# then the total runtime is O(nlogn)


def merge_inefficient(L1, L2):
    return sorted(L1 + L2)

# [5, 10, 12, 15]
# [4, 4.5, 7, 13]
# res: [4, 4.5, 5, 7, 10, 12, 13, 15]
def merge(L1, L2):
    '''Return a sorted version of L1 + L2
    assume L1 and >2 are sorted in non-increasing order'''
    i, j = 0, 0
    merged = []
    # currently looking at L1[i] and L2[j]
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    merged.extend(L1[i:])
    merged.extend(L2[j:])

    # In total, we'll append len(L1) + len(L2) elements to
    # merged, and the appends are taking up most of the runtime
    # so the runtime is O(len(L1) + len(L2))


