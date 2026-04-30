# Jonathan Foster
# 4/30/26
# P5LAB
# This program will simulate a customer using a self-checkout machine


import random

def main():
    # Generate a random float value with 2 decimal places
    amount_owed = round(random.uniform(0.01, 100.00),2)
    # display the amount owed
    print(f"You owe ${amount_owed:.2f}")
    # Prompt the user to enter an amount of cash into the self checkout
    amount_paid = float(input("How much cash will you put into the self checkout: "))
    # calculate the change owed
    change_owed = amount_paid - amount_owed
    print(f"Change is ${change_owed:.2f}")
    print()
    change_owed = round(change_owed * 100)
    
    disperse_change(change_owed)
    
def disperse_change(change):
    
    DOLLARS = 100
    QUARTERS = 25
    DIMES = 10
    NICKELS = 5
    PENNIES = 1
    '''
    # Get a float from the user

    change = float(input("Enter the amount as a float: $"))

    # Convert the float to an integer

    change = int(change * DOLLARS)
    print(change)
    '''
    if change ==0:
        print("No change!")

    # Calculate the change for each coin type
    # Integer division //
    # Modulus %

    num_dollars = change // DOLLARS
    change = change % DOLLARS

    num_quarters = change // QUARTERS
    change = change % QUARTERS

    num_dimes = change // DIMES
    change = change % DIMES

    num_nickel = change // NICKELS
    change = change % NICKELS

    num_pennies = change // PENNIES

    # Display the amounts used

    if num_dollars > 0:
        print(num_dollars, end=' ')
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")

    if num_quarters > 0:
        print(num_quarters, end=' ')
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")
            
    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")
            
    if num_nickel > 0:
        print(num_nickel, end=' ')
        if num_nickel == 1:
            print("Nickel")
        else:
            print("Nickels")

    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

main()
