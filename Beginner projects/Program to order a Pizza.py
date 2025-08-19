#WAP to order a Pizza
pizza = input("Please select a Pizza size:\ns for small\nm for medium\nl for large\n")
bill = 0
if pizza == "s" or pizza == "S":
      bill = 100
      print("Your price is 100rps.")
elif pizza == "m" or pizza == "M":
    bill = 200
    print("Your pizza is 200rps.")
elif pizza == "l" or pizza == "L":
    bill = 300
    print("Your pizza is 300rps")
else:
    print(f"Please select from the options")
print("Thank You!")


pepperoni = input("Do you want pepperoni with the pizza? please select Y/N:\n")
if pepperoni == "Y" or pepperoni == "y":
        if pizza == "S" or pizza == "s":
                bill += 30
                print(f"Your bill is {bill}.")
        else:
                bill += 50
                print(f"Your bill is {bill}.")
    else:
            print("Please select from the options.")

extra_cheese = input("Do you want extra cheese? PLease select Y/N:\n")
if extra_cheese == "Y" or extra_cheese == "y":
            bill += 20
            print(f"Your total bill is {bill}")
else:
            print(f"Please pay {bill}.")
