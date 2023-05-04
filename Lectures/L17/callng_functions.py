def f(x):
    x = 500

def fL(L):
    L = [500]

def fL2(L2):
    L2[0] = 600

if __name__ == '__main__':
    x = 600
    f(x) # equivalent to first going <local x> = <global x>
    L = [600]
    fL(L) 
    fL2(L) #equivalent to first going <local L2> = <global L>

# Local variables [fL2]
# Name          Address
# L2            @1040


# Global variables
# Name          Address
# L             @1040
# 
# x             @1000
# 
# 


# Memory
# Address          Value
# 1000             600
# 1020             500        
# 1040             [@1020]
# 1060             [@1020]
# 1080             '__name__'
# 1100              <function f>
