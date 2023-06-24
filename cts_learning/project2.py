## Project with loop and function.

lives = 10
stringword = "Apple"
word = list(stringword.lower())
winner = False
incorrectletters = ["a", "b", "c"]

def printscore():
    print("Lives: " + str(lives))
    print("Incorrect letters: ", end="")
    for x in range(len(incorrectletters)):
        if x == len(incorrectletters) - 1:
            print(incorrectletters[x], end="")
        else:
            print(incorrectletters[x], end=",")
    print("")
while lives > 0 and winner == False:
    # Print out the current scoreboard
    printscore()
    # Ask the user for a letter
    # Check if they won
    lives -= 1
if lives <= 0:
    print("You lost oh!. The word was " + stringword)
#else:
