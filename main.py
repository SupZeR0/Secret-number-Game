import random
number_guessed = int(input("Enter the number between 1 and 20: "))
random_number = random.randint(1, 20)
if number_guessed == random_number:
  print(f"You won! the guessed number is {number_guessed}")
else:
  print(f"you lost  the guessed number was {random_number}")
