import calc


if __name__ == '__main__':

    calc.initialize()

    calc.add(42)

    if calc.get_current_value() == 42:

        print("Test 1 passed")

    else:

        print("Test 1 failed")



    calc.initialize()

    calc.add(2)

    calc.multiply(5)

    if calc.get_current_value() == 10:

        print("Test 1 passed")

    else:

        print("Test 1 failed")



    calc.initialize()

    calc.add(100)

    calc.divide(5)

    calc.subtract(6)

    if calc.get_current_value() == 10:

        print("Test 1 passed")

    else:

        print("Test 1 failed")

