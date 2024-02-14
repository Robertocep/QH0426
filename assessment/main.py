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
        elif option_main == "B":
            option_b = tui.menu_b()
        elif option_main == "C":
            option_c = tui.menu_c()
        elif option_main == "D":
            break




