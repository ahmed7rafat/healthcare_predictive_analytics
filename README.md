# healthcare_predictive_analytics
An end-to-end data science project that combines stroke prediction and disease association mining using Apriori.
The system provides a predictive form, an interactive dashboard, and an assistant for related disease suggestions — all integrated into a single Flask app.

## 📁 Project Structure  

```bash
healthcare_predictive_analytics/
│
├── app.py                         # Flask app: prediction form, dashboard, Apriori assistant
├── dash7.py                       # Optional standalone dashboard script
├── f1project.ipynb                # Stroke prediction model + EDA
├── f2project.ipynb                # Apriori rule mining on diseases
│
├── healthcare-dataset-stroke-data.csv   # Original raw stroke dataset
├── cleaned_healthcare_data.csv          # Cleaned dataset for stroke prediction
├── disease_transactions_1500.csv        # Dataset for Apriori analysis
│
├── model.pkl                      # Saved stroke prediction model
├── apriori_rules.pkl              # Saved Apriori rules
│
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

```bash
# Clone the repository
git clone https://github.com/ahmed7rafat/healthcare_predictive_analytics.git

# Navigate into the project folder
cd healthcare_predictive_analytics

# Install dependencies
pip install pandas scikit-learn mlxtend flask plotly

# Run the Flask app
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

