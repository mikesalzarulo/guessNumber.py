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
    roundNum = 0
    number = random.randrange(1,101)
    # Intro.
    print('Guess the Mystery Number ...')

    # Continues loop until 7 rounds have passed
    for ROUNDS in range(7):
        ROUNDS += 1
        guess = int(input('Enter your guess (1-100):'))
        print('Round', ROUNDS, 'of 7\n'+
        '-------------')
        if 0 < guess < 101:
            if guess < number:
                print('--->', guess, 'is too low...')
            elif guess > number:
                print('--->', guess, 'is too high...')
            elif guess == number:
                print('Congratulations ... You guessed the Mystery Number!')
            else:
                print('Error...Incorrect number. Try again.')
        else:
            print('Error...Incorrect number. Try again.')
        
        
main()

