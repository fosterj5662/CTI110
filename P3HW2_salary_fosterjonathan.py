# Jonathan Foster
# 3/24/26
# P3HW2
# This project will show salary information

name = input("Enter the employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

# Calculate overtime using an if/else decision structure

if hoursWorked > 40:
    overTimeHours = hoursWorked - 40
    overPay = overTimeHours * (payRate * 1.5)
    regPay = 40 * payRate
    grossPay = regPay + overPay
else:
    overPay = 0
    overTimeHours = 0
    regPay = hoursWorked * payRate
    grossPay = regPay

print("-------------------------------------")
print("Employee Name: ",name,"\n")
print(f"{"Hours Worked":<15}{"Pay Rate":<12}{"Over Time":<12}{"Over Time Pay":<16}{"Regular Hour Pay":<20}{"Gross Pay":<12}")
print("-----------------------------------------------------------------------------------------------")
print(f"{hoursWorked:<15}{payRate:<12}{overTimeHours:<12}{overPay:<16.2f}${regPay:<20.2f}${grossPay:<12.2f}")


# Pseudocode

'''
Asks the user to enter name of employee
Ask user to enter number of hours the employee worked this week
Ask user to enter employee's pay rate
Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
Calculate amount employee should be paid for regular hours worked.
Display gross pay (total amount that should be paid to employee)
The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
Once finished, submit the finished code file through the assignment link in this folder.
'''

# Comment out unused code

'''
print(overPay)
print(overTimeHours)
print(regPay)
print(grossPay)
'''



