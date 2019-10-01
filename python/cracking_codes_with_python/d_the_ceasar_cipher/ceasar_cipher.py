# Caesar Cipher guided by the example in chapter 5 of Cracking Codes with Python. 
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
#import pyperclip

message = input('Enter text to be encrypted here. ')
key = int(input('Enter Encryption Key Here. '))

mode = input('Encryption mode or Decryption mode? ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz1234567890!?.,;:()'

translated = ''

for symbol in message:
  
  if symbol in SYMBOLS: 
    
    symbol_index = SYMBOLS.find(symbol)

   
    if mode.lower() == 'encryption' or mode.lower() == 'encrypt': 
      translated_index = symbol_index + key

    elif mode.lower() == 'decryption' or mode.lower() == 'decryption': 
      translated_index = symbol_index - key  
    
    if translated_index >= len(SYMBOLS): 
      translated_index = translated_index - len(SYMBOLS)
    elif translated_index < 0: 
      translated_index = translated_index + len(SYMBOLS) 

    translated = translated + SYMBOLS[translated_index]
  else: 
    translated = translated + symbol

print(translated)
#pyperclip.copy(translated)