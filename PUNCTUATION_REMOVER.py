# THIS PROGRAM WILL REMOVE PUNCTUATIONS ('''!()-[]{};:'"\,<>./?@#$%^&*~''') FROM ENTERED STRING
from run import *
PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
STRING = input("\nENTER THE STRING THAT YOU WANT TO REMOVE PUNCTUATIONS :\n")
#STRING = STRING.casefold() # MAKE THE ENTERED STRING SUITABLE FOR CASELESS COMPARISON
# REMOVING PUNCTUATIONS FROM THE ENTERED STRING
NO_PUNCTUATIONS = ""
for char in STRING:
   if char not in PUNCTUATIONS:
       NO_PUNCTUATIONS = NO_PUNCTUATIONS + char

# DISPLAYING THE NON PUNCTUATED STRING
print("\nNON PUNCTUATED VERSION OF ENTERED STRING IS: ", NO_PUNCTUATIONS)
run("PUNCTUATION_REMOVER.py")