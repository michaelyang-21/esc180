## Lecture 12
## 10/05/2022

L = [5, 6, 7, 19, 12, 15]

print(L[1:5:2])
print(L[:5:2])
print(L[::2])

print(L[::-1]) # the list in reverse

print(L[::-2])
L.insert(1, "hi")
# L = L.insert(1, "hello")
L.append(5)
L.insert(len(L), "end")
L.insert(0, "beginning")
print(L)

L = [5, 6, 7, 6, 8]
L.index(6)
L.index(6)
#L.index(99)
print("hi")

# e in L # True if e is equal to an element of L, False o/w
5 in L
99 in L

5 not in L
99 not in L # not (99 in L)

e = 5
if e in L:
    print("There is an element equal to", e, "in L")
else:
    print(e, "not found in L")

L = [6, 7, 8]
L.append(-1)

L2 = [8, 9]
L.extend(L2)

L = [6, 7, 8]
L2 = [8, 9]
L.append(L2)

def my_extend(L1, L2):
    for e in L2:
        L1.append(e)

L1 = [1, 2]
L2 = [3, 4]
my_extend(L1, L2)

L1 = [1, 2]
L2 = [1, 4, 5]
L3 = L1 + L2

L1 = L1 + L2
L1 += L2 # exactly the same as L1.extend(L2)

L = [5, 8, 10, 12]
L[1:2]= [10, 50]

L = [5, 8, 10, 12]
L.sort()
# L = L.sort() # L becomes None

L = [9, 0, 50, 52]
sorted_L = sorted(L) # L does not change, sorted_L is the
#sorted version of K

# lexicographic order - dictionary order

L = ["Zz", "abc", "123", "ABC"]
sorted(L, reverse=True)

#sorted(["a", 542]) error

