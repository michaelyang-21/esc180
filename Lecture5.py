##Lecture 5
##09/20/2020

# globals table
# a: 25
#
#
# locals table
# x: 5
# res: 25
# Information into function: global variable
# Information out of function: modify global variable
#

def adjust_grade():
    global grade
    grade = grade + 5

# Information into function, passed via a parameter
# Information out of the function: via return

def adjust_grade2(g):
    return g + 5

def adjust_grade3(grade):
    grade = grade + 100
    return grade - 95


def f(x):
    global res
    res = x**2
    return res

def g():
    print(a)

if __name__ == '__main__':
    a = f(5)
    g()
    # print(a)
    # print(res)



















