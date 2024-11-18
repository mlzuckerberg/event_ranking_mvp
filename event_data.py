# Author: Michelle Zuckerberg
# Date: November 17, 2024
# Desciption: This file handles fetching event data from a json file.

import json

# This function loads the event data from a json file, returning a list of event dictionaries to their details
def load_event_data(filename):
    with open(filename, 'r') as file:
        events = json.load(file)
    return events

# This function saves the event data to a json file
def save_event_data(events, filename):
    with open(filename, 'w') as file:
        json.dump(events, file, indent=4)
