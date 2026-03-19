# Jonathan Foster
# 3/19/26
# P3LAB
# This project is going to allow users to enter in money (float) value with 2 decimals

# Define constants for the change

DOLLARS = 100
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1

# Get a float from the user

change = float(input("Enter the amount as a float: $"))

# Convert the float to an integer

change = int(change * DOLLARS)
print(change)

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





