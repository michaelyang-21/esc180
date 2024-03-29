if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.

    # regular purchase (1 /month), pays back at beginning of next month
    
    print("TEST CASE 1")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 80.0
    pay_bill(80, 1, 2)
    purchase(80, 1, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 80.0
    pay_bill(80, 1, 3)
    purchase(80, 1, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 80.0

    # regular purchase (1 /month), pays half at beginning of next month
    print("TEST CASE 2")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 80.0
    pay_bill(40, 1, 2)  # 40
    purchase(80, 1, 2, "Canada")  # 120 (40 + 80)
    print("Now owing:", amount_owed(29, 2))  # 120.0 (40 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 122.0 (40*1.05+80 interest, 0 non-interest)
    pay_bill(40, 1, 3)  # 82.0 (82 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 162.0 (82 interest, 80 non-interest)
    print("Now owing:", amount_owed(31, 3))  # 162.0 (82 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 166.1 (86.1+80 interest, 0 non-interest)

    # regular purchase (2 /month), pays back at beginning of next month
    print("TEST CASE 3")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(160, 1, 2)
    purchase(80, 1, 2, "Canada")
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 160.0
    pay_bill(160, 1, 3)
    purchase(80, 1, 3, "Canada")
    purchase(80, 2, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 160.0

    # regular purchase (2 /month), pays half at beginning of next month
    print("TEST CASE 4")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # buy once, pay in june in full, check in december
    print("TEST CASE 5")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    pay_bill(97.24050000000001, 15, 6)
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))

    # buy once, pay in june in partial, check in december
    print("TEST CASE 6")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    pay_bill(10, 15, 6)  # 87.2405 remaining
    print("Now owing:", amount_owed(15, 6))  # 87.2405->91.602525(july)->96.18265125->100.9917838125->106.0413730031->
    print("Now owing:", amount_owed(31, 12))  # 111.3434416533 in november -> 116.9106137359 in december

    # buy once, buy again in early june, pay in june in full for jan debt+interest, check in december
    print("TEST CASE 7")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(97.2405, 15, 6)  # 80 new debt remaining
    print("Now owing:", amount_owed(15, 6))  # 80
    print("Now owing:", amount_owed(31, 12))  # 80->80->84->88.2->92.61->97.2405->102.102525

    # buy once, buy again in early june, pay in june (slightly more than jan debt+interest), check in december
    print("TEST CASE 8")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(100, 15, 6)  # 77.2405 (all new debt) remaining
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))  # 77.2405->77.2405->81.102525->85.15765125
    # ->89.4155338125->93.8863105031->98.5806260283 (at dec)

    # buy once, buy again in early june, pay in june (slightly less than jan debt+interest), check in december
    print("TEST CASE 9")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(90, 15, 6)  # 87.2405 remaining (7.2405 old debt)
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))  # 80+7.2405(june)->80+7.602525 (87.602525)->91.98265125->96.5817838125
    # ->101.4108730031->106.4814166533->111.805487486

    # buy once, forget about the card
    print("TEST CASE 10")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 12))  # 80->80(feb)->(80*1.05^10)(dec)130.3115701422

    # buy once, pay back immediately forget about the card
    print("TEST CASE 11")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    pay_bill(80, 1, 1)
    print("Now owing:", amount_owed(31, 12))  # 0

    # TEST 4 but with alternating 2 countries
    print("TEST CASE 12")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "France")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "France")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "France")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # TEST 4 but with alternating 3 countries
    print("TEST CASE 13")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "France")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80 interest building debt
    purchase(80, 1, 2, "China")  # FRAUD - ERROR, still 80
    purchase(80, 2, 2, "France")  # ALREADY FRAUD - ERROR, still 80
    print("Now owing:", amount_owed(29, 2))  # 80 (80 interest, 0 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 84.0 (84 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 4.0 (4 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # ALREADY FRAUD - ERROR, still 4
    purchase(80, 2, 3, "France")  # ALREADY FRAUD - ERROR, still 4
    print("Now owing:", amount_owed(31, 3))  # 4.0 (4 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 4.2 (4.2 interest, 0 non-interest)

    # TEST 4 but with same country -> then 2 other countries
    print("TEST CASE 14")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "France")  # FRAUD, STILL 244 (164 interest, 80 non-interest)
    print("Now owing:", amount_owed(31, 3))  # 244 (164 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 252.2 (164*1.05+80 interest, 0 non-interest)

    # TEST 4 but with 3 countries, but each country purchase twice
    print("TEST CASE 15")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "France")  # 160 (80 + 80)
    purchase(80, 2, 2, "France")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "China")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # Fraud early on, but don't pay back
    print("TEST CASE 16")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 1, "France")
    purchase(30, 2, 1, "Germany")
    purchase(30, 3, 1, "Germany")
    print("Now owing:", amount_owed(31, 1))  # 130.0
    print("Now owing:", amount_owed(31, 2))  # 130.0
    print("Now owing:", amount_owed(31, 3))  # 130*1.05
    print("Now owing:", amount_owed(31, 12))  # 130*1.05**10=211.7563014811

    # Fraud early on, but pay back
    print("TEST CASE 17")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 1, "France")
    purchase(30, 2, 1, "Germany")
    purchase(30, 3, 1, "Germany")
    pay_bill(130, 3, 1)
    print("Now owing:", amount_owed(31, 1))  # 0
    print("Now owing:", amount_owed(31, 2))  # 0
    print("Now owing:", amount_owed(31, 3))  # 0
    print("Now owing:", amount_owed(31, 12))  # 0

    # Fraud early on, but pay back
    print("TEST CASE 18")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 2, "France")
    pay_bill(90, 3, 2)  # now owe 40 non interest
    purchase(30, 3, 3, "Germany")
    purchase(30, 4, 4, "Germany")
    print("Now owing:", amount_owed(31, 3))  # 40 interested money
    print("Now owing:", amount_owed(31, 12))  # 40*1.05**9


    print("TEST CASE 19")
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

    print("TEST CASE 20")
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))
    purchase(80, 8, 1, "Canada")
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(6, 3))
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))
    print("Now owing:", amount_owed(7, 4))
    print("Now owing:", amount_owed(1, 5))
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))
    print(purchase(50, 3, 5, "United States"))
    purchase(150, 3, 5, "Canada")
    print("Now owing:", amount_owed(1, 6))

    
    print("TEST CASE 21")
    initialize()
    purchase(80, 8, 1, "Canada")
    purchase(80, 7, 1, "France")
    purchase(80, 8, 2, "United States")
    purchase(180, 8, 7, "Canada")
    print("Now Owing:", amount_owed(9, 10))

    
    print("TEST CASE 22")
    initialize()
    purchase(100, 15, 12, "France")
    purchase(10, 1, 11, "Portugol")
    pay_bill(50, 16, 12)
    pay_bill(50, 15, 12)
    print("Now owing:", amount_owed(30, 12))

    
    print("TEST CASE 23")
    initialize()
    purchase(110, 1, 1, "France")
    purchase(30, 30, 1, "Portugol")
    purchase(30, 1, 2, "France")
    pay_bill(30, 10, 2)
    purchase(60, 4, 3, "France")
    purchase(100, 5, 4, "Canada")
    purchase(12, 4, 4, "Portugol")
    pay_bill(40, 1, 6)
    pay_bill(50, 1, 7)
    print("Now Owing:", amount_owed(12, 12))

    
    print("TEST CASE 24")
    initialize()
    purchase(110, 1, 1, "France")
    pay_bill(110, 1, 1)
    purchase(135, 2, 3, "Mexico")
    pay_bill(123, 3, 4)
    purchase(12, 5, 6, "KFC")
    pay_bill(12, 7, 8)
    purchase(10000000000, 7, 8, "Switzerland")
    print("Now Owing:", amount_owed(8, 8))

    
    print("TEST CASE 25")
    initialize()
    purchase(1232, 1, 1, "Pancakes")
    purchase(182, 30, 1, "Panama")
    pay_bill(1414, 1, 3)
    purchase(12, 10, 3, "Pancakes")
    purchase(100, 1, 4, "Somewhere")
    pay_bill(20, 1, 3)
    purchase(10000000, 3, 4, 'Panama')
    print("Now Owing:", amount_owed(8, 8))