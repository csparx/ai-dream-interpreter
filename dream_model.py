import pandas as pd
from difflib import SequenceMatcher

# Load the dataset
dataset_path = "data/dreams_dataset.csv"
dream_data = pd.read_csv(dataset_path)

def preprocess_dataset(dataset):
    # Drop rows with missing values
    dataset = dataset.dropna(subset=['Dream Symbol', 'Interpretation'])

    # Normalize text (convert to lowercase)
    dataset['Dream Symbol'] = dataset['Dream Symbol'].str.lower()
    dataset['Interpretation'] = dataset['Interpretation'].str.lower()

    return dataset

# Preprocess the dataset
dream_data = preprocess_dataset(dream_data)

def find_interpretation(dream_text):
    # Normalize the input text
    dream_text = dream_text.lower()

    # Find the best match using similarity scoring
    best_match = None
    highest_score = 0

    for _, row in dream_data.iterrows():
        symbol = row['Dream Symbol']
        score = SequenceMatcher(None, symbol, dream_text).ratio()
        if score > highest_score:
            highest_score = score
            best_match = row['Interpretation']

    # Return the best match if the score is above a threshold
    if highest_score > 0.75:  # Adjust the threshold as needed
        return best_match
    return "No matching interpretation found in the dataset."