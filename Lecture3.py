##Lecture 3
## 09/14/2022
import math

#Print solutions of ax^2+bs+c = 0

a = 1
b = -2
c = 1

disc = b**2 - 4*a*c

if disc > 0:
    r1 = (-b + math.sqrt(disc)) / (2*a)
    r2 = (-b - math.sqrt(disc)) / (2*a)
    print(r1, r2)
elif disc == 0:
    r = -b/(2*a)
    print(r)
else:
    print("no solution")


#literal: a value entered directly into the program
#25
#"hello"
5.6

#keywords: if else, literals, 25, "hello", identifiers:, a, print)

#string literals

"hello"
"45"
45
s = 'artsci\'s are "smart"'
print(s)
print("\\")

s = '''abc
def
ghi'''
# in general, don't use it because it is used as docstring
print(s)


# floating point numbers("floats")
# a* 2^b # a: mantissa, b: exponent

#
















