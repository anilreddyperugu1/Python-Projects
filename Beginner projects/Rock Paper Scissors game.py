import random
user_choice = int(input("Enter a number between 0 and 2:"))
if user_choice > 2:
    print("Please select from 0 to 3")
computer_choice = random.randint(0,2)
print(f"Computer's choice is {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("Hurray!! You Won.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose. Please try again")
elif user_choice > computer_choice:
        print("Hurray!! You Won.")
elif computer_choice > user_choice:
        print("You lose. Please try again")
elif user_choice == computer_choice:
    print("Draw!!")



