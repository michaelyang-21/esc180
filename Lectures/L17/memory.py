#1. If there is a new object on the RhS, put it in memory
# make the LHS refer to the new object in memory
# in the globals table

x = 500    # 500 goes in the memory table
L = [500, 501]

# @ 2. If the RHS is an existin object, simply copy
#   the address to which RHS referes to the LHS
#   in the globals table

L1 = L # L and L1 refer to the same addess, so changing
        # L[0] implies a change in L1[0]

# 3. Chaning the contents of a list changes the memory table

L[0] = 510 # L1[0] is differnt now as well
y = 502
L[0] = y
z = "hello"

# Global variables
# Name          Address
# x             @1000
# L             @1040
# L1            @1040
# y             @1060
# z             @1080


# Memory
# Address          Value
# 1000             500
# 1020             501
# 1040             [@1020, @1020]
# 1060             502
# 1080             "hello"