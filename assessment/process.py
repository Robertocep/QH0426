"""
This module is responsible for processing the data.  It will largely contain 
functions that will recieve the overall dataset and perfrom necessary processes 
in order to provide the desired result in the desired format. It is likely that 
most sections will require functions to be placed in this module.
"""
import tui

def avg_rating_by_location(reviews: list):
    """
    Computes the average park rating for each location based on the provided reviews.

    Args:
    - reviews (list): A collection of dictionaries representing park reviews.
      Each dictionary should contain 'location' (str) and 'rating' (float) keys.

    Returns:
    dict: A dictionary with unique locations as keys and their corresponding 
            average ratings from reviews.
    """

    temp_parks = {}

    for rrr in reviews:
        if not rrr["branch"] in temp_parks:
            temp_parks[rrr["branch"]] = {}

        # Fore every review add review to destined park's storage.
        if not rrr["reviewer_location"] in temp_parks[rrr["branch"]]:
            temp_parks[rrr["branch"]][rrr["reviewer_location"]] = [rrr["rating"]]
        else:
            temp_parks[rrr["branch"]][rrr["reviewer_location"]] += [rrr["rating"]]

    # Inside dictionary, calculate average ratings for every city
    for _ , rev_locations in temp_parks.items():
        for loc, rrr in rev_locations.items():
            rev_locations[loc] = sum(rrr) / len(rrr)
    return temp_parks

def monthly_average_reviews(reviews: list, name: str):
    """
    Computes the average monthly reviews for the specified park over the years.

    Args:
    - reviews (list): A collection of dictionaries representing park reviews.
    - park_name (str): The name of the park for which average monthly reviews are computed.

    Returns:
    dict: A dictionary with months as keys and their corresponding average number of reviews \
          for the specified park.
    """

    ratings = {}
    for rrr in reviews:
        if rrr["branch"].capitalize() == name and rrr["year_month"] is not None:
            month = rrr["year_month"].split("-")[1]
            if ratings.get(month) is None:
                ratings[month] = [rrr["rating"]]
            else:
                mon_list = ratings.get(month)
                mon_list.append(rrr["rating"])
                ratings[month] = mon_list

    # Calculate average ratings for each month and sort the dictionary by keys in ascending order
    avg_ratings = {}
    for mm, rrr in ratings.items():
        avg_ratings[mm] = sum(rrr) / len(rrr)
    return dict(sorted(avg_ratings.items(), key=lambda x: int(x[0])))

def top_locations_by_review(reviews: list, name: str):
    """
    Determines the top 10 locations that provided the highest average ratings
    for the specified park.

    Args:
    - reviews (list): A collection of dictionaries representing park reviews.
    - park_name (str): The name of the park for which top review locations are sought.

    Returns:
    dict: A dictionary with locations as keys and their respective average ratings
    for the specified park.
    """

    temp_ratings = {}
    for rrr in reviews:
        if rrr["branch"].capitalize() == name:
            if temp_ratings.get(rrr["reviewer_location"]) is None:
                temp_ratings[rrr["reviewer_location"]] = [rrr["rating"]]
            else:
                temp = temp_ratings.get(rrr["reviewer_location"])
                temp.append(rrr["rating"])
                temp_ratings[rrr["reviewer_location"]] = temp

    # Calculate average ratings for each city
    avg_rrr = {}
    for c, rrr in temp_ratings.items():
        avg_rrr[c] = sum(rrr) / len(rrr)

    # Select top 10 cities and Extract ratings and names for plotting
    ratings = {}
    for c in sorted(avg_rrr, key=avg_rrr.get, reverse=True)[:10]:
        ratings[c] = avg_rrr[c]
    return ratings

def avg_review_score(reviews: list):
    """
    Computes the average review rating for each park based on the provided reviews.

    Args:
    - reviews (list): A collection of dictionaries representing park reviews.

    Returns:
    dict: A dictionary with park names as keys and their corresponding average \
          review ratings as values.
    """

    temp_parks = {}
    for rrr in reviews:
        if temp_parks.get(rrr["branch"]) is None:
            temp_parks[rrr["branch"]] = [rrr["rating"]]
        else:
            review_list = temp_parks.get(rrr["branch"])
            review_list.append(rrr["rating"])
            temp_parks[rrr["branch"]] = review_list

    avg_rrr = {}
    for park in temp_parks.items():
        try:
            avg = sum(park[1])/len(park[1])
            avg_rrr[park[0]] = avg
        except ZeroDivisionError:
            pass
    return avg_rrr

def review_count(reviews: list):
    """
    Creates a dictionary with park names as keys and their respective review counts as values.

    Args:
    - reviews (list): A collection of strings representing park reviews.

    Returns:
    dict: A dictionary mapping park names to the number of reviews each park has received.
    """

    parks = {}
    for rrr in reviews:
        if parks.get(rrr["branch"]) is None:
            parks[rrr["branch"]] = 0
        else:
            parks[rrr["branch"]] = parks.get(rrr["branch"]) + 1
    return parks

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

def location_wise_park_reviews(reviews: list, name: str, reviewer_location: str):
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
                "year_month": row[2] if row[2] != "missing" else None,
                "reviewer_location": row[3],
                "branch": row[4]
            })

        tui.flush("CSV Data successfully loaded.")
        tui.flush(f"Available rows in data are: {len(reviews)}")
        return reviews

class ParkDataExporter:
    """
    ParkDataExporter class aggregates information about parks and saves it in various formats.
    """

    def __init__(self, data):
        """
        Initialize the ParkDataExporter instance.

        Args:
            data: List of Review objects
        """
        self.data = data
        self.output = None

    def create_export_data(self):
        """
        Create a dictionary object containing aggregated park information.

        Returns:
            dict: Aggregated park information
        """
        parks = {}
        for review in self.data:
            if not review["branch"] in parks:
                parks[review["branch"]] = {
                    "No of Reviews": 0,
                    "Number of positive reviews": 0,
                    "Average review score": 0,
                    "Number of countries": set()
                }

            # Increment the number of reviews.
            parks[review["branch"]]["No of Reviews"] += 1

            # Increment the number of positive reviews.
            if review["rating"] >= 4:
                parks[review["branch"]]["Number of positive reviews"] += 1

            # Aggregate review score.
            parks[review["branch"]]["Average review score"] += review["rating"]

            # Add the reviewer's country to the set.
            parks[review["branch"]]["Number of countries"].add(review["reviewer_location"])

        for _, park in parks.items():
            park["Number of countries"] = len(park["Number of countries"])
            park["Average review score"] /= park["No of Reviews"]

        return parks

    def save_as_txt(self):
        """
        Export aggregated park data as TXT.
        """
        output = self.create_export_data()
        with open('parks.txt', 'w', encoding="utf-8") as txt_file:
            for park, data in output.items():
                txt_file.write(f"{park}: {data}\n")
            txt_file.write("")

    def save_as_csv(self):
        """
        Export aggregated park data as CSV.
        """
        output = self.create_export_data()
        with open('parks.csv', 'w', encoding="utf-8") as csv_file:
            header = "Park,No of Reviews,Number of positive reviews,"
            header += "Average review score,Number of countries\n"

            csv_file.write(header)
            for park, data in output.items():
                csv_file.write(f"{park},{data['No of Reviews']},")
                csv_file.write(f"{data['Number of positive reviews']},")
                csv_file.write(f"{data['Average review score']},{data['Number of countries']}\n")

    def save_as_json(self):
        """
        Export aggregated park data as JSON.
        """
        output = self.create_export_data()
        with open('parks.json', 'w', encoding="utf-8") as json_file:
            json_file.write(str(output))
