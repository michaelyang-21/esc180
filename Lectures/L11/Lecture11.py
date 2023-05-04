# Lecture 11
## 10/04/2022

my_input = input("Give me an integer:")
print("Your input twice: ", int(my_input) * 2)

#too terse, not readable
print("Your input twice:", int(input("Your input:")) * 2)

#heterogenous lists
# lists of with elements of different types
def f():
    return 42

L = [5, [1, 2], f]

L[2]() # 42
L[1][0] # 1
L[1][1] # 2
[5, 6, 7][1] #6

# slicing
res = L[1:4] # [L[1], L[2], L[3]]

res = []
for i in range(1, 4):
    L.append(L[i])

res = L[1:7:2]
res = []
for i in range(1, 7, 2):
    res.append(L[i])
