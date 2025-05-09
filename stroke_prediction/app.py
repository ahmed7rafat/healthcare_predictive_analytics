import os
import pickle
import numpy as np
from flask import Flask, render_template, request
from dash7 import init_dashboard


model_path = r'C:\Users\MG\Desktop\stroke_prediction_project1\templates\model.pkl'

# Check if model file exists
if os.path.exists(model_path):
    print("✅ model.pkl exists.")
else:
    print("❌ model.pkl NOT found at the given path.")

# Try to load the model
try:
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    print(f"Error loading the model: {e}")

# Create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    gender = request.form.get("gender")
    age = float(request.form.get("age"))
    hypertension = int(request.form.get("hypertension"))
    heart_disease = int(request.form.get("heart_disease"))
    ever_married = request.form.get("ever_married")
    work_type = request.form.get("work_type")
    residence_type = request.form.get("Residence_type")
    avg_glucose_level = float(request.form.get("avg_glucose_level"))
    bmi = float(request.form.get("bmi"))
    smoking_status = request.form.get("smoking_status")

    features = np.array([[
        age,
        hypertension,
        heart_disease,
        avg_glucose_level,
        bmi,
        1 if gender == "Male" else 0,
        1 if gender == "Other" else 0,
        1 if ever_married == "Yes" else 0,
        1 if work_type == "Never_worked" else 0,
        1 if work_type == "Private" else 0,
        1 if work_type == "Self-employed" else 0,
        1 if work_type == "children" else 0,
        1 if residence_type == "Urban" else 0,
        1 if smoking_status == "formerly smoked" else 0,
        1 if smoking_status == "never smoked" else 0,
        1 if smoking_status == "smokes" else 0
    ]])

    prediction = model.predict(features)[0]
    prediction = "No" if prediction == 1 else "Yes"


    return render_template("index.html", prediction=prediction)

@app.route('/new_page')
def new_page():
    return render_template('new_page.html')

@app.route('/dashboard')
def dashboard():
    return redirect('/dash')



if __name__ == "__main__":
    init_dashboard(app)
    app.run(debug=True)



