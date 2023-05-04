
a = "hello" # Place "hello" 
            # sets a to the address memory
            # where "hello" was place

# global variable table
# variable          address
# a                 @1060

print(id(a)) # the actual location in the memory table
                # of "hello"

b = "hel"
c = "lo"
d = b + c

print(id(a), id(d))


a = 500

L = [500, 501]
L1 = L
b = a

#for i in range(-10, 300):
    #print(i, id(i))

# aliasing: two variables referring to the same object
# in memory
# L and L1 are aliases of each other
L[1] = 500
print(L)
print(L1)

L1 = [501, 501]
print(L)
print(L1)


# global variable table
#  variable         address
#  a                @1040
#  L                @1080
#  L1               @1100
#  b                @1020

# memory table
# address           value
# 1000
# 1020              500
# 1040              501
# 1060                 "hello"
# 1080              [@1020, @1040]
# 1100              [@1040, @1040]