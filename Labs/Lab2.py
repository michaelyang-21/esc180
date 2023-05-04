#1

# def my_sqrt(x):
#     sqr = x**.5
#     return sqr
#
# def my_print_square(x):
#     print(x**2)
# if __name__ == "__main__":
#     res = my_sqrt(25)
#     res2 = my_print_square(25)
#     print(res2)

#2

def display_current_value():
    global current_value

    print("Current value:", current_value)



def add(to_add):

    global current_value

    global previous

    previous = current_value

    current_value += to_add



def mult(to_mult):

    global current_value

    global previous

    previous = current_value

    current_value *= to_mult



def div(to_div):

    # divide by zero will cause errors

    if (to_div == 0):

        print("Cannot divide by zero")

    else:

        global current_value

        global previous

        previous = current_value

        current_value /= to_div



def memory():

    global current_value

    global save

    save = current_value



def recall():

    global save

    global current_value

    current_value = save



def undo():

    global previous

    global current_value

    current_value, previous = previous, current_value



if __name__ == "__main__":

    print("Welcome to the calculator program.")



    current_value = 0

    previous = 0





    current_value = 25

    memory()

    div(0)

    display_current_value

    add(5) # current value: 30

    display_current_value()

    mult(2) # current value: 60

    display_current_value()

    undo() # current value: 30

    display_current_value()

    undo() # current value: 60

    display_current_value()

    undo() # current value: 30

    display_current_value()

    recall()

    display_current_value()
