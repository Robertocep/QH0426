# firs declaration of function called directions to stores steps
def directions():
    #creating the list inside the decalred functions
    steps = ["move forward", "move backward", " turn left" , "turn right"]
    return steps

# #function declaration

def run_task1():
   print (directions())


def movements():
    path = ["move forward",10, "move backward", 5, " turn left" ,3, "turn right", 1 ]

    return path

def run_task2():
    print("Moving...")
    path = movements()
    # {directions} for {steps} steps
    print(f"{path [0]} for {path [1]} steps")
    print(f"{path [2]} for {path [3]} steps")
    print(f"{path [4]} for {path [5]} steps")
    print(f"{path [6]} for {path [7]} steps")

# for move in range(0, len(movpath), 2):
#     print(movpath[move] + "for" + str(movpath[move+1]) + "steps")

if __name__== "__main__":
    run_task1()
    run_task2()

