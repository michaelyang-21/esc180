L = [1, 50, 100, 150, 200, 500, 700, 800, 900, 1000]
e = 50
# Is e in the first half of L? Yes
# Is e in the first quater of L # Is e in the third quarter of L

# Keep track of low and high
# e must be in between L[low] and L[high]

# Binary search
# low = 0, high = 9, mid = 4
# high = 3, mid = 2
# high = 2, mid = 1


def find_i_binary(L, 2):
    '''Return the location of e in the sorted list L
    return None if e is not in L'''

    low = 0
    high = len(L) - 1
    while high - low >= 2:
        mid = (low + high)//2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else
            return mid

    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    else:
        return None

# Keep track of high - low
# high - low; n
#             n/2
#             n/4
#             ...
#             1
# Approx log2(n) iterations
# Complexity of binary search: O(log n)
