L = [1, 2, [4, 5], 6]
print(L[2])
print(L[2][1])

M = [[1, 2, 3, 4],           #5
     [1, 0, 1, 0],           #6
     [2, 2, 3, 5]]           #1
                             #2

def mult_M_v(M, v):
    res = []
    for row_i in range(len(M)):
        dot_pro = 0
        for col_i in range(len(M[0])):
            dot_pro += M[row_i][col_i] * v[col_i]
        res.append(dot_pro)
    
    return res
print(M[1])

print(M[2][1])

for row in M:
    print(row)

# Print the transpose of M

for col_i in range(len(M[0])):
    for row_i in range(len(M)):
        print(str(M[row_i][col_i]) + " ", end = "")
    print("")

print("hi", end = "")
print("hello")