"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
import process

if __name__ == "__main__":
    
    tui.note("Disneyland Review Analyzer")
    data = process.reader(r"data\disneyland_reviews.csv")

    while True:
        option_main = tui.menu_main()
        
        if option_main == "A":
            option_a = tui.menu_a()
            if option_a == "A":
                pass
            elif option_a == "B":
                pass
            elif option_a == "C":
                pass
            elif option_a == "D":
                pass
            
        elif option_main == "B":
            option_b = tui.menu_b()
            if option_b == "A":
                pass
            elif option_b == "B":
                pass
            elif option_b == "C":
                pass
            elif option_b == "D":
                pass
            
        elif option_main == "C":
            option_c = tui.menu_c()
            if option_c == "A":
                pass
            elif option_c == "B":
                pass
            elif option_c == "D":

        elif option_main == "D":
            break




