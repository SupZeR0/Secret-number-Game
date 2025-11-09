import random
# Return a number between 1 and 20 (both included)
random_number = random.randint(1,20)
# storage the random number in variable
winner_number = [random_number]
# take a number from the user 
print("the computer have guessed a random number between 1 and 20")
number_guess = int(input("Guess the number: "))
print("-"*20)

#check if the number is the winning number
if number_guess in winner_number:
  print("You won You guessed the number right")
elif number_guess != winner_number:
  print(f"you lost the random number is {winner_number} ")
elif number_guess:
  print("please Enter a number between 1 and 20 ")  