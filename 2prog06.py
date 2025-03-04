# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
first_number = int(input("Input first number = "))
count = 1
sum = 0

while count < 10:
    sum += int(input("Input a number = "))
    count += 1

print(first_number - sum)