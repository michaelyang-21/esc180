# tuples tuples
# Life lists, but immutable

t = (1, 2, 3, 4)
print(t[1])

# Cannot change the contents of a tuple

t1 = ([1, 2], 3)
# t1[0] = 5 is not allowed
t1[0][1] = 5
print(t1)

t2 = (5, 6)
# unpacking a tuple
a, b, = t2

t3 = (1, 2, 3)
#a, b = t3 # error

# a, b = b, a # creating a tuple on the RHS, then unpacking it

def f():
    return 42, 43, 44

ret_t = f()
print(ret_t)