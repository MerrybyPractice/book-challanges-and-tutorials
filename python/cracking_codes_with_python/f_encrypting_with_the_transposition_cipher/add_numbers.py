# Inspired by the add numbers script in chapter 7 of Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

def add_numbers(a, b):

  return_value = a + b
  
  print(return_value)
  return return_value

input_value_a = int(input('What is the first value you would like to add? '))
input_value_b = int(input('What is the seccond value you would like to add? '))

add_numbers(input_value_a, input_value_b)