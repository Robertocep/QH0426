"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def menu_main():
    """
    Main menu.
    """
    while True:
        print("\nPlease enter the letter which coresponds with your desired menu choice:")
        print("\t[A] View Data")
        print("\t[B] Visualize Data")
        print("\t[C] Export Data")
        print("\t[D] Exit\n")

        temp = input("").lower()
        if temp == "a" or temp == "b" or temp == "c" or temp == "d":
            flush(f"You have chosen option {temp.capitalize()}")
            return temp.capitalize()
        print("Please choose from options above.")

def flush(obj):
    """
    Print provided string
    """
    print(obj)

def note(msg):
    """
    Diplay Notes
    """
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))


