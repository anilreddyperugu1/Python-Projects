#WAP to print authoriation for a customer into an exibition
height = int(input("Enter your height in feet:"))
bill = 0
total_bill = 0
if height >= 3:
      print("You can ride")
      age = int(input("What's your age?:"))
      if age < 12:
            bill = 150
            print("Your bill is 150rps")
      elif age < 18:
            bill = 250
            print("Your bill is 250rps")
      elif age > 18:
            bill = 500
            print("Your bill is 500rps")
      want_photo = input("Do you want a photo? Please type (Y/N):")
      if want_photo == "Y" or want_photo == "y":
            total_bill = bill + 50
            print(f" total_bill = {bill} + 50")
      print(f"So, your total bill is {total_bill}.")
else:
      print("You're not allowed")
print("Enjoy the ride!")


