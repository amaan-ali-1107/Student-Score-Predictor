import requests

url = 'https://student-score-api.onrender.com/predict'

data = {
    "gender": "female",
    "race_ethnicity": "group C",
    "parental_level_of_education": "some high school",
    "lunch": "free/reduced",
    "test_preparation_course": "none",
    "reading_score": 17,
    "writing_score": 10
}

response = requests.post(url, json=data)
print(response.json())
