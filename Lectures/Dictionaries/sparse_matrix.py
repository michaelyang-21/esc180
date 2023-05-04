# Sparse matrix

# [[1, 0, 0]                1     0 + 1*1
#  [5, 0, 2]]               2     0 + 2*3 + 5*1
#                           3
# dim = (2, 3)

L = [[0] * 5] * 4
L[0][0] = 1
print(L)

L = []
for i in range(4):
    L.append([0] * 5)

def mult_M_sparse_v(M, v, dim):
    res = [0] * dim[0]
    for coords, entry in M.items():
        v[coords[0]] += entry * v[coords[1]]



M = {(0, 0): 1, (1, 2): 2, (1, 0): 5}
print(M[(1, 2)])

print(M.items())

for coords, entry in M.items():
    print(coords, entry)

for k, v in M.items():
    print(k, v)