## Lecture 4
## 09/15/2022
# multiple assignments

a, b = 5, 6

#swapping values
a, b = b, a

#doesn't work, just make a be equal to b
a = b
b = a

# how to swap variables without using multiple assignments or temporary variable

#using a temp variable
temp = b
b = a
a = temp

#another version (hint)
a = 5
b = 6
a = a + b
b = a - b
a = a - b

print(a)
print(b)
##
#functions

def print_plus_two(x):
    to_print = x+2
    print(to_print)

def print_plus_y(x, y):
    print(x+y)

#docstring
def pirate_print(s):
    ''' Print the piratified version of the string s'''
    return "Ahoy! " + s + "! Yarr!"

def multiply(x, y):
    prod = x * y
    return prod

def actually_plunder_grade():
    #use global can be used globally
    global grade
    grade = 67

if __name__ == '__main__':
    print_plus_two(2)
    print_plus_two(8)
    print_plus_y(5, 6)
    my_prod = multiply(3, 5)
    print(pirate_print("I love Praxis"))

    grade = 98
    actually_plunder_grade()
    print(grade)

print(print(2))
#return
#2 ; print(2)
#None ; inner print statement has no return value so None is returned

# local variables cannot be accessed outside of function








