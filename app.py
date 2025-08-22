from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app= Flask(__name__)

# ---------------- Home Page ----------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------- Web Form Prediction ----------------
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),  # Kept same as before
                writing_score=float(request.form.get('reading_score'))
            )

            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=int(results[0]))

        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")

# ---------------- API Endpoint for JSON Requests ----------------
@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        content = request.get_json()

        # Check if all required fields exist
        required_fields = [
            "gender", "race_ethnicity", "parental_level_of_education",
            "lunch", "test_preparation_course", "reading_score", "writing_score"
        ]
        for field in required_fields:
            if field not in content:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Create data object
        data = CustomData(
            gender=content['gender'],
            race_ethnicity=content['race_ethnicity'],
            parental_level_of_education=content['parental_level_of_education'],
            lunch=content['lunch'],
            test_preparation_course=content['test_preparation_course'],
            reading_score=float(content['reading_score']),
            writing_score=float(content['writing_score'])
        )

        # Predict
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return jsonify({"math_score": int(results[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
        