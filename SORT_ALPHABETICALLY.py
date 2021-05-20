# THIS PROGRAM WILL SORT ALPHABETICALLY THE WORDS FORM A STRING PROVIDED BY THE USER
from run import *
STRING = input("\nENTER YOUR STRING: ")
# SPLIT THE ENTERED STRING INTO A LIST OF WORDS
WORDS = [word.lower() for word in STRING.split()]
# SORT THE LIST
WORDS.sort()
# DISPLAY THE SORTED WORDS
SORTED_LIST_CAPS = [word.capitalize() for word in WORDS]
SORTED_LIST_UP = [word.upper() for word in WORDS]
SORTED_LIST_LO = [word.lower() for word in WORDS]
print("\nTHE LIST OF SORTED WORDS IN CAPITALIZED FORMAT IS: ", SORTED_LIST_CAPS)
print("\nTHE LIST OF SORTED WORDS IN UPPER CASE FORMAT IS: ", SORTED_LIST_UP)
print("\nTHE LIST OF SORTED WORDS IN LOWER CASE FORMAT IS: ", SORTED_LIST_LO)
print("\nTHE SORTED WORDS IN CAPITALIZED FORMAT ARE:")
for word in SORTED_LIST_CAPS:
    print(word)
print("\nTHE SORTED WORDS IN UPPER CASE FORMAT ARE:")
for word in SORTED_LIST_UP:
    print(word)
print("\nTHE SORTED WORDS IN LOWER CASE FORMAT ARE:")
for word in SORTED_LIST_LO:
    print(word)
run("SORT_ALPHABETICALLY.py")