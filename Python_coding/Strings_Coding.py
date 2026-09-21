# reverse the string
'''
input_string = input("Enter a string to reverse: ")
reversed_string = input_string[::-1]    
print("Reversed string:", reversed_string)

'''


# count the number of vowels in the string
'''
input_string = input("Enter a string to count vowels: ")
vowels = "aeiou"   
vowel_count = 0
for char in input_string.lower():
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

'''

# count the number of consonants 
'''
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Consonants:", count)
'''

# check palindrome
'''
text = input ("Enter a string to check palindrome: ")
if text == text[::-1]:
    print("The string is a palindrome.") 
else:
    print("The string is not a palindrome.")   

'''

# count the numbere of words in the string
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

'''

# count the number of characters in the string
'''
text = input("Enter a string: ")
char_count = len(text)
print("Number of characters:", char_count)
'''

# uppercase and lowercase conversion
'''
text = input("Enter a string: ")
result_text = ""
for ch in text:
    if ch.islower():
        result_text += ch.upper()
    elif ch.isupper():
        result_text += ch.lower()
    else:
        result_text += ch

print("Converted string:", result_text)

'''

