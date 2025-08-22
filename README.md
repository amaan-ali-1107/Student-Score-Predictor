# Student Score Predictor 🎓📊

This project predicts **Math scores of students** using Machine Learning.  
It demonstrates a complete ML workflow: **EDA → Model Training → Web App → Deployment**.  
A Flask web application is built to serve predictions, and the project is deployed on **Microsoft Azure** with continuous delivery from GitHub.

🔗 Live App: [Student Score Predictor](https://student-score.azurewebsites.net/)

---

## 📌 Project Workflow

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

## 📂 Project Structure

student_score_predictor/
│── app.py # Flask web application
│── requirements.txt # Python dependencies
│── setup.py # Setup script (for packaging/deployment)
│── README.md # Project documentation
│── .gitignore # Ignore files for Git

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd student_score_predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app locally:

bash
Copy
Edit
python app.py
Visit in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000/
▶️ Usage
Enter student details in the web app form.

Submit to get the predicted Math score.

Example:

Input Features (Student)	Predicted Math Score
Gender: Male, Study Hours: 5, Test Prep: Yes	78

🛠 Tech Stack
Python (3.x)

Pandas, NumPy, Scikit-learn (EDA + ML model)

Flask (Web App)

Azure App Service (Deployment)

GitHub (CI/CD Integration)

🚀 Deployment
Deployed using Azure Web App Service.

GitHub repository linked with Azure for continuous delivery.

Every commit to the main branch triggers automatic deployment.

🙌 Acknowledgments
This project was built as part of a Machine Learning learning journey to practice:

Exploratory Data Analysis (EDA)

Model Training & Evaluation

Flask Web Development

Cloud Deployment (Azure) & CI/CD

