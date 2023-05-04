"""The Credit Card Simulator starter code
You should complete every incomplete function,
and add more functions and variables as needed.
Add comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Oct. 3, 2022
"""

# You should modify initialize()


def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global MONTHLY_INTEREST_RATE

    global card 
    card = True

    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0

    last_update_day, last_update_month = -1, -1

    last_country = None
    last_country2 = None

    MONTHLY_INTEREST_RATE = 1.05


def date_same_or_later(day1, month1, day2, month2):
    """Returns whether the date1 is the same or later than another date2"""
    if month1 > month2:
        return True
    elif month1 == month2:
        if day1 >= day2:
            return True
        else:
            return False
    else:
        return False

def all_three_different(c1, c2, c3):
    """Compare if 3 countries are equal"""
    if (c1 == None or c2 == None or c3 == None):
        return False
    if (c1 != c2 and c2 != c3 and c1 != c3):
        return True
    return False

def purchase(amount, day, month, country):
    """Makes a purchase if applicable
    Return "error" if the purchase date is before most recent date
    Also return "error" if card is disabled
    """
    global last_update_day
    global last_update_month

    global last_country
    global last_country2

    global cur_balance_owing_recent
    global cur_balance_owing_intst
    global card

    global MONTHLY_INTEREST_RATE

    # check if the card is disabled
    if card == False:
        return "error"

    # check of transaction date is later or same day and current day
    if date_same_or_later(day, month, last_update_day, last_update_month) == False:
        return "error"

    # check if 3 countries are the same. If same, then disable card
    if (all_three_different(last_country, last_country2, country)):
        card = False
        return "error"
    
    # if month is the same as the last update month, add amount to recent owing
    if month == last_update_month:
        cur_balance_owing_recent += amount
    
    # it is the next month
    elif (month - last_update_month) == 1:
        # increase interest on current owing with interest
        # 0 if its february
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE

        #add the most recent month. Total owing in january if its february
        cur_balance_owing_intst += cur_balance_owing_recent

        # set new owing recent of month
        cur_balance_owing_recent = amount
    
    elif month - last_update_month >= 2:
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE ** (month-last_update_month - 1)
        cur_balance_owing_recent = amount
    
    last_update_day = day
    last_update_month = month
    last_country = last_country2
    last_country2 = country

def amount_owed(day, month):
    """Calculate the total amount owed up to the specific date
    If its later, return error

    If the months are later, then interestis calulated on months that are older than 2 months
    """
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    global last_update_day
    global last_update_month
    global MONTHLY_INTEREST_RATE

    if date_same_or_later(day, month, last_update_day, last_update_month) == False:
        return "error"
    
    if month == last_update_month:
        pass
    
    elif month - last_update_month == 1:
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0

    elif month - last_update_month >= 2:
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE ** (month-last_update_month - 1)
        cur_balance_owing_recent = 0

    
    last_update_day = day
    last_update_month = month

    return cur_balance_owing_intst + cur_balance_owing_recent

def pay_bill(amount, day, month):
    global last_update_day
    global last_update_month
    global cur_balance_owing_intst
    global cur_balance_owing_recent

    if date_same_or_later(day, month, last_update_day, last_update_month) == False:
        return "error"
    
    owed = amount_owed(day, month)
    if amount >= owed:
        cur_balance_owing_intst = 0
        cur_balance_owing_recent = 0
    
    else:
        if amount > cur_balance_owing_intst:
            cur_balance_owing_recent -= (amount - cur_balance_owing_intst)
            cur_balance_owing_intst = 0
        else:
            cur_balance_owing_intst -= amount

    last_update_day = day
    last_update_month = month


# Initialize all global variables outside the main block.
initialize()

if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in
                                                #          a row)

    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375
                                                 # (43.65375*1.05+40)
    

    print("TEST CASE 5")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    pay_bill(97.24050000000001, 15, 6)
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))
