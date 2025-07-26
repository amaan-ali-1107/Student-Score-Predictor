import requests

url = 'http://127.0.0.1:5000/predict'

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
