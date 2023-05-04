def sum_list(L):
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])

# Total amount of time: *((n-1) + (n-2) + .... + 1) k*n(n-1) / 2

# O(n^2)

'''
[] -> 0
[3] -> 3 + 0
[2, 3] -> 2+3+0
[1, 2, 3] -> 1+(2+(3+0))

'''

def sum_list3(L, end_i):
    '''Return sum(L[:end_i])'''
    if end_i == 0:
        return 0
    return L[end_i-1] + sum_list3(L, end_i-1)


# [1, 2, 3], 0 -> 0
# [1, 2, 3], 1 -> 1
# [1, 2, 3], 2 -> 2+1
# [1, 2, 3], 3 -> 3+(2+1)