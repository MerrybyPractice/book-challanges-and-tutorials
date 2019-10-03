# Columnar Transposition Ciper Decryption inspired by chapter 8 of Cracking Codes with Python 
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math, pyperclip

def decrypt_message(key, ciphertext):

  num_columns = int(math.ceil(len(ciphertext) / float(key)))

  num_rows = key

  extra_boxes = (num_columns * num_rows) - len(ciphertext)

  plaintext = [''] * num_columns

  column = 0
  row =0

  for symbol in ciphertext:
    plaintext[column] += symbol
    column += 1 # Point to the next column.

    if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - extra_boxes):
      column = 0
      row += 1
            
  return ''.join(plaintext)

def main(): 
  ciphertext = input('What is the text you would like to decrypt? ')
  key = int(input('What is the key you would like to use? '))

  decrypt_message(key, ciphertext)


if __name__ == '__main__': 
  decrypt_message(key, ciphertext)
