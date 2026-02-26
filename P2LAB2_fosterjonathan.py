# Jonathan Foster
# 2/26/26
# P2LAB2
# This program will show how to use dictionary with keys and values

# Create the dictionary The car model is key and the mpg is the value

cars = {"Camero": 18.21, "Prius" : 52.36, "Model S" : 110, "Silverado" : 26}

# Display results, Show a list of all keys in the dictionary

keys = cars.keys()
print(keys)
print()

# Get user input, get the vehicle from the user

car_input = input("Enter a vehicle to see it's mpg: ")
print()

# Get the corresponding mpg to the vehicle's name

mpg_output = cars[car_input]

# Display output

print(f"The {car_input} gets {mpg_output} mpg.\n")

# Get the distance traveled

distance = float(input(f"How many miles will you drive the {car_input}? "))
print()

# Calculate gallons of gas needed

gallons_needed = distance / mpg_output

# Display the car and number of gallons needed

print(f"{gallons_needed:,.2f} gallon(s) of gas needed to drive the {car_input} {distance} miles.")

