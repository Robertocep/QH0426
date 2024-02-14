"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import tui


def average_yearly_park_rating(reviews: list, name: str, rating_year: str):
    """
    Calculates the average yearly rating for a park based on reviews from a specific year.

    Parameters:
    - reviews (list): A list representing park reviews.
    - name (str): The name of the park for which the average rating is to be calculated.
    - rating_year (str): The year for which the average rating is to be calculated.

    Returns:
    str:  The average yearly rating formatted answer.
    """
    temp_list = []
    for rrr in reviews:
        if rrr["branch"].capitalize() == name:
            if rrr["year_month"] is not None:
                if rating_year == rrr["year_month"].split("-")[0]:
                    temp_list.append(rrr["rating"])

    if len(temp_list) > 0:
        average = sum(temp_list)/len(temp_list)
        return f"Average rating for the {name} in the {rating_year} is {average:.2f}"
    else:
        return f"No Ratings for {name} on year {rating_year}"
    
def location_wise_park_reviews(reviews: list, name: str, reviewer_location: str) -> str:
    """
    Fetches a park review based on the provided park name and the reviewer's location.

    Args:
    - reviews (list): A collection representing park reviews.
    - name (str): The name of the park for which a review is requested.
    - reviewer_location (str): The location of the reviewer providing the feedback.

    Returns:
    str: A string containing the review information for the specified park and reviewer's location.
    """

    count = 0
    for rrr in reviews:
        if rrr["branch"].capitalize() == name:
            if rrr["reviewer_location"].capitalize() == reviewer_location:
                count += 1
    output = f"\n{name} park recieved {count} reviews from {reviewer_location}"
    return output


def get_park_reviews(reviews: list, name: str):
    """
    Fetches reviews for a specified park based on its name.

    Args:
    - reviews (list): A collection representing park reviews.
    - name (str): The name of the park for which reviews are requested.

    Returns:
    list: A list of strings containing reviews for the specified park.
    """

    temp_list = []
    for rrr in reviews:
        if rrr["branch"].capitalize() == name:
            output = f'A person from {rrr["reviewer_location"]} left {rrr["rating"]} stars'
            if rrr["year_month"]:
                output += f' on {rrr["year_month"]}'
            temp_list.append(output)
    return temp_list

def reader(path: str):
    """
    Read the given csvfile.
    """
    reviews = []
    # Open the CSV file in read mode with utf-8 encoding.
    with open(path, 'r', encoding="utf-8") as file:
        all_data = file.readlines()
        rows = all_data[1:]
        for row in rows:
            row = row.strip().split(",")
            reviews.append({
                "review_id" : row[0],
                "rating": int(row[1]),
                "year_month": row[2],
                "reviewer_location": row[3],
                "branch": row[4]
            })
        tui.flush("CSV Data successfully loaded.")
        tui.flush(f"Available rows in data are: {len(reviews)}")
        return reviews