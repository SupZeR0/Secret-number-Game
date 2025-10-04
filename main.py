stop_num = int(input("Please enter the number you want to end with: "))
even_odd = int(input("if you want only even number type 2 if you want odd type 3 "))

if even_odd == 2:
  for number in range(0, stop_num + 1, 2):
    print(f"the even numbers is: {number}")
elif even_odd == 3:
  for number in range(1, stop_num + 1, 2):
    print(f"the odd numbers is: {number}")
else:
  for number in range(1, stop_num + 1):
    print(number)