"""
Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.

Used dictionary and basic operations. Using if else:
"""

student_grades = {} # Create a dictionary.

while True:
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = int(input("Enter your choice: ")) # Take the choice from the user.

    if choice == 1:
        name = input("Enter student name: ") # Take the name from the user.
        grade = int(input("\nEnter student grade: ")) # Take the grade from the user.
        student_grades[name] = grade # Add the name and grade to the dictionary.
    elif choice == 2:
        name = input("Enter student name: ") # Take the name from the user.
        grade = int(input("\nEnter student grade: ")) # Take the grade from the user.
        student_grades[name] = grade # Add the name and grade to the dictionary.
    elif choice == 3:
        for name, grade in student_grades.items(): # Print the name and grade from the dictionary.
            print(f"{name}: {grade}") # Print the name and grade from the dictionary.
    elif choice == 4:
        break # Break the loop.
    else:
        print("Invalid choice. Please try again.") # Print the invalid choice.

print("Exiting the program.") # Print the exiting the program.