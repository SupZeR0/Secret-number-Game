import random
number_guessed = input("Enter the number between 1 and 20: ")
if number_guessed == random.randint(1,20):
  print("You won!")
else:
  print("you lost!")