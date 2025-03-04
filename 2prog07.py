# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
number_set = set()
even_set = set()


while len(number_set) < 10:
    new_input = int(input("Input a number = "))
    number_set.add(new_input)

    if new_input % 2 == 0:
        even_set.add(new_input)

print(number_set)
print(even_set)
print("Total of =", len(even_set), "even numbers")
