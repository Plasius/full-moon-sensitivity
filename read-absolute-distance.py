from datetime import datetime
import csv
from datetime import datetime
from collections import defaultdict
import json
import os


def read_dates(csv_file_path):
    # Create a list to store parsed dates
    dates = []

    # Read CSV data from the file
    with open(csv_file_path, 'r') as file:
        # Assuming 'Date' is the header in your CSV data
        reader = csv.DictReader(file)
        
        for row in reader:
            # Parse the date string using datetime.strptime
            date_str = row['Date']
            date_obj = datetime.strptime(date_str, '%d-%b-%y')
            
            # Append the parsed date to the list
            dates.append(date_obj)
    
    return dates


day_difference_frequency = defaultdict(int)

def find_closest_date_frequency(random_date_obj, dates):
    #random_date_obj = datetime.strptime(random_date, '%d-%b-%Y')
    min_day_difference = float('inf')

    # Iterate through the dates to find the closest date
    for date_obj in dates:
        day_difference = abs((date_obj - random_date_obj).days)
        min_day_difference = min(min_day_difference, day_difference)

    # Add the minimal day difference to the frequency dictionary
    day_difference_frequency[min_day_difference] += 1


# Print the list of parsed dates
#find_closest_date_frequency('26-Dec-2023')

dates = read_dates('/Users/plasius/Desktop/full_moons.csv')

#repeat for all json files
    #loop through the messages of one json
        #call find_closest_date_frequency
        
fileIndex = 0        

for filename in os.listdir('/Users/plasius/Desktop/messages'):
    if filename.endswith(".json"):
        json_file_path = os.path.join('/Users/plasius/Desktop/messages', filename)
        
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            messages = data.get('messages', [])

            # Extract and print the dates from messages
            for message in messages:
                timestamp_ms = message.get('timestamp_ms', 0)
                date_obj = datetime.utcfromtimestamp(timestamp_ms / 1000.0)
                find_closest_date_frequency(date_obj, dates)
                
        fileIndex+=1
        print(fileIndex, 1121, float(fileIndex/1121))
        

print(day_difference_frequency)