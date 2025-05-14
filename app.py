from flask import Flask, request, jsonify, render_template_string
from transformers import pipeline, set_seed
import logging
from dream_model import find_interpretation  # Import the function from dream_model

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load GPT-Neo model
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
set_seed(42)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Dream Interpreter</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="container">
        <h1>AI Dream Interpreter</h1>
        <p>Ever wake up from a dream and wonder what it meant?
Enter the details of your dream below, and our AI will help interpret the symbols, themes, and emotions that may be hiding beneath the surface.</p>
        <textarea id="dreamInput" rows="4" cols="50" placeholder="Type your dream here..."></textarea><br>
        <button onclick="interpretDream()">Interpret</button>
        <h2 id="interpretation-title" style="display:none;">Interpretation:</h2>
        <p id="interpretation" style="display:none;"></p>

        <script>
            async function interpretDream() {
                const dreamText = document.getElementById('dreamInput').value;
                if (!dreamText) {
                    alert("Please enter a dream!");
                    return;
                }

                // Hide interpretation before submitting
                document.getElementById('interpretation-title').style.display = 'none';
                document.getElementById('interpretation').style.display = 'none';

                const response = await fetch('/interpret', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ dream: dreamText }),
                });

                const result = await response.json();
                document.getElementById('interpretation').innerText = result.interpretation || 'No interpretation generated.';
                document.getElementById('interpretation-title').style.display = 'block';
                document.getElementById('interpretation').style.display = 'block';
            }
        </script>
        </div>
    </body>
    </html>
    """)

@app.route('/interpret', methods=['POST'])
def interpret():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 415

    data = request.get_json()
    dream_text = data.get('dream')

    if not dream_text:
        return jsonify({'error': 'Dream text is required'}), 400

    try:
        # First, try to find an interpretation in the dataset
        interpretation = find_interpretation(dream_text)
        if interpretation == "No matching interpretation found in the dataset.":
            # If no match is found, use the generator
            prompt = (
                f"Please provide a meaningful and concise interpretation of the following dream based on common dream symbols and psychological insights:\n\n"
                f"Dream: {dream_text}\n\n"
                f"Interpretation:"
            )
            result = generator(prompt, max_length=200, num_return_sequences=1)

            # Validate the result
            if not result or 'generated_text' not in result[0]:
                logging.error("Unexpected output format from the generator.")
                return jsonify({'error': 'Failed to generate an interpretation. Please try again.'}), 500

            # Extract the interpretation
            generated_text = result[0]['generated_text']
            if "Interpretation:" in generated_text:
                interpretation = generated_text.split("Interpretation:")[1].strip()
            else:
                interpretation = generated_text.strip()

        return jsonify({'interpretation': interpretation})
    except Exception as e:
        logging.error(f"Error during dream interpretation: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
