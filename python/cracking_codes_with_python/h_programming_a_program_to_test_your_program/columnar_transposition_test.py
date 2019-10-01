# Automated Testing for a Columnar Transpotion Cypher encoder and decoder per Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys
from cracking_codes_with_python.f_encrypting_with_the_transposition_cipher import columnar_cipher

from cracking_codes_with_python_g_decrypting_with_the_transposition_cipher.decrypt_columnar_transposition_cipher import decrypt_message

def main(): 
  random.seed(802) 

  for i in range(20): 
    message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40) 

    message = list(message) 

    random.shuffle(message) 
    message = ''.join(message)
    print('Test #%s: "%s..."'%(i+1, message[:50]))

    for key in range(1, int(len(message)/2)):
      encrypted = colmunar_cipher.colmunar_cipher(key, message) 
      decrypted = decrypt_message.decrypt_message(key, encrypted)

      if message != decrypted: 
        print('Mismatch with key %s and message %s.' % (key, message))
        print('Decrypted as: ' + decrypted) 
        sys.exit()
  print('Transposition cipher test passed.')  

  if __name__ == '__main__': 
    main()    
