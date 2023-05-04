##Lecture 6
##09/21/2022
#object types
# int: short for integer, a whole number of unlimited size
# float: floating point number
# str: short of string
# function

def f():
    return 42

code = 180
"ESC" + str(code)
"ESC" + "code"

str(3.14)

print("ESC", 180, "H1")
print("ESC", 180, "H1", sep = "!!!")

#########################################3

float(4)
int(4.0)

int(4.7) # truncation: throwing away the fractional part
int(-4.7)

# if the float is positive, can use the following
# to round it:
a = 4.7
int(a + 0.5)

float("3.14")
int("5")
#int("3.14")

##naming conventions

# legal identifier name: anything that starts with a letter
# or an underscore _ and is composed of letters, digits
# and underscores

_asdfasdfasdfasdfsadf = 5 # legal

# pothole/snake case

num_courses_engsci = 6 # moral way of naming variable

## return statements

# f(x) = x^2
def f(x):
    return 42
    print("hi")
    return x**2

def artsie_math(arg1, arg2, op):
    '''Return arg1 <op> arg2 if op is "+" or "-",
    print an error message otherwise'''
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    else:
        print("This is too difficult for me :(")

def artsie_math2(arg1, arg2, op):
    if op != "+" and op != "-":
        print("This is too difficult for me :(")
        return

    if op == "+":
        return arg1 + arg2
    elif opreturn == "-":
        return arg1 - arg2


if __name__ == '__main__':
    # a = f(5)
    # print(a)

    res = artsie_math (3, 2, "+") # res: 5
    res = artsie_math(3, 2, "*") # prints an error message

    if res == None:
        print("artscis screwed up")
    else:
        print(res)























