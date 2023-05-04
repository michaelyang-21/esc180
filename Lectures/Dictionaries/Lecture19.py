# Aliasing

L1 = [5, 6, 7]
L2 = L1

L2[1] = 42 # exactly the same as L1[1] = 42

L2 = [1, 2] # L1 stays the same

# Shallow copy
L1 = [5, 6, 7]
L2 = L1[:] # shorthand for L2 = [L1[0], L1[1], L1[2]]

L1[0] = 42 # L2 is unchanged

# Shallow copy
L1 = [[1, 2], [3, 4]]
L2 = L1[:]

L1[0][0] = 42 #changes both L1 and L2
L1[0] = 24 # changes only L1 not L2

# Deep copy
copy_L1 = []
for sublist in L1:
    copy_L1.append(sublist[:])

# Not deep copy
L1 = [[[1]]]
copy_L1 = []
for sublist in L1:
    copy_L1.append(sublist[:])

# Deep copy of a list of lists of lists of integers

L1 = [[[1]]]
copy_L1 = []

for sublist in L1:
    copy_sublist = []
    for subsublist in sublist:
        copy_sublist.append(subsublist[:])
    copy_L1.append(copy_sublist)

L1[0][0][0] = 50 # copy_L1[0][0][0] is unchanged

L = [[[[[[[[1]]]]]]], 50]

print("hello")

