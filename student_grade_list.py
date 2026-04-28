"""
Student Grade List Program

This program allows users to enter student names and grades, validates the inputs,
and displays the list of students with their grades, highlighting the highest and lowest grades.

"""

# Display the current student grade list, with the highest and lowest grade
def student_grade_list(student_name,student_grade):
    print("\n---Student Grade---")
    # Print students' name with its corresponding grade
    for i, name in enumerate(student_name):
        print(f'{i + 1}. {name} : {student_grade[i]}')
    print("\n")

    # Print the highest / lowest grade with its corresponding name 
    print(f'Highest grade : {student_name[student_grade.index(max(student_grade))]} with {max(student_grade)}')
    print(f'Lowest grade  : {student_name[student_grade.index(min(student_grade))]} with {min(student_grade)}')
    print("\n")

# Validate name - reject empty name, spaces only and non-alphabet name
def get_valid_name():
    while True:
        input_name = input("Enter name : ")
        # Checking if the user put an empty name or spaces only
        if len(input_name) == 0 or input_name.isspace():
            print("Please enter a name")
            continue
        # Checking if the user put non-alphabet name
        if input_name.replace(" ","").isalpha() == False:
            print("Name contains number or symbols")
            continue
        return input_name.title()

# Validate grade - reject float number, grade below 0 and above 100
def get_valid_grade():
    while True :
        input_grade = input("Enter grade : ")
        try :
            # Convert to float first to catch decimal
            input_grade = float(input_grade)
            if input_grade != int(input_grade):
                print("Please enter a whole number")
                continue

            if input_grade < 0 or input_grade > 100:
                print("Please enter a valid grade (0 - 100)")
                continue

            return int(input_grade)
        except:
            print("Please enter a number")
            continue

# Validate choice - reject anything beside "Y" and "N"
def get_valid_choice():
    while True :
        exit_program = input("Exit program? [Y/N]\n").title()
        if exit_program == "Y" or exit_program == "N":
            return exit_program
        else:
            print("Invalid Input")

student_name = []
student_grade = []
print("Welcome to student grade list program!")

# Main loop to collect student data and display results
while True :
    name = get_valid_name()
    grade = get_valid_grade()

    student_name.append(name)
    student_grade.append(grade)

    student_grade_list(student_name,student_grade)

    if get_valid_choice() == "Y":
        break

print("Exit program successfully")