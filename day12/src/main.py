#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to Number Guessing Game\nPlease choose a difficulty\n")
difficulty = input("type easy or hard depending on your level\n")
lives = 0
if difficulty == "hard":
    lives=5
elif difficulty == "easy":
    lives=10
random_number=random.randint(0,100)
endGame=False
while endGame == False:
    user_guess=int(input("\nChoose a random number between 1 and 100:"))
    if user_guess == random_number:
        print(f"You re right,the correct answer is {random_number}")
        endGame=True
    elif user_guess<random_number:
        print("Wrong answer,try a littel higher")
        lives-=1
        print(f"\nYou ve got {lives} life/lives left\n")
    elif user_guess>random_number:
        print("Wrong answer,try a littel lower")
        lives-=1
        print(f"\nYou ve got {lives} life/lives left\n")
    if lives == 0:
        print("No more lives end of game :(")
        endGame=True