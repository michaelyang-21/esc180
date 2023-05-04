## Lists

earnings = [86, 63, 68, 59]
print(earnings[0])
print(earnings[2])
earnings[-1] # the same easnings[len(L) - 1]

len(earnings)

for e in earnings:
    print(e * 1.4)

def is_non_decreasing(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True
