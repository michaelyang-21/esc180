# Recursion
# functions calling themselves as helper function

# Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, ...
# 1, 1
# fib(n) = fib(n-1) + fib(n-1)

def fib(n):
    '''Return the n-th Fibonacci number'''
    # base case
    if n <= 2:
        return 1

    return fib(n-1) + f(n-2)

# Three laws of reursion
# 1. To know the answer for larger inputs you must know the answer for smaller inputs
# 2. You can't push on a rope (must have a base case)

def minus1(n):
    if n == -20:
        return 0
    print(n)
    return 1 + minus(n-1)

minus1(5)

# minus(20) -> 0 # number of times minus1() was called, -1
#
# minus(-19) -> 1
# ...
# minus1(3)
#   |
# minus1(4)
#   |
# minus1(5) -> 5

def is_even(n):
    '''Return True iff n is even, False o/w
    Assume n >= 0
    '''
    if n == 0:
        return True

    return not is_even(n-1)

# is_even(0) -> True
#   |
# is_even(1) -> False
#   |
# is_even(2) -> True
#   |
# is_even(3) -> False

def is_even_while(n):
    i_is_even = True
    i = 0
    # i is_even is the status of i
    while i < n:
        i_is_even = not i_is_even
        i += 1
    return i_is_even

def is_even_while2(n):
    i_is_even = True
    i = n
    # i is_even is the status of i
    while i > 0:
        i_is_even = not i_is_even
        i -= 1
    return i_is_even

# print the elements of the list L one by one
# print L(0)
# print the rest of L
def print_list_forward(L):
    if len(L) == 0:
        return

    print(L[0])
    print_list_forward(L[1:]) # k*(n-1)

    #*((n-1) + (n-2) + ... +1) O(n^2)


print_list_forward([])      #

print_list_forward([7])     # print 7

print_list_forward([6, 7])  # print 6

print_list_forward([5, 6, 7]) # print 5

# [5, 6, 7]
# print [6, 7] backward
# print 5

def print_list_backward(L):
    if len(L) == 0:
        return

    print_list_backward(L[1:])
    print(L[0])

print_list_backward([])      #

print_list_backward([7])     # print 7

print_list_backward([6, 7])  # print 6

print_list_backward([5, 6, 7]) # print 5


