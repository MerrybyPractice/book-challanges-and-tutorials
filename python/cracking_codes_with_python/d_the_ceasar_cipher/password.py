#password checking program as described in chapter 5 of Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

typed_password = input('Enter your password. ')

if typed_password == 'swordfish':
  print('Access Granted')
else: 
  print('Access Denied')  

print('Done')
