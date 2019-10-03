# Columnar Transposition Ciper Decryption inspired by chapter 8 of Cracking Codes with Python 
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math

def decrypt_message(key, ciphertext): 

  num_columns = int(math.ceil(len(ciphertext)/float(key)))

  #necessary?
  num_rows = key

  extra_boxes = (num_columns * key) - len(ciphertext) 

  plain_text = [''] * key

  cur_column = 0
  cur_row = 0

  for char in ciphertext: 

    plain_text[cur_column] += char
    cur_column += 1

    if (cur_column == num_columns) or (cur_column == num_columns - 1 and cur_row >= key - extra_boxes): 

      cur_column = 0
      cur_row += 1

  return_value = ''.join(plain_text)  
  print(return_value)
  return return_value     


def main(): 
  ciphertext = input('What is the text you would like to decrypt? ')
  key = int(input('What is the key you would like to use? '))

  decrypt_message(key, ciphertext)


if __name__ == '__main__': 
  decrypt_message(key, ciphertext)
