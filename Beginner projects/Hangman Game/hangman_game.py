import random
import words_file
import Hangman_emoji

random_name = random.choice(words_file.words)
# print(random_name)

#creating as many blanks as the random name has
blanks = []
for i in range(len(random_name)):
    blanks += "_"
print(blanks)

print(Hangman_emoji.stages[6])
lives = 6

#Main body
game_over = False
while not game_over:
    guess_letter = input("Guess a letter:").lower()
    #replacing the blank with the input letter if they are same
    for i in range(len(random_name)): #apple
        if guess_letter == random_name[i]:
            blanks[i] = guess_letter
    print(blanks)

    if guess_letter not in random_name:
        lives -= 1
        print("Sorry! you missed it. Lives remaining:", lives)
    print(Hangman_emoji.stages[lives])
    if lives == 0:
        game_over = True
        print("Hangman formed. You Lose!")
    if "_" not in blanks:
        game_over = True
        print("You Won!")


