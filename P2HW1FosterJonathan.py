# Jonathan Foster
# 2/19/26
# P1HW2
# This program calculates and displays travel expenses
# pseudocode
# 3 Ask user to enter their budget
# 4 Ask user to enter travel destination
# 5 Ask user for amount they will spend on gas
# 6 Ask user for amount they will spend on accommodation
# 7 Ask user for amount they will spend on food
# 8 Add expenses
# 9 Subtract expenses from budget
# 10 Display results


print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
print()
travel = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("How much will you need for food? "))
print()
print()
print()
print("------------Travel Expenses------------")
print(f"{"Location:":<20}{travel}")
print(f"{"Initial Budget:":<20}${budget:,.2f}")
print(f"{"Fuel:":<20}${gas:.2f}")
print(f"{"Accomodation:":<20}${hotel:.2f}")
print(f"{"Food:":<20}${food:.2f}")
print("----------------------------------------")
balance = budget - gas - hotel - food
print(f"{"Remaining balance:":<20}${balance:.2f}")

