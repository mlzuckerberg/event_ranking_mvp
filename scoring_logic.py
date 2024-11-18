"""
Michelle Zuckerberg
November 17, 2024
This file handles scoring and ranking events based on relevance and word embeddings for semantic matching"""

import spacy # a word embedding library
from sklearn.metrics.pairwise import cosine_similarity # for calculating semantic similarity

# Load spaCy's pre-trained word embeddings (this is a medium size model)
nlp = spacy.load("en_core_web_md")

# This function uses spaCy to get the word embedding of a word
def get_embedding(text):
    doc = nlp(text)
    return doc.vector  # Returns the vector representation of the text

# This function calculates the cosine similarity between two word embeddings
def cosine_similarity_score(list1, list2):
    # Join the lists into a single string
    text1 = ' '.join(list1) if isinstance(list1, list) else list1
    text2 = ' '.join(list2) if isinstance(list2, list) else list2

    # Get the word embeddings for each text
    embedding1 = get_embedding(text1).reshape(1, -1)
    embedding2 = get_embedding(text2).reshape(1, -1)

    # Compute and return cosine similarity
    return cosine_similarity(embedding1, embedding2)[0][0]

# This function scores an event based off of points given the events and the strategy, incorporating semantic matching
def score_event(event, strategy):
    score = 0

    # Audience match (semantic matching using embeddings)
    audience_score = 0
    for audience_term in strategy['target_audience']:
        # Compute semantic similarity between audience term and event audience
        audience_score = max(audience_score, cosine_similarity_score(audience_term, event['audience']))

    # Add to total score (normalized, you can adjust this weight)
    if audience_score > 0.5:  # Threshold can be adjusted
        score += 1

    # Industry match (semantic matching using embeddings)
    industry_score = cosine_similarity_score(strategy['industry_sector'], event['industry'])
    if industry_score > 0.5:  # Threshold can be adjusted
        score += 1

    # Geographic match (check if event location matches strategy's geographic focus)
    if any(location in event['location'].lower() for location in strategy['geographic_focus']):
        score += 1

    # Budget compliance (check if the event's cost is within the budget constraints)
    if strategy['budget_constraints']['min'] <= event['cost'] <= strategy['budget_constraints']['max']:
        score += 1

    # Event objectives or KPIs
    if 'lead generation' in [objective.lower() for objective in strategy['objectives']] and \
       'lead generation' in event.get('description', '').lower():
        score += 1

    return score

# This function ranks events based on their relevance score to the strategy
def rank_events(events, strategy):
    scored_events = [(event, score_event(event, strategy)) for event in events]
    scored_events.sort(key=lambda x: x[1], reverse=True)
    return scored_events[:10]
