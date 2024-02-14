"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""


import matplotlib.pyplot as plt

def chart_pie(parks: dict):
    """
    Show a pie chart based on the data in the provided dictionary.
    
    Parameters:
    - parks (dict): A dictionary containing values for the pie chart.

    Returns:
    None: Displays a pie chart using the data from the dictionary.
    """

    # Creating a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(parks.values(), labels=parks.keys(), autopct='%1.1f%%')
    plt.title('Number of Reviews for Each Park')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

def chart_bar(avg_ratings: dict, legend: str):
    """
    Present a bar chart illustrating the average review scores for each park.

    Parameters:
    - avg_ratings (dict): A dictionary with park names as keys and their corresponding average review scores.
    - legend (str): Legend shown at chart

    Returns:
    None: Displays a bar chart representing the average review scores for each park.
    """

    # Creating a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(avg_ratings.keys(), avg_ratings.values(), color='skyblue')
    plt.title(legend)
    plt.xlabel('Park')
    plt.ylabel('Average Review Score')
    plt.tight_layout()
    plt.show()