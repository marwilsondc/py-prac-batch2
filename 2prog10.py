# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
first_number = int(input("Input a number: "))
second_number = int(input("Input another number: "))

for i in range(first_number + 1, second_number):
    print(i)