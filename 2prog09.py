# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
number_set = range(1, 101)

for i in number_set:
    if i % 5 != 0:
        print(i)