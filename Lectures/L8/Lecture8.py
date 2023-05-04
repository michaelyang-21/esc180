##Lecture 8
##09/27/2022

for i in range(5):  # up to, but not including 5
    print(i)

for i in range(1, 6):  # start at 1, go up to but not including 5
    print(i)

for i in range(2, 15, 3): # start at 2, go up to but not including 15, in steps of 3
    print(i)

for i in range(2, 16, 3):   # start at 2, , go up to but not including 16, in steps of 3

    print(i)

for i in range(18, 3, -3): # start at 18, go down to but not inluding 3, in steps of -3
    print(i)

def print_with_while(start, end, step):
    i = start
    if step > 0:
        while i < end:
            print(i)
            i += step # same as i = i + step
    elif step < 0:
        while i > end:
            print(i)
            i += step

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

# while condition: sign(i-end)* sign(step) < 0

def print_with_while(start, end, step):
    i = start
    while sign(i-end)*sign(step) < 0:
        print(i)
        i += step # same as i = i + step
