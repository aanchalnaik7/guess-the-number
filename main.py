import random  #from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer, turns):
  """checks answers against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input('Choose a difficulty. Type "easy" or "hard": ')
  if level == "easy": 
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the guessing game!")
  print("I am thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  print(f"The correct answer is: {answer}")
  turns = set_difficulty()

  guess =0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the numbers.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have gone out of guesses, You lose.")
      return
    elif guess != answer:
      print("Guess again.")
game()