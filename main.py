"""
Michelle Zuckerberg
November 17, 2024
This file is the main file which calls functions from other files"""

import json
from event_data import load_event_data
from scoring_logic import rank_events

# This is the main function
def main():
    # Load events and strategy data
    events = load_event_data('events.json')
    strategy = load_event_data('strategy.json')

    # Rank the events based on the strategy
    ranked_events = rank_events(events, strategy)

    # Prepare the results to write to a new JSON file
    ranked_events_data = []
    for event, score in ranked_events:
        ranked_events_data.append({
            'event_name': event['name'],
            'event_url': event['url'],
            'score': score
        })

    # Write the ranked events to a new JSON file
    with open('ranked_events.json', 'w') as f:
        json.dump(ranked_events_data, f, indent=4)

    print("Ranked events have been saved to 'ranked_events.json'.")

if __name__ == "__main__":
    main()
