# 🏘️ Real Estate Price Predictor - Streamlit App

Welcome to my first end-to-end Machine Learning project — a **web application** that predicts **real estate price per unit area** based on various property features from the **Taiwan housing market** 📊.

This project is part of my transition from data analysis to machine learning, inspired by Krish Naik Sir's course. I wanted to move beyond theory and apply what I learned in a practical, deployable way — and this is the result!

---

## 🚀 Demo

👉 [Click here to try the live app](https://codewithsayanjib-real-estate-valuation-prediction-app-53mvyl.streamlit.app/) *(replace with your Streamlit link)*  
👉 [View the source code on GitHub](https://github.com/Codewithsayanjib/Real-estate-valuation-prediction)

---

## 📂 Project Structure

- `app.py` → Streamlit UI and prediction logic  
- `Real estate valuation data set.csv` → Dataset from UCI ML Repository  
- `Realestatepredictionproject.ipynb` → Jupyter notebook used for EDA and model training  
- `requirements.txt` → Required libraries for deployment

---

## 📌 Features

- Predicts house price per unit area using:
  - Transaction Date
  - House Age
  - Distance to MRT Station
  - Number of Convenience Stores
  - Latitude & Longitude

- Clean Streamlit interface with sidebar and user input sliders  
- Linear Regression model with preprocessing and feature scaling  
- Deployed live using **Streamlit Cloud**

---

## 📊 Dataset

📌 Source: [UCI Machine Learning Repository – Real estate valuation data set](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set)

- Country: Taiwan 🇹🇼  
- Size: 414 rows × 7 columns  
- Target Variable: `Y house price of unit area`

---

## 🧠 What I Learned

- Implementing regression with real-world data  
- Visualizing correlations and model performance  
- Building interactive ML apps with Streamlit  
- Confidence comes not just from theory, but from shipping real projects!

---

## 🛠️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Codewithsayanjib/Real-estate-valuation-prediction.git
cd Real-estate-valuation-prediction

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
