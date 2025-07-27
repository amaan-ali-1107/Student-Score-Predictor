from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

# Set paths relative to current script location
ARTIFACTS_PATH = os.path.join(os.path.dirname(__file__), 'artifacts')

# Load preprocessor and model
with open(os.path.join(ARTIFACTS_PATH, 'preprocessor.pkl'), 'rb') as f:
    preprocessor = pickle.load(f)

with open(os.path.join(ARTIFACTS_PATH, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Math Score Prediction API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Convert JSON to DataFrame
        input_df = pd.DataFrame([data])

        # Preprocess the input
        transformed_input = preprocessor.transform(input_df)

        # Predict using the model
        prediction = model.predict(transformed_input)

        return jsonify({
            'math_score': int(prediction[0])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
