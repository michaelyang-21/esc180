"""The Credit Card Simulator

Author: Qiren(Michael) Yang.  Last modified: Oct. 9, 2022
"""

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
    """Returns whether the date1 is the same or later than date2"""

    #If month is later, then date is later
    if month1 > month2:
        return True
    #If months are equal
    elif month1 == month2:
        #compare dates
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
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE

        #add the most recent month.
        cur_balance_owing_intst += cur_balance_owing_recent

        # set new owing recent of month
        cur_balance_owing_recent = amount

    #If the difference in months is greater than 2
    elif (month - last_update_month) >= 2:
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE ** (month - last_update_month - 1)
        cur_balance_owing_recent = amount

    # Update dates
    last_update_day = day
    last_update_month = month
    last_country = last_country2
    last_country2 = country

def amount_owed(day, month):
    """Calculate the total amount owed up to the specific date
    If its earlier, return error

    If the months are later, then interest is calulated on months that are older than 2 months
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

    # if month is next month
    elif month - last_update_month == 1:
        #calculate interest first
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE

        # add to owing interest and reset recent owings
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0

    elif month - last_update_month >= 2:
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_intst *= MONTHLY_INTEREST_RATE ** (month - last_update_month - 1)
        cur_balance_owing_recent = 0

    #update dates
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

    # gets the total owed amount up to the pay date. Keeps owed values recent for other functions
    owed = amount_owed(day, month)
    # if payed is more than owed, reset everything to zero
    if amount >= owed:
        cur_balance_owing_intst = 0
        cur_balance_owing_recent = 0

    else:
        #pays the ones owing interest first
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

    purchase(77, 7, 1, "Hawaii")
    print("Now owing:", amount_owed(7, 1))   #77p

    purchase(88, 8, 2, "China")              #88p 77i
    print("Now owing:", amount_owed(8 ,2))   #165

    purchase(99, 6, 2, "Mexico")     #error 88p 77i
    # print("lasttransd:",last_trans_day)      #8

    print("Now owing:", amount_owed(10 ,2))  #88p 77i

    purchase(66, 7, 3, "China")     #error 0p 168.85i
    # print("Purcha", total_owed[0])
    # print("inte", total_owed[1])
    # print("lasttransd:",last_trans_day)      #10

    print("Now owing:", amount_owed(8 ,3))   #168.85
    # print(purchase(55, 15, 3, "Hawaii"))     #error
    # print("lasttransd:",last_trans_day)     #8

    print("Now owing:", amount_owed(18 ,3))  #168.85

    print("Now owing:", amount_owed(1 ,4))   #177.2925

    pay_bill(100, 7, 8)                      #115.5
    # print("Purcha", total_owed[0])
    # print("inte", total_owed[1])
    # print("lasttransd:",last_trans_day)
    print("Now owing:", amount_owed(7 ,8))