# A module for detecting English from Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

'''

j_detect_english.is_english(your_string) 
  True or False

The detect english module requires a dictionary.txt to run, an example can be found on https://nostarch.com/crachingcodes/ . If you wish to create your own, it needs to be formatted so that each word is on its own line, with no definition. 

This module will return a True or False statement when called on a string.

'''

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_and_spaces = uppercase_letters + uppercase_letters.lower() + ' \t\n'

def load_dictionary(dictionary_file_string): 
  dictionary = open(dictionary_file_string)

  english_words = {} 

  for word in dictionary.read().split('\n'): 
    english_words[word] = None

  dictionary.close()  

  return english_words

def remove_non_letters(text): 
  letters_only = []

  for symbol in text:
    if symbol in letters_and_spaces: 
      letters_only.append(symbol)
  return ''.join(letters_only)     


def get_english_count(text, dictionary_file_string): 
  text = text.upper()
  text = remove_non_letters(text)

  possible_words = text.split() 

  if possible_words == []: 
    return 0.0

  matches = 0

  english_words = load_dictionary(dictionary_file_string)

  for word in possible_words:   
    if word in english_words: 
      matches += 1
  return float(matches) / len(possible_words)  

def is_english(text, word_percentage = 20, letter_percentage = 85): 
  words_match = get_english_count(text) * 100 >= word_percentage
  num_letters = len(remove_non_letters(text))   

  percent_letters_in_message = float(num_letters) / len(text) * 100

  letters_match = percent_letters_in_message >= letter_percentage

  return words_match and letters_match
