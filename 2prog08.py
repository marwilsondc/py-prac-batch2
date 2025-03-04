# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
printable = 0

while printable < 100:
    if printable % 2 != 0:
        print(printable)
    
    printable += 1