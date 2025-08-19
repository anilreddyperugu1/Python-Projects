import random

easy_lives = 10
def easy(num):
    global easy_lives
    number = int(input("Make a guess: "))
    if num == number:
        print("Hurray!! You guessed it!!")
        print(f"The number is {num}")
    elif easy_lives == 1:
        print("You lose")
        print(f"The number is {num}")
    else:
        if number < num:
            print("Your guess is too low!")
        elif number > num:
            print("Your guess is too high!")
        print("Guess again")
        easy_lives -= 1
        print(f"You have only {easy_lives} attempts to guess the number")
        easy(thought_num)


hard_lives = 5
def hard(num):
    global hard_lives
    number = int(input("Make a guess: "))
    if num == number:
        print("Hurray!! You guessed it!!")
        print(f"The number is {num}")
    elif hard_lives == 1:
        print("You lose")
        print(f"The number is {num}")
    else:
        if number < num:
            print("Your guess is too low!")
        elif number > num:
            print("Your guess is too high!")
        print("try again")
        hard_lives -= 1
        print(f"You have only {hard_lives} attempts to guess the number")
        hard(thought_num)


print("Lemme think of a number between 1 to 50.")
thought_num = random.randint(1, 50)
# print(thought_num)
level = input("Choose level of difficulty... type 'easy' or 'hard': ").lower()
if level == "easy":
    print(f"You have 10 attempts to guess the number")
    easy(thought_num)
if level == "hard":
    print(f"You have 05 attempts to guess the number")
    hard(thought_num)