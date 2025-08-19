import higher_lower_ascii_image
import higher_lower_db_names_and_data
import random

print(higher_lower_ascii_image.image)

random_info1 = random.choice(higher_lower_db_names_and_data.data)

random_info2 = random.choice(higher_lower_db_names_and_data.data)


score = 0
def display():
    global random_info1
    global random_info2
    if random_info1["followers"] == random_info2["followers"]:
        random_info2 = random.choice(higher_lower_db_names_and_data.data)
        print(f"compare1: {random_info1["name"]}, a {random_info1["description"]}, from {random_info1["country"]}")
        print(f"compare2: {random_info2["name"]}, a {random_info2["description"]}, from {random_info2["country"]}")
    else:
        print(f"compare1: {random_info1["name"]}, a {random_info1["description"]}, from {random_info1["country"]}")
        print(f"compare2: {random_info2["name"]}, a {random_info2["description"]}, from {random_info2["country"]}")


def modify_a():
    global random_info1
    global random_info2
    random_info1 = random_info1
    random_info2 = random.choice(higher_lower_db_names_and_data.data)

def modify_b():
    global random_info1
    global random_info2
    random_info1 = random_info2

def func1():
    global random_info1
    global random_info2
    global score
    if random_info1["followers"] > random_info2["followers"]:
        score += 1
        print(f"You're right!\n---------------------\nYour score is = {score}\n---------------------")
        modify_a()
        game()
    else:
        print("You're wrong! You lose.")


def func2():
    global random_info1
    global random_info2
    global score
    if random_info2["followers"] > random_info1["followers"]:
        score += 1
        print(f"You're right!\n---------------------\nYour score is = {score}\n---------------------")
        modify_b()
        random_info2 = random.choice(higher_lower_db_names_and_data.data)
        game()
    else:
        print("You lose")
#

def game():
    display()
    question = int(input("Who is having more followers? Type 1 or 2: "))
    if question == 1:
        func1()
    elif question == 2:
        func2()
    else:
        print("bye")
game()






