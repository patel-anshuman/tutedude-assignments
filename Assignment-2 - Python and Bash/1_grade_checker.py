# Grade Checker
"""
Grade Checker

Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
here we used a basic if else statement to carry out marks and all.
"""

score = int(input("Enter your score: ")) # Take the score from the user.

if score >= 90:
    print("A") # Print the grade.
elif score >= 80:
    print("B") # Print the grade.
elif score >= 70:
    print("C") # Print the grade.
elif score >= 60:
    print("D") # Print the grade.
else:
    print("F") # Print the grade.