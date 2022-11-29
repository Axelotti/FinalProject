import os, random
os.system("clear")

BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

print("WORDLE")
print("Let's play Wordle:")
print("Type a 5 letter word below and press Enter. \n")

file = open("words.txt","r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList)-1)].upper()
correct = word
# You get six chances to guess
for _ in range(6):
    guess = input("Please guess. > ").upper()

    # Check each letter
    for i in range(0, 5):
        if guess[i]==correct[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")
            
    print()

    # Check if the guess is correct
    if guess == correct:
        print("You win!")
        exit()
        
print("You lose!")
print(f"The correct word was {correct}.")
