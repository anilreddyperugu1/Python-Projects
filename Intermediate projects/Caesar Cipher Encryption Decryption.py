letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z","!", " ", ",", "?", ".",]

#defining encryption technique
def encryption(text, shift_key):  # hi
    cipher_text = ""
    for i in text:
        position = letters_list.index(i)
        new_position = (position + int(shift_key)) % 31
        cipher_text += letters_list[new_position]
    print(f"Your cipher text is: {cipher_text}")

#defining decryption technique
def decryption(text, shift_key):
    normal_text = ""
    for i in text:
        position = letters_list.index(i)
        old_position = (position - int(shift_key)) % 31
        normal_text += letters_list[old_position]
    print(F"Your normal text is: {normal_text}")

#input and output things

while True:
    choice = input("Enter 'e' for encryption and 'd' for decryption:").lower()
    message = input("Type your message:").lower()
    shift = input("Please give the shift number:")
    if choice == "e":
        encryption(text=message, shift_key=shift)
    elif choice == "d":
        decryption(text=message, shift_key=shift)
    else:
        print("Please select from options.")
    go_again = input("Do you wanna go again (Y/N):").lower()
    if go_again == "y":
        True
    elif go_again == "n":
        False
        print("Thank You!")
        break





