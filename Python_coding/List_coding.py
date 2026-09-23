# find maximum Without using max()
'''
numbers = list(map(int, input("Enter numbers: ").split()))
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num


print("Maximum number:", max_number)
'''

# find the total and average in the list 

numbers = list(map(int,input("Enter numbers: ").split()))
total = sum(numbers)
average = total / len(numbers)
print("Total:", total)
print("Average:", average)


