#Read one character and print its ASCII value. Also show which character has ASCII value 65.
'''
ch = input("Enter a character: ")
print("ASCII value of", ch, "is", ord(ch)) # ord() character to number
print("Character with ASCII 65 is", chr(65)) # chr() converts number to character
'''

#Read a word and a number n. Print the word joined with itself using +, then print the word repeated n times using *.

word = input("Enter a word: ")
n = int(input("Enter repeat count: "))
joined = word + word # + joins (concatenates) strings
repeated = word * n # * repeats a string
print("Joined:", joined)
print("Repeated:", repeated)