# Code for a Columnar Transposition Encryption and Decryption per Cracking Codes with Python 
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time, os, sys 

from f_columnar_cipher import encrypt_message as encrypt

from g_decrypt_columnar_transposition_cipher import decrypt_message as decrypt

file_name = input('What file would you like to access? ')
mode = input('Would you like to encrypt or decrypt this file?')

def columnar_transposition_file(file_name, mode): 
  input_file_name = file_name
  output_file_name = 'assets/file_encryption/encrypted.txt'
  key = 123
  mode = mode #encrypt or decrypt 

  if not os.path.exists(input_file_name):
    print('The file %s does not exist. Terminating...' % (input_file_name))
    sys.exit()

  if os.path.exists(output_file_name): 
    print('This will overwrite the file %s. 9(C)ontinue or (Q)uit?' %(output_file_name))
    response = input('> ')
    if not response.lower().startswith('c'): 
      #I mean, a lot of things start with c that arent continue, but ok
      sys.exit()  

  file_obj = open(input_file_name)
  content = file_obj.read()
  file_obj.close()

  print('%sing...' %(mode.title()))

  start_time = time.time()

  if mode == 'encrypt': 
    translated = encrypt(key, content)
  elif mode == 'decrypt': 
    translated = decrypt(key, content)
   
  total_time = round(time.time() - start_time, 2) 
  print('%sion time: %s secconds' %(mode.title, total_time))

  output_file_object = open(output_file_name, 'w')
  output_file_object.write(translated)
  output_file_object.close()

  print('Done %sing %s (%s characters).' % (mode, input_file_name, len(content)))
  print('%sed file is %s.' % (mode.title(), output_file_name))

columnar_transposition_file(file_name, mode)

# if __name__ == '__main__': 
#   columnar_transposition_file()

