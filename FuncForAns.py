# define a function whose missio is Generate a list in order to contain the answer list
def GenerateAnsList(answer_list, chosen_word):
    for i in range(len(chosen_word)):
        answer_list.append("_")
        
#define a function Replacing the letters
def ReplaceLetter(chosen_word, answer_list, guess):
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            answer_list[i] = guess

# Check wherether the answer list was full or not
def IsFull(answer_list):
    if "_" not in answer_list:
        return True
    return False

# Check the guess wherether is in answer list or not
def CheckWord(guess, answer_list):
    if guess in answer_list:
        return True
    return False
