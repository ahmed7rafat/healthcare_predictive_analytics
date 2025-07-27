import os
import pickle
import numpy as np
from flask import Flask, render_template, request, redirect
from dash7 import init_dashboard
import pandas as pd

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Load Apriori rules
rules_path = os.path.join(os.path.dirname(__file__), 'apriori_rules.pkl')
rules = pickle.load(open(rules_path, 'rb'))
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x))
rules['consequents'] = rules['consequents'].apply(lambda x: list(x))

# Extract symptoms
all_symptoms = set()
for s in rules['antecedents']:
    all_symptoms.update(s)
symptom_list = sorted(list(all_symptoms))

def medical_assistant(selected_symptom):
    matched = rules[rules['antecedents'].apply(lambda x: selected_symptom in x)]
    result_dict = {}
    for _, row in matched.iterrows():
        for consequent in row['consequents']:
            if consequent not in result_dict or row['confidence'] > result_dict[consequent]:
                result_dict[consequent] = row['confidence']
    return sorted(
        [{"consequents": disease, "confidence": conf} for disease, conf in result_dict.items()],
        key=lambda x: x["confidence"],
        reverse=True
    )

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

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    results = []
    selected = request.args.get('symptom') if request.method == 'GET' else request.form.get('symptom')
    if selected:
        results = medical_assistant(selected)
    return render_template('chatbot.html', symptoms=symptom_list, selected=selected, results=results)

@app.route('/dashboard')
def dashboard():
    return redirect('/dash')

if __name__ == "__main__":
    init_dashboard(app)
    app.run(debug=True)
