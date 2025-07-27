import streamlit as st
import requests

st.set_page_config(page_title="Math Score Predictor", page_icon="🧮")
st.title("📊 Math Score Predictor")

st.write("Fill in the student details to predict their **Math Score (0–100)**.")

# Input form
with st.form("input_form"):
    gender = st.selectbox("Gender", ["female", "male"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        ["bachelor's degree", "some college", "master's degree",
         "associate's degree", "high school", "some high school"]
    )
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score (0–100)", min_value=0, max_value=100, value=70)
    writing_score = st.number_input("Writing Score (0–100)", min_value=0, max_value=100, value=70)

    submitted = st.form_submit_button("🎯 Predict Math Score")

# Handle form submission
if submitted:
    # Create JSON payload
    payload = {
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation_course,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    api_url = "https://student-score-api.onrender.com/predict"

    # Call the API
    with st.spinner("🔄 Predicting..."):
        try:
            response = requests.post(api_url, json=payload)
            result = response.json()

            # Debug output (optional — remove if not needed)
            st.write("🔎 Raw API Response:", result)

            if response.status_code == 200:
                if "math_score" in result:
                    predicted_score = result["math_score"]
                    st.success(f"✅ Predicted Math Score: **{predicted_score}**")
                else:
                    st.error("❌ Key 'math_score' not found in API response.")
            else:
                st.error(f"❌ API returned status {response.status_code}: {result}")
        except Exception as e:
            st.error(f"⚠️ API request failed: {e}")
