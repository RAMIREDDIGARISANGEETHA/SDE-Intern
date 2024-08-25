'''Task-02

Create a

Guessing Game

Build a program that generates a random number and challenges the user to guess it.
The program should prompt the user to input their guess, compare it to the generated number,
and provide feedback if the guess is too high ar too low. It should continue until the user correctly guesses the number and then display the number of attempts it took to win the game'''
import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    guessing_game()
