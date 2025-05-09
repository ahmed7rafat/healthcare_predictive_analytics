from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load saved rules 
with open("apriori_rules.pkl", "rb") as f:
    rules = pickle.load(f)

# Ensure antecedents and consequents are lists
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x))
rules['consequents'] = rules['consequents'].apply(lambda x: list(x))

# Extract all unique symptoms from antecedents 
all_symptoms = set()
for s in rules['antecedents']:
    all_symptoms.update(s)

symptom_list = sorted(list(all_symptoms))

# Flask app setup 
app = Flask(__name__)

# Medical assistant logic 
def medical_assistant(selected_symptom):
    matched = rules[rules['antecedents'].apply(lambda x: selected_symptom in x)]
    
    # Dictionary to hold highest confidence per consequent
    result_dict = {}

    for _, row in matched.iterrows():
        for consequent in row['consequents']:
            if consequent not in result_dict or row['confidence'] > result_dict[consequent]:
                result_dict[consequent] = row['confidence']

    # Convert to sorted list of results
    results = sorted(
        [{"consequents": disease, "confidence": conf} for disease, conf in result_dict.items()],
        key=lambda x: x["confidence"],
        reverse=True
    )

    return results


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    selected = None

    if request.method == 'POST':
        selected = request.form.get('symptom')
        results = medical_assistant(selected)

    return render_template('index.html', symptoms=symptom_list, selected=selected, results=results)

if __name__ == '__main__':
    app.run(debug=True)
