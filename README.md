# 🏋️‍♂️ Calorie Burn Prediction Web App

A simple and interactive web application that predicts the **calories burnt** after a workout session using various physical parameters. This app uses a trained **XGBoost Regressor** model and is powered by **Flask** for the backend and HTML/CSS for the frontend.

---

## 🔥 Features

- Predicts calories burnt based on user input
- Clean and responsive UI for a better user experience
- Powered by a machine learning model trained using **XGBoost Regressor**
- Built using Python, Flask, HTML, and CSS

---

## 📌 Use Case

This web app is particularly useful for **gym-goers** and fitness enthusiasts who want to **track calories burnt** after their workout sessions based on their personal body metrics and workout intensity.

---

## 🧠 Input Features

The model takes the following inputs:

- **Gender** 
- **Age** (in years)
- **Height** (in cm)
- **Weight** (in kg)
- **Duration** (in minutes)  
  _→ Total time spent on physical exercises like running, cycling, gym workout, etc._
- **Heart Rate** (in bpm)
- **Body Temperature** (in °C)

---

## ⚙️ Technologies Used

- **Machine Learning Model**: XGBoost Regressor
- **Backend**: Flask
- **Frontend**: HTML + CSS
- **Model Serialization**: `joblib`

---

## Model Details

The model was trained using the XGBoost Regressor, a high-performance gradient boosting algorithm. It delivers accurate predictions even on small datasets with well-tuned hyperparameters.

## Author 
Arpit Gupta (arpit-528)
