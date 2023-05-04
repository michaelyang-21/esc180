# sorting a list of floats
# [50, 0, 3, 2, 10, 100]
# [50, 0, 3, 2, 10, 100]
# [10, 0, 3, 2, 50, 100]
# [2, 0, 3, 10, 50, 100]
# [2, 0, 3, 10, 50, 100]
# [0, 2, 3, 10, 50, 100]

# Selection Sort
#
def max_i(L):
    '''Return the location of the maximum element in L'''
    cur_max = L[0]
    cur_max_i = 0
    for i in range(1, len(L)):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i

# runtime of max_i: O(n), n is the length of the input

def selection_sort(i):
    # n = len(L)
    for j in range(len(L)-1):           # k5 time
        ind_of_max = max_i(L[:(len(L) - j)]) # runtime is proportional to k*(n-j)
        end_max = len(L) - 1 - j # k3 time
        L[ind_of_max], L[end_max] = L[end_max], L[ind_of_max] # k4 time

    # Every line excpet line 26 : a total (k5+k3+k4)*(n-1)
    # The total for line 26:
    # (k1+k2)(n+(n-1)+(n-2) + ... + 1)

    # Total runtime ~ (k5+k3+k4)*(n-1) + 0.5(k1+k2)n + 0.5*(k1+k2)^n
    # O(n^2)

def max_i_j(L, last_ind1):
    cur_max = L[0]
    cur_max_i = 0
    for i in range(1, last_ind1):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i

# max_i_j is O(last_ind1)
#       the runtime is proportional to k1*last_ind

def selection_sort_faster(L):
    # n = len(L)
    for j in range(len(L)-1):           # k5 time
        ind_of_max = max_i(L, (len(L)-j)) # runtime is proportional to k*(n-j)
        end_max = len(L) - 1 - j # k3 time
        L[ind_of_max], L[end_max] = L[end_max], L[ind_of_max] # k4

    # Still O(n^2)
