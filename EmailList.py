# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 2/20/19
# Python Version 3.7.2

# For this program I decided to use regular expressions in order to check for a valid email address.
# I felt that this was far more effective and efficient than building up a string and parsing through it as we learned in class.
# I found the regexes that I wanted to use on the internet at: http://emailregex.com/ 
# However, I wrote all of the code that uses the regexes myself.

# Importing pkgs
import os
import re

# This function allows me to clear the screen, I got this code from Stack Overflow. It is Linux and Windows compatible.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Main Boolean that keeps track of whether the user has closed the program
Is_Running = True

# Main menu that shows the user what they can do
Menu_Text = """
EZ Email Subscriber Management

[0] - Exit
[1] - Show Emails
[2] - Add An Email
[3] - Remove An Email
"""

# Holds the list of emails
Email_List = []

# Tracks what the user is inputting into the console
User_Input = ""

# Tracks whether the user has made a decision
User_Confirm = False

########################################################### PROGRAM LOGIC ################################################################

### The user wants to close the program
def Close_Program():

    # Adding global variables
    global User_Input
    global Is_Running

    # Clearing the screen for readability
    cls()

    print("\nAre you sure you want to close the program?")
    while User_Confirm == False:
        User_Input = input("\nPress '0' to close the program or '1' to go back: ")
        if int(User_Input) == 0:
            Is_Running = False
            break
        elif int(User_Input) == 1:
            cls()
            break
        else:
            print("\nPlease enter a valid selection: ")

### The user wants to view the complete list of emails
def Show_Emails():

    # Clearing the screen to improve readability
    cls()

    print("Current Subscribers:\n")
    for Email in Email_List: # Prints the list of emails
        print(str(Email_List.index(Email) + 1) + ") " + Email)

    input("\nPlease press 'enter' to return to the main menu.")
    cls()

### The user wants to add an email to the list
def Add_Email():

    global User_Input
    global User_Confirm

    while User_Confirm == False:
        # Clearing the screen to improve readability
        cls()
        print("Type 'exit' at anytime to return to the main menu.")
        User_Input = input("Please enter the email that you would like to add to the list: ")
        if User_Input.upper() == "EXIT":
            cls()
            break
        # Checks the user input against a regular expression 
        elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", User_Input):
            # This code occurs when the regex check returns false
            cls()
            print("Please enter a valid email address.")
            input("\nPress 'enter' to continue.")
        elif re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", User_Input):
            if len(Email_List) <= 9: # If the list of emails has 10 or less emails
                # This code occurs when the regex check returns true
                Email_List.append(User_Input)
                print("\n" + User_Input + " was added to the list.")
                input("\nPlease press 'enter' to continue.")
            else: # if the list of emails has more than 10 emails
                cls()
                print("\nYou already have 10 emails in your subscriber list. Please delete at least one to add a new one.")
                input("Press 'enter' to continue.")

### The user wants to remove an email from the list
def Remove_Email():

    # Adding global variables
    global User_Input
    global User_Confirm

    while User_Confirm == False:

        # Clearing the screen to improve readability
        cls()

        for Email in Email_List: # Prints the list of emails
            print(str(Email_List.index(Email) + 1) + ") " + Email)

        print("\nType 'exit' at anytime to return to the main menu.")
        User_Input = input("Please select the email that you would like to remove from the list: ")

        if User_Input.upper() == "EXIT":
            cls()
            break
        elif int(User_Input) <= len(Email_List):
            del Email_List[int(User_Input) - 1]
        else:
            cls()
            print("Please select a valid email to delete.")
            input("Press 'enter' to continue.")

### The main menu that allows the user access to the rest of the program
### This is also the main loop that the program runs in.
### Once the user selects an option they are taken to that part of the code before coming back here
def Main_Menu():

    # Adding global variables
    global User_Input
    global Is_Running
    
    print(Menu_Text)

    User_Input = input("Please enter a number in order to perform an action: ")

    if User_Input == "0":
        Close_Program()
    elif User_Input == "1":
        Show_Emails()
    elif User_Input == "2":
        Add_Email()
    elif User_Input == "3":
        Remove_Email()
    else:
        cls()
        print("\nPlease enter a valid selection.")
        User_Input = input("\nPlease press 'enter' to return to the main menu.")
        cls()

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:

    Main_Menu()