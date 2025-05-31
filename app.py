from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('calories_model.pkl')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get each input field by name
    gender = int(request.form['gender'])
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heartRate'])
    body_temp = float(request.form['bodyTemp'])

    # Arrange the inputs in the same order your model was trained on
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    
    # Predict using your loaded model
    prediction = model.predict(input_data)

    # Send result back to the template
    return render_template('index.html', prediction_text=f"🔥 You have burnt approximately {prediction[0]:.2f} calories!")


if __name__ == "__main__":
    app.run(debug=True)

