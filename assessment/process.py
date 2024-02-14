"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import tui

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