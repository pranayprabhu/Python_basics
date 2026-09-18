# print("Hello World")

# taking the input and print
'''
name = input("Enter the name : ")
age = input("Enter the age : ")
print(f"My name is {name} and my age is {age}")

'''

# read the input as int and add 
'''
num1 = int(input("enter the number1 : "))
num2 = int(input("enter the number2 : "))
print(f"addition of two numbers {num1 + num2}")
'''

# swap numbers without temp variable 
'''
num1 = int(input("enter the number1 : "))
num2 = int(input("enter the number2 : "))

# num1,num2 = num2,num1  #in python 

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping number1 : {num1} and number2 : {num2}")

'''
# type conversion 
'''
num1 = input("enter the number1 : ")

num_int = int(num1)
num_float = float(num1)
num_str = str(num1)

print(f"number1 as int : {num_int} and as float : {num_float} and as string : {num_str}")
print(type(num_int))
print(type(num_float))
print(type(num_str))
'''

# f string formatting {marks:.2f} means: show the number with exactly 2 digits after the decimalpoint
'''
name = input("enter the name : ")
marks = float(input("enter the marks  : "))

print(f"My name is {name} and marks is {marks:.2f}")
'''

# multiple inputs in single line
'''
num1,num2 = input("enter the number1 and number2 : ").split()
num1 = int(num1)
num2 = int(num2)
print(f"addition of two numbers {num1 + num2}")
'''

# map() applies int() to every piece produced by split()
'''
a, b, c = map(int, input("Enter three numbers: ").split())
average = (a + b + c) / 3
print(f"Average = {average:.2f}")

'''


