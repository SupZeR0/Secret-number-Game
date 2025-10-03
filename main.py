import string 
import random

char_list =string.digits+string.ascii_letters +string.punctuation

pass_len = 28

pass_code = ""

while len(pin_code)< pin_len:
  pin_code+=random.choice(char_list)

print(f"Your Pin Code Is: {pin_code}")