import FuncForAns
import picture
import words
import random
import time

answer_list = []

#Random the word from list and assign to variable called chosen_word
chosen_word = random.choice(words.word_list)


#Print the logo
print(picture.logo)

#Generate a "_" list that contain the answer word
FuncForAns.GenerateAnsList(answer_list, chosen_word)
print("\n\t\t" + ' '.join(answer_list), end = "\n\n")

#Declare a lives that equals to 6
lives = 6
display = ""

#Keeping the track of guessing letter
while (not FuncForAns.IsFull(answer_list)) and (lives > 0):
    #Ask the user to guess a letter, and assign their answer to variable caller guess
    guess = input("Guess a letter(or enter 'exit' to exit): ").lower()
    if guess == "exit":
        break
    else:
        #replace the letters into the appropriate blanks of answer list
        FuncForAns.ReplaceLetter(chosen_word, answer_list, guess)
        display = ' '.join(answer_list)
        print("\t\t" + display)

        if FuncForAns.CheckWord(guess, answer_list):
            print(picture.stages[lives])
        else:
            lives -= 1
            print(picture.stages[lives])

#Print the conclusion at the end of game
if guess != "exit":
    if lives <= 0:
        print("\n\n~~~~YOU LOSE~~~~")
    else:
        print("\n\n****YOU WIN****")
print(f"\nPsst, the chosen word is '{chosen_word}'\n")
#Stop the program in 4 seconds
time.sleep(4)
