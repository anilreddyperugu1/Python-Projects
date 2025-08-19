#Program to generate a random shuffled password
import random

print("Welcome to the Password Generator!!")

letters_list = ["a", "b", "c", "d", "e", "f" ,"g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# letters = 52
numbers_list = [1,2,3,4,5,6,7,8,9,0]
# numbers = 10
symbols_list = ["!","@","#","$","%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", ";", ":", "'", ",", "<", ">", "/"]
# symbols = 25

letters = int(input("How many letters would you like in your password?"))
numbers = int(input("How many numbers would you like?"))
symbols = int(input("How many symbols would you like?"))

#generate a random str from the above lists and store it in the empty string
empty_string = ""
for i in range(letters):
    random_letter = random.choice(letters_list)
    empty_string += random_letter

for i in range(numbers):
    random_number = random.choice(numbers_list)
    empty_string += str(random_number)

for i in range(symbols):
    random_symbol = random.choice(symbols_list)
    empty_string += random_symbol

# print(empty_string)
#shuffling the generated password and printing
result = "".join(random.sample(empty_string, len(empty_string)))
print(f"Your password would be: {result}")