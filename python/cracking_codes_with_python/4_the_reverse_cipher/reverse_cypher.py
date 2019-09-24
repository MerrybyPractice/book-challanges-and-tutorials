# Reverse Cipher example as written in chapter 4 of Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = input()
translated = ''

i = len(message) - 1

while i >=0: 
  translated = translated + message[i] 
  i = i -1

print(translated)


