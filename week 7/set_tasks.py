web_browsers = set()
web_browsers = {"Chrome", "Firefox", "Edge"}
# This function creates and returns a set of observations
def observed():
    # Create a set named observations
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    # The set will automatically remove duplicates
    return observations

# This function calls the observed function and displays the set
def run_task1():
    # Call the observed function and store the returned set
    result = observed()
    # Display the set
    print(result)

# Check if this file is the main program and run task 1
if __name__ == "__main__":
    run_task1()

    # activity 2

    # Initialize a set with tuples representing web browser usage
    web_browser_usage = {("Chrome", 10), ("Firefox", 9), ("Edge", 3)}

    # Add a new tuple to the set
    web_browser_usage.add(("Opera", 1))

    # Remove an existing tuple from the set
    web_browser_usage.remove(("Edge", 3))

    # The set now contains unique tuples without duplicates
    print(web_browser_usage)

    # task

    # This function prompts the user to enter observations and returns a list of these observations
    def observed_items():
        observations = []  # Create an empty list to store observations
        # Prompt the user to enter 7 observations
        for _ in range(7):
            observation = input("Please enter an observation: ")
            observations.append(observation)  # Add the observation to the list
        return observations  # Return the list of observations


    # This function counts the occurrences of each observation and displays the results
    def run_task2():
        print("Counting observations...")  # Display the initial message
        observations = observed_items()  # Call the observed_items function to get the list of observations
        observation_set = set()  # Create an empty set to store unique observations with counts

        # Count the occurrences of each observation and add it to the set as a tuple
        for observation in set(observations):  # Convert list to set to get unique values
            count = observations.count(observation)  # Count the occurrences of the observation
            observation_set.add((observation, count))  # Add the tuple to the set

        # Display the content of the set
        for item in observation_set:
            print(f"{item[0]} observed {item[1]} times.")


    # Check if this file is the main program and run task 2
    if __name__ == "__main__":
        run_task2()
