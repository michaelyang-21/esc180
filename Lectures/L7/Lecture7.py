## Lecture 7
## 09/22/2022
5 / 2
4 / 2

# integer division
6//2

7//2

(.7) // 2
7 // (-2) # -4

# remainder ("modulo")

7 % 2 # == 1, because 2 * (7//2) + 1 = 7

2 * ((-7)//2) + (-7) % 2 # always seven

(-7)%2 # 1

7%(-2) # -1

## repeated computation ("loops")

# sets i to 0, 1, 2, 3, 4
for i in range(5):
    print(i)
    print(2*i)
    print("=========")


# want to compute a^b
# 1* a * a * a .... * a
# b times

def my_pow(a, b):
    '''Return a^b, b a non-negative integer'''

    res = 1
    # if b is 0, for i in range(0), it repeats 0 times so
    # for loop is skipped

    for i in range(b):
        res = res * a
    return res

# while loop

# while <cond>:
#   <block>

i = 0
while i < 5:
    print(i)
    i = i + 1

flag = True
# want to check if 3 < 5
while flag and 3 < 5:
    print("we're sure 3 < 5")
    flag = False


# equivalent to
if 3 < 5:
    print("we're sure 3 < 5")



if __name__ == '__main__':
    print(my_pow(2, 3))


# want to compute log10(n)
# 10^(log10(n)) = n

def my_log10(n):
    '''Return log10(n), n is an exact positive
    power of 10'''
    ans = 0
    cur_pow = 1
    while cur_pow < n:
        cur_pow = cur_pow * 10
        ans = ans + 1

    return ans

if __name__ == '__main__':
    my_log10(1000000)

