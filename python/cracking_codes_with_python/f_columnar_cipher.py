# Colmunar Transposition Cipher Encryption as enumerated in chapter 7 of Cracking codes with Python. 
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

def encrypt_message(key, message): 
    ciphertext = [''] * key
    
    for column in range(key): 
      current_index = column

      while current_index < len(message): 
        
        ciphertext[column] += message[current_index]
        

        current_index += key

    return ''.join(ciphertext)

    ciphertext = encrypt_message(key, message) 

    print(ciphertext + '|')  

def main(): 
  message = input('What is the message we will be encrypting? ')
  key = int(input('What is the encryption key we will be using? '))
  encrypt_message(key, message)
if __name__ == '__main__':
  main()
