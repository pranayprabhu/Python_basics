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

num1 = int(input("enter the number1 : "))
num2 = int(input("enter the number2 : "))

# num1,num2 = num2,num1
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping number1 : {num1} and number2 : {num2}")


