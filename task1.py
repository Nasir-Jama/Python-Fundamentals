'''
Program: Task 1
Author: Abdinasir Jama
Date: October 2025
Description: This program allows the user to convert kilometeres to miles
'''


Working = True
# Working is a variable stored preferrably stored in cpu register, cache memory / ram
# Working is set to the data type of True (which are of two binary states of 0 and 1)
# it is most likely set to one in binary data (guessing by computer conventions)
while Working:
        # I am using this variable working to create a loop using the key-term "while"
        # The while loop continously runs depending on statement its given is true (1)
        InputText = "Enter a distance (km): "
        UserInput = input(InputText)

        # The variable input text is used to be put through into the method "input"
        # This method requests a user input from the user through the terminal tab
 
        if UserInput.strip().lower() == "stop":
            """
            I used the method "strip" because I learnt that it removes spaces and then
            set what the user has inputed to lower-case and that it matches "stop"
            
             This dosn't permantly change what the user has inputed instead checks
             if condition matches 
            """

            break
            # This set the statment in the while loop to false and permantly breaks the loop
        try:
              # The term "try" attempts to perform a task (conversion) without causing an error

              Miles = float(UserInput) * 0.621371

              # The conversion of miles is set to a float and is multiplied by the conversation
              # rate of kilometres to miles (0.621371)
              
              print(f"{round(Miles, 2)} miles")

              # The special f in the start allows for expressions in statement
              # Expressions are used through {} and i run the method of round
              # To round to 2 decimal places

        except ValueError:
              print("Error: Please Enter A Number Or Type Stop to Exit")
              # If the exception of valueerror is presented e.g. if error happends
              # I would present an error message in 


