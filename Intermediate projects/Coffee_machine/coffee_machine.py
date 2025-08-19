import coffee_machine_db

milk = coffee_machine_db.data[1]["quantity"]
espresso = coffee_machine_db.data[2]["quantity"]
water = coffee_machine_db.data[0]["quantity"]
beans = coffee_machine_db.data[3]["quantity"]
total_paid = 0
paid = 0
def spill_tea():
    global water
    global milk
    global choice
    global total_provided
    global total
    global paid
    tea = 15
    paid = tea
    if total_provided >= tea:
        total = total_provided - tea
        if total_provided == tea:
            print(f"Here is your {choice}!")
        else:
            print(f"Please have your {total} in change")
            print(f"Here is your {choice}!!")
    else:
        print("Please provide enough money")
        exit()
    if water >= 120 or milk >= 80 :
        water = water - 120
        milk = milk - 80
    else:
        print("Not enough water/milk")
        exit()

def spill_coffee():
    global water
    global milk
    global total_provided
    global total
    global paid
    coffee = 30
    paid = coffee
    if total_provided >= coffee:
        total = total_provided - coffee
        if total_provided == coffee:
            print(f"Here is your {choice}!")
        else:
            print(f"Please have your {total} in change")
            print(f"Here is your {choice}!!")
    else:
        print("Please provide enough money")
        exit()
    if water >= 120 or milk >= 100:
        water = water - 120
        milk = milk - 100
    else:
        print("Sorry! Not enough water/milk")
        exit()

def spill_espresso():
    global water
    global beans
    global total_provided
    global total
    global espresso
    global paid
    espresso = 45
    paid = espresso
    if total_provided >= espresso:
        total = total_provided - espresso
        if total_provided == espresso:
            print(f"Here is your {choice}!")
        else:
            print(f"Please have your {total} in change")
            print(f"Here is your {choice}!!")
    else:
        print("Please provide enough money")
        exit()
    if water >= 80 or beans >= 20 :
        water = water - 80
        beans = beans - 20
    else:
        print("Not enough water/beans")
        exit()

def latte_cappuccino():
    global total_provided
    global choice
    global milk
    global espresso
    global total
    global paid
    if choice == "latte":
        def spill_latte():
            global milk
            global espresso
            global total_provide
            global paid
            latte = 50
            paid = latte
            if milk > 90 and espresso >= 45:
                milk -= 100 #required 100ml
                espresso -= 50 #required 50ml
            else:
                print("Not enough milk/espresso")
                exit()
            if total_provided >= latte:
                total = total_provided - latte
                if total_provided == latte:
                    print(f"Here is your {choice}!")
                else:
                    print(f"Please have your {total} in change")
                    print(f"Here is your {choice}!!")
            else:
                print("Please provide enough money")
                exit()
        spill_latte()
    if choice == "cappuccino":
        def spill_cappuccino():
            global milk
            global espresso
            global total_provided
            global total
            global paid
            cappuccino = 150
            paid = cappuccino
            if milk > 60 and espresso >= 30:
                milk -= 70 #required 100ml
                espresso -= 40 #required 50ml
            else:
                print("Not enough milk/espresso")
                exit()
            if total_provided >= cappuccino:
                total = total_provided - cappuccino
                if total_provided == cappuccino:
                    print(f"Here is your {choice}!")
                else:
                    print(f"Please have your {total} in change")
                    print(f"Here is your {choice}!!")
            else:
                print("Please provide enough money")
                exit()
        spill_cappuccino()


def checking_coins():
    global choice
    global total_provided
    print("Please insert coins.")
    five_coins = int(input("How many 5Rs. coins: "))
    ten_coins = int(input("How many 10Rs. coins: "))
    twenty_coins = int(input("How many 20Rs. coins: "))
    total_provided = ((5 * five_coins) + (10  * ten_coins) + (20 * twenty_coins))
    print(f"money provided = {total_provided}")

def report():
    global milk
    global water
    global espresso
    global beans
    global paid
    global total_paid
    print(f"milk: {milk}ml")
    print(f"water: {water}ml")
    print(f"espresso: {espresso}ml")
    print(f"beans: {beans}")
    total_paid += paid
    print(f"money: {total_paid}")




dispense = True
while dispense:
    choice = input("What would you like to have? (latte/espresso/cappuccino/tea/coffee):")
    if choice == "tea":
        print("The price is 15Rs.")
        checking_coins()
        spill_tea()
    elif choice == "coffee":
        print("The price is choice 30Rs.")
        checking_coins()
        spill_coffee()
    elif choice == "espresso":
        print("The price is 45Rs.")
        checking_coins()
        spill_espresso()
    elif choice == "latte":
        print("The price is 50Rs.")
        checking_coins()
        latte_cappuccino()
    elif choice == "cappuccino":
        print("The price is 150Rs.")
        checking_coins()
        latte_cappuccino()
    elif choice == "report":
        report()
    elif choice == "off":
        dispense = False
        print("Thank you.")
    else:
        print("Please select from the options.")
