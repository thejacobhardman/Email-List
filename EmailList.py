# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 2/20/19
# Python Version 3.7.2

# Importing the OS pkg
import os

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

    print("Current Subscribers:\n")
    for Email in Email_List: # Prints the list of emails
        print(str(Email_List.index(Email)) + ") " + Email)

    input("\nPlease press 'enter' to return to the main menu.")
    cls()

### The user wants to add an email to the list
def Add_Email():

    global User_Input
    global User_Confirm

    while User_Confirm == False:
        print("\nType 'exit' at anytime to return to the main menu.")
        User_Input = input("Please enter the email that you would like to add to the list: ")
        if User_Input.upper() == "EXIT":
            cls()
            break
        else:
            Email_List.append(User_Input)

### The user wants to remove an email from the list
def Remove_Email():

    # Adding global variables
    global User_Input
    global User_Confirm

    while User_Confirm == False:

        for Email in Email_List: # Prints the list of emails
            print(str(Email_List.index(Email)) + ") " + Email)

        print("\nType 'exit' at anytime to return to the main menu.")
        User_Input = input("Please select the email that you would like to remove from the list: ")

        if User_Input.upper() == "EXIT":
            cls()
            break
        else:
            del Email_List[int(User_Input)]

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