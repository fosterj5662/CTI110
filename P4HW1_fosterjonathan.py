# Jonathan Foster
# 4/16/26
# P4HW1
# This project asses the students ability to edit and enhance exiting programs

score_num = int(input("How many scores do you want to enter: "))
print()
# Create empty list
scores = []

for num in range(1, score_num + 1):
    score = float(input("Enter score #" + str(num) + ": "))
    while score < 0 or score > 100:
        print("\nINVALID SCORE!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) + " again: "))
    scores.append(score)
print()

# Find the lowest score
lowest = min(scores)
scores_modified = scores
scores_modified.remove(lowest)

# Calculate the average
avg = sum(scores_modified) / len(scores_modified)

if avg >= 90:
    Grade = 'A'
elif avg >= 80:
    Grade = 'B'
elif avg >= 70:
    Grade = 'C'
elif avg >= 60:
    Grade = 'D'
else:
    Grade = 'F'
print("----------------Results---------------")
print("Lowest score: {}".format(lowest))
print("Modified List: {}".format(scores_modified))
print("Average of scores: {:.2f}".format(avg))
print("Grade: {}".format(Grade))
print("-------------------------------------------------")







# pseudocode
'''Ask user to enter for number of scores they would like to enter. (10 points)
Create a loop to collect the number of scores the user wants to enter. (25 points)
Note every time a score is entered, the following should be done
Evaluate if the score is valid, it should be between 0 and 100 .
If it is not, notify the user and ask for a VALID score to be entered. (20 points)
Hint - you will need to use more than one loop in this program'''

