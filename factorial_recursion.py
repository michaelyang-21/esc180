# recursion
# n! = 1^2*3...*(n-1)^n

# fact(n) = n*fact(n-1)
# 0! = 1

def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n

# fact(0)   -> 1
#   |
# fact(1)   -> 1*1
#   |
# fact(2)   -> ((1)*1)*2
#   |
# fact(3)   -> (((1)*1)*2)*3
#   |
# fact(4)   -> ((((1)*1)*2)*3)*4
