# Student Score Predictor

This project predicts **Math scores of students** using Machine Learning.  
It demonstrates a complete ML workflow: **EDA → Model Training → Web App → Deployment**.  
A Flask web application is built to serve predictions, and the project is deployed on **Microsoft Azure** with continuous delivery from GitHub.

🔗 Live App: [Student Score Predictor](https://student-score.azurewebsites.net/)

---

## Technologies Used:
- Python (3.13)

- Pandas, NumPy, Matplotlib, Scikit-learn (EDA + ML model)

- HTML, CSS (Template for UI)

- Flask (Web App)

- Azure App Service (Deployment)

- GitHub (CI/CD Integration)  

---

## Project Workflow

1. **Dataset & EDA**  
   - Performed exploratory data analysis to understand relationships, distributions, and correlations in the student dataset.  
   - Cleaned and preprocessed the dataset for model training.  

2. **Model Training**  
   - Built a modular pipeline for training.  
   - Used regression algorithms (via Scikit-learn) to predict student Math scores.  
   - Evaluated model performance using metrics such as RMSE and R².  

3. **Web Application (Flask)**  
   - Developed a simple Flask app (`app.py`) where users can input student details and receive predicted Math scores.  

4. **Deployment**  
   - Deployed on **Azure Web App Service**.  
   - Integrated with GitHub for **Continuous Deployment (CD)**.  
   - Any changes pushed to the repository are automatically deployed on Azure.

---

## Diagram describing the Data Flow:
images/data_flow.png

---

## Deployment
- Deployed using Azure Web App Service.

- GitHub repository linked with Azure for continuous delivery.

- Every commit to the main branch triggers automatic deployment.

---

## For running on  localhost:

- Clone the repository: git clone https://github.com/amaan-ali-1107/Student-Score-predictor.git and navigate to the project folder using cd student-Score-predictor.

- Create a virtual environment: python -m venv venv and activate it using     venv\Scripts\activate on Windows or source venv/bin/activate on macOS/Linux.

- Install the required dependencies: pip install -r requirements.txt.

- Run the Flask application: python app.py.

- Open your browser and go to http://127.0.0.1:5000 to use the app locally.