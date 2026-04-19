# Jonathan Foster
# 4/17/26
# P4LAB2
# This project displays information to users using loops

runAgain = 'yes'

while (runAgain.lower() == 'yes'):
    num = int(input("Enter an integer: "))
    print('\n')
    if num >= 0:
        for i in range(1,13):
            print(f'{num} * {i} = {num * i}')
        print('\n')
    else:
        print("This program does not handle negative numbers!")
        print('\n')
    runAgain = input("Do you want to run the program again? Enter yes or no: ")
    print('\n')
print("The program has exited")





'''Write a program that asks the user to enter an integer.
Only if the integer is zero or higher, the program should display the multiplication table for that integer from 1 to 12. See example output below.
If the integer the user entered is less than zero, the program should tell the user that it cannot accept negative values.
After displaying the multiplication table, the program should ask the user if they wish to run it again.
If the user types "yes", the program should run again. If the user types "no", the program should end.
You MUST use both a for loop and a while loop in this program.'''
