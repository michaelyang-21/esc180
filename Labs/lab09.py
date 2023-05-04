## Q1
def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)

print(power(2, 4))

## Q2
def interleave(L1, L2):

    if len(L1) == 0:
        return []
    else:
        return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])
print(interleave([1, 2, 3], [1, 2, 3]))

## Q3
def reverse_rec(L):
    if len(L) == 2:
        return [L[1], L[0]]

    elif len(L) == 1:
        return L

    else:
        return [L[len(L) - 1]] + reverse_rec(L[1:len(L) - 1]) + [L[0]]

## Q4
print(reverse_rec([1, 2, 3, 4, 5, 6]))

def zigzag(L):
    if len(L) == 0:
        print("", end="")
    elif len(L) == 1:
       print(L[0], end=' ')
    else:
        zigzag(L[1:len(L) - 1])
        print(L[0], L[-1], end =' ')

zigzag([1, 2, 3, 4, 5])

## Q5
def is_balanced(s):
    paren_end = s.find(")")
    if paren_end == -1:
        return '(' not in s

    paren_start = s[:paren_end].rfind("(")

    if paren_start == -1:
        return False
    if paren_end < paren_start:
        return False

    return is_balanced(s[:paren_start] + s[paren_end + 1:])

print("")
print(is_balanced("(()(()))"))
print(is_balanced("(hello)"))

print(is_balanced("(well (I think), recursion works like that (as far as I know)"))