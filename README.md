# Dream Interpreter

Dream Interpreter is a Flask-based web application that uses AI to interpret dreams. Users can input their dreams, and the application provides meaningful interpretations based on a dataset of dream symbols or generates interpretations using a text-generation model.

## Features

- **Dream Interpretation**: Provides interpretations based on a dataset of common dream symbols.
- **AI-Powered Generation**: Uses the GPT-Neo model to generate interpretations for dreams not found in the dataset.
- **User-Friendly Interface**: A clean and professional web interface for users to input their dreams and view interpretations.

## Project Structure
dream-interpreter/
├── app.py # Main Flask application
├── dream_model.py # Logic for dataset processing and dream interpretation
├── static/
│ └── style.css # CSS for styling the web interface
├── data/
│└── dreams_dataset.csv # Dataset of dream symbols and interpretations
├── templates/ # (Optional) Folder for HTML templates
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Installation

1. **Clone the Repository**:
   git clone https://github.com/your-username/dream-interpreter.git
   cd dream-interpreter

2. **Set Up a Virtual Environment**:
    python3 -m venv dream_interpreter_env
    source dream_interpreter_env/bin/activate

3. **Install Dependencies:**:
    pip install -r requirements.txt

4. **Ensure Dataset is in Place:**:
    Place your dreams_dataset.csv file in the data/ directory.

## Usage

1. **Run the Application**:
    python3 app.py

2. **Access the Web Interface**: 
    Open your browser and navigate to:
    http://127.0.0.1:5000

3. **Input Your Dream**:
    Type your dream into the text box.
    Click the "Interpret" button to receive an interpretation.

## Dependencies

- **Flask**: Web framework for Python.
- **Transformers**: For AI-powered text generation using GPT-Neo.
- **Pandas**: For dataset processing.
- **Torch**: Backend for the Transformers library.

## Dataset

The application uses a dataset of dream symbols and their interpretations. The dataset should be a CSV file with the following columns:

- **Dream Symbol**: The dream symbol or scenario.
- **Interpretation**: The corresponding interpretation.

## Customization

- **Styling**: Modify static/style.css to customize the appearance of the web interface.
- **Dataset**: Update data/dreams_dataset.csv to include additional dream symbols and interpretations.

## Future Enhancements

- Add support for multilingual dream interpretations.
- Integrate with Azure AI services for enhanced text generation.
- Implement user authentication for saving and revisiting dream interpretations.

##Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.