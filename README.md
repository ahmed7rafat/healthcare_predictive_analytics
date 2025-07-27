# healthcare_predictive_analytics
An end-to-end data science project that combines stroke prediction and disease association mining using Apriori.
The system provides a predictive form, an interactive dashboard, and an assistant for related disease suggestions — all integrated into a single Flask app.

📁 Project Structure
.
├── app.py                         # Flask app: prediction form, dashboard, and Apriori assistant
├── dash7.py                       # Optional dashboard visualization
├── f1project.ipynb                # Stroke prediction model + EDA
├── f2project.ipynb                # Apriori rule mining on diseases
├── healthcare-dataset-stroke-data.csv   # Original stroke dataset (raw)
├── cleaned_healthcare_data.csv    # Stroke prediction dataset
├── disease_transactions_1500.csv  # Dataset for Apriori
├── model.pkl                      # Stroke prediction model
├── apriori_rules.pkl              # Saved rules from Apriori
├── templates/                     # Flask HTML templates
└── README.md

🚀 Key Features
- 🧠 Predict stroke risk using a trained machine learning model
- 📊 Interactive dashboard with visual insights for stroke dataset
- 🤖 Assistant powered by Apriori that suggests related diseases
- 🌐 All features are integrated into one Flask application

🛠️ Tech Stack
- Python
- Pandas, Scikit-learn, Mlxtend
- Flask, Dash, Plotly
- Jupyter Notebook

📦 How to Clone and Run
git clone https://github.com/ahmed7rafat/healthcare_predictive_analytics.git
cd healthcare_predictive_analytics

pip install pandas scikit-learn mlxtend flask plotly

python app.py

📚 Notebooks
- f1project.ipynb → EDA and ML model for stroke prediction
- f2project.ipynb → Apriori rule mining on disease transactions

📊 Datasets
- healthcare-dataset-stroke-data.csv → Original stroke dataset (raw)
- cleaned_healthcare_data.csv → Stroke prediction dataset
- disease_transactions_1500.csv → Apriori dataset for disease associations

🤖 app.py Overview
- Predictive Form: Accepts patient data to predict stroke using the ML model
- Dashboard: Displays stroke data insights using visualizations
- Assistant: User selects a disease to view other associated conditions using Apriori

