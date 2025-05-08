# dream_model.py

from transformers import pipeline, set_seed

# Load a text generation pipeline using GPT-2
generator = pipeline('text-generation', model='gpt2')
set_seed(42)  # Optional: ensures reproducibility

def interpret_dream(prompt, max_length=100):
    """
    Generates a dream interpretation based on the input prompt.
    """
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result
