# Columnar Transposition Hack per Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip 
from cracking_codes_with_python.j_detect_english import is_english
from cracking_codes_with_python.g_decrypt_columnar_transposition_cipher import decrypt_message as decrypt 

def hack_transposition(text): 
  print('Press Ctrl-C to quit at any time.')

  print('Hacking...')
  for key in range(1, len(text)): 

    print('Trying key #%s...' % (key))
    print()
    print('...')
    decrypted_text = decrypt(key, text)
    print()
    print('...')

    if is_english(decrypted_text): 

      print()
      print('Possible encryption hack:')
      print('Key %s: %s' % (key, decrypted_text[:100]))
      print()
      print('Enter D if done, anything else to continue the hack:')
      response = input('>')

      if response.strip().upper().startswith('D'):
        return decrypted_text

  return None   

def main(text): 

  hacked_text = hack_transposition(text)

  if hacked_text == None: 
    print('Failed to hack the Columnar Transposition Encryption')
  else: 
    print('Copying hacked string to clipboard:')
    print(hacked_text)
    pyperclip.copy(hacked_text)  

if __name__ == '__main__': 
  main()
