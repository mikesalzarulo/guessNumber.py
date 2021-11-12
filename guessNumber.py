#
# Michael Salzarulo
#
# guessNumber.py
#
# A number guessing game where the the user has seven attempts to guess the random number
# that was generated in the function from 1-100.
#
# Algorithm
# Display Game Goal: Display, "Guess the Mystery Number."
# Generate: Generate a random number between 1-100 inclusive.
# Input: A number (1-100).
# Processing: 1. Display round of rounds
#             2. Display input against whether it is too high or too low.
#             3. Continue processing until 7 rounds are reached or random number is guessed.
# Output: You are wrong, try again/ Correct and congratulations.
#





# Import random module.
import random
# Define main function.
def main():
    # Define Constant.
    ROUNDS = 7
    # Define Variables.
    first = 1
    last = 100
    userGuess = 0
    roundNum = 0
    numGuesses = 0
    randomNumber = random.randrange(1,101)
    choice = 'y'
    # Intro.
    print('Guess the Mystery Number ...\n')
    # Continues loop until 7 rounds have passed
    while numGuesses < 7 and userGuess != randomNumber:
        # Adds to the count of rounds and guesses.
        roundNum += 1
        numGuesses += 1
        # Displays game round.
        print('Round', roundNum, 'of', ROUNDS,'\n'+
            '-------------')
        # Calls the function to validate the user's guess.
        userGuess = getGuess(first, last)
        # Calls the function to compare the user's guess to number by passing parameters.
        guessWin(userGuess, randomNumber)
    # Asks the user if they would like to play again.
    choice = input('Would you like yo try again (y/n)?')
    # If y then call main function.
    if choice == 'y':
        main()
    # If anything else, break.
    else:
        print('Goodbye.')
# Returns range of user's guess value.        
def guessWin(guess, number):
        # Prints that guess is too low if too low.
        if guess < number:
            return print('--->', guess, 'is too low...')
        # Prints that guess is too high if too high.
        elif guess > number:
            return print('--->', guess, 'is too high...')
        # Congratulates user if correct.
        elif guess == number:
            return print('Congratulations ... You guessed the Mystery Number!')
        # If anything else is entered, respond with error.
        else:
            return print('Error...Incorrect number. Try again.')
# Defines the get guess validation function.        
def getGuess(first, last):
        # Defines functions variables.
        guess = 0
        # Asks for user's input.
        guess = int(input('Enter your guess (1-100):'))
        # Enters loop of validation until true.
        while first > guess or guess > last:
            # If false, respond with error and continue.
            print('Error...Incorrect number. Try again.')
                
            guess = int(input('Enter your guess (1-100):'))
            # If true, break and return guess.
        return guess
main()







