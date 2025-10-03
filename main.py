import string 
import random

char_list =string.digits+srti

pin_len = 6

pin_code = ""

while len(pin_code)< pin_len:
  pin_code+=random.choice(char_list)

print(f"Your Pin Code Is: {pin_code}")