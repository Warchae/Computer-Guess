from random import randint

#Variables
bottom = 0
top = 100
compGuess = randint(bottom,top)
tryAgain = 1

#User Guessed The Number in Limits
while tryAgain:
    try:
        guess = int(input("Choose a number between 0 - 100: "  ))
        if guess <= 100 and guess >= 0:
            tryAgain = 0
    except ValueError:
        print("Type a number, not float or letter.")

# Print computer guess and take feedback from user
def showGetFeedback():
    print(compGuess)
    return feedback() 

# Taking feedback function.
def feedback():
    feedback = input("If guess is too high (H), if it is too low (L), otherwise if computer guess correct type (C): ").upper()
    while feedback not in ["H", "L", "C"]:
        feedback = input("Invalid input. Please enter 'H' for too high, 'L' for too low, or 'C' for correct: ").upper()
    return feedback

# Main Program
try:
    x = showGetFeedback()
    while x != 'C':
        if x == "H":
            top = compGuess - 1
            compGuess = randint(bottom,top)
            x = showGetFeedback()
        elif x == "L":
            bottom = compGuess + 1
            compGuess = randint(bottom,top)
            x = showGetFeedback()
        else:
            print("Computer guessed your number correctly.")

except ValueError:
    print("Out of range.")