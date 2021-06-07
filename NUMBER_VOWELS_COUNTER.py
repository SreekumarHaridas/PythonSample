# THIS PROGRAM WILL COUNT THE NUMBER OF EACH VOWEL IN A STRING USING DICTIONARY AND LIST COMPREHENSION
from run import *
VOWELS = 'aeiou'
STRING = input("\nENTER THE STRING THAT YOU WANT TO COUNT THE NUMBER OF VOWELS IN IT :\n")
STRING = STRING.casefold() # MAKE THE ENTERED STRING SUITABLE FOR CASELESS COMPARISON
# MAKE A DICTIONARY WITH EACH VOWEL A KEY AND VALUE 0
COUNT = {}.fromkeys(VOWELS, 0)
for char in STRING:
   if char in COUNT:
       COUNT[char] += 1
# DISPLAYING THE LIST OF VOWELS AND COUNT OF EACH VOWEL
print("\nTHE LIST OF VOWELS AND COUNT OF EACH VOWEL IN THE ENTERED STRING IS: ", COUNT)
run("NUMBER_VOWELS_COUNTER.py")