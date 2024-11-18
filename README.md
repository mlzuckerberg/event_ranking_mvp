# Event Ranking System MVP

## Overview
This project aims to automate the process of discovering and ranking industry events based on a provided event marketing strategy. The solution uses semantic matching and various criteria (audience, industry, geographic focus, budget) to rank events in terms of relevance to the given strategy. The top-ranked events are then saved in a new JSON file for further analysis.

## Features
- Semantic Matching: Uses word embeddings for semantic similarity between event data and strategy.
- Customizable Scoring: Scoring system that evaluates events based on audience match, industry sector, geographic focus, budget compliance, and event objectives.
- Output: The top 10 ranked events are saved to a new JSON file, including event names, URLs, and relevance scores.

## Files in this Project
1. event_data.py - 
This file contains functions for loading event data and organizing it into a usable format for the ranking process. It reads a JSON file containing event information, such as event name, URL, audience, industry sector, location, and cost.

- Functions:
  - load_event_data(filepath): Loads event data from a JSON file.

2. scoring_logic.py - 
This file contains the logic to score events based on how well they align with the provided marketing strategy. It uses semantic matching (via word embeddings) and evaluates events based on the criteria outlined in the strategy.

- Functions:
  - cosine_similarity_score(text1, text2): Calculates the cosine similarity score between two text strings using word embeddings.
  - score_event(event, strategy): Scores an individual event based on its alignment with the strategy.
  - rank_events(events, strategy): Ranks a list of events based on their relevance to the strategy.

3. main.py - 
The main script that loads the events and strategy data, ranks the events, and outputs the results to a new JSON file.

- Functions:
  - main(): The entry point for the script. Loads event and strategy data, ranks the events, and saves the results to a new file.

4. strategy.json - 
A JSON file that represents the marketing strategy. 
The data in the json file provided here is the result of asking an LLM (ChatGPT in this case) to generate a sample strategy with the prompt "Please generate a sample strategy that an event ranking system could use as input." You could prompt a generative LLM of your choice or use your own json file.
This file includes these fields:
- target_audience: A list of keywords or phrases describing the intended audience.
- objectives: A list of objectives (e.g., lead generation, brand awareness).
- industry_sector: A specific industry sector for which the events should be relevant.
- geographic_focus: A list of geographic locations or regions.
- budget_constraints: A budget range (min and max).
- KPIs: Key performance indicators that are relevant for event selection.


5. events.json - 
A JSON file containing a list of events. 
Note: The data in the json file provided here is the result of asking an LLM (ChatGPT in this case) to generate a sample strategy with the prompt "Please generate a sample json file of events that an event ranking system could use as input, containing details such as name, url, audience, industry, location, and cost ." You could prompt a generative LLM of your choice or use your own json file.
Each event includes these details:
- name: The name of the event.
- url: The URL of the event.
- audience: The target audience of the event.
- industry: The industry sector the event pertains to.
- location: The geographic location of the event.
- cost: The cost of participating in the event.

6. ranked_events.json - 
This is the output file that contains the ranked events. It includes the event names, URLs, and relevance scores based on the provided strategy. 

## How to Run the Project
1. Requirements
- Python 3.x
- spaCy library for word embeddings

2. Installation
- Clone the repository or download the project files.
- Install spaCy: pip install spacy
- Download the en_core_web_md model: python -m spacy download en_core_web_md

3. Running the Project
- Place the following files in the project directory:
  - events.json: A JSON file containing a list of events. 
  - strategy.json: A JSON file representing the event strategy.
  - Run the main script: python main.py
  - This will process the events based on the strategy and save the ranked events to a new file named ranked_events.json.
  - Check the ranked_events.json file for the results. It will contain the event names, URLs, and their relevance scores.
  
## The Scoring Logic
The scoring algorithm evaluates each event based on:
- Audience Match: Semantic similarity between the target audience in the strategy and the event's audience.
- Industry Match: Semantic similarity between the event's industry sector and the strategy's specified sector.
- Geographic Match: Checks if the event's location aligns with the strategy's geographic focus.
- Budget Compliance: Ensures the event's cost is within the strategy's specified budget range.
- Objectives and KPIs: If applicable, objectives like "lead generation" are checked against the event description.
Each factor contributes to the total score, which is used to rank the events.

## Future Improvements
- Refined scoring algorithm: Further refinement could include more advanced semantic matching techniques.
- Extended data sources: Integrating multiple external APIs to gather real-world event data.
- Web scraping: Automatically scrape event data from websites for real-time updates.
