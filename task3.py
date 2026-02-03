import os

# import is used to access different scripts, classes and etc (libaries)
# os stands for Operating System so allows me to interact with the operating system
# i can use os to interfact with files, environment (environ) and but much more.


# In this caes am going to use os to handle, create or edit files.

# File names
input_file = "students.txt"
output_file = "results.txt"

# I created 2 variables to control what the script should look out or etc.

# dictionary to hold student data
students = {}


# Step 1: Read from file if it exists, otherwise enter manually
if os.path.exists(input_file):
    # This check if the os (operating systm) and the current path folder, checks for input file
    with open(input_file, "r") as f:
        # now that we know file exists, we open it as read only mode and store this as f
        for line in f:
            # loops over each line in the text file
            parts = line.strip().split(",")
            # strip removes spaces in that line e.g. "Alice,95"
            # split creates / returns a list seprated by the "," and stored as parts
            if len(parts) == 2:
                # checks if the data seprated in the list is exactly 2
                # e.g. [mark, 25]
                name = parts[0].strip()
                # python starts list at 0
                try:
                    mark = float(parts[1].strip())
                    students[name] = mark
                    # now we make sure the mark dosnt have spaces and that its a decimal
                    # now we store the student name and their marks in the dictionary
                except ValueError:
                    print(f"Invalid mark for {name}, skipped.")
else:
    # if the file is not found we would manually create it (manual data entry)
    print("File not found. Enter student data manually.")
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        # first we ask for the student name and remove the spaces
        if name.lower() == "done":
            # we check if the student typed "done" to end the program
            break
        try:
            # now we attempt to get the student marks
            mark = float(input(f"Enter mark for {name}: "))
            students[name] = mark
            # now we stored the student name and mark in the dictionary
            # using the student name as its unique identifier
        except ValueError:
            print("Invalid mark. Try again.")
            # remember try just attempts if there an error it goes here


# Step 2: Calculate average and top mark
if students:
    # if students found we do our own calculations to find stuff
    average = sum(students.values()) / len(students)
    # .values just only returns numbers in dictionary [80, 60, 30]
    # sum just adds the values up e.g. 80+60+30
    # now average we calculate by deviding it by the number of students
    top_student = max(students, key=students.get)
    # max just gets the top value, telling max to get it from marks not names
    top_mark = students[top_student]
    # reverse enginnering i guess, this just returns a number since students[a] = 1

else:
    # if no data in students we create default values
    average = 0
    top_student = "N/A"
    top_mark = 0

# Step 3: Write results to file
with open(output_file, "w") as f:
    # now we create an output file or rewrite an outputfile as store it as f

    # now we repeatedly just use the f.write function and use the f"" and {} 
    f.write("Student Results:\n")
    for name, mark in students.items():
        f.write(f"{name}: {mark}\n")
    f.write(f"\nAverage mark: {average:.2f}\n")
    f.write(f"Top student: {top_student} ({top_mark})\n")
    

print(f"Results written to {output_file}")

# final output message