from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
model_path = r"C:\Users\ShadanAlamKaifee\Documents\Projects\Diabetes_Prediction\models\diabetes_prediction_model.pkl"
with open (model_path, 'rb') as file:
    model = pickle.load(file)

# Initialize FastAPI
app = FastAPI(title = "Diabetes Prediction API")

# Input Schema
class input_data(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: int
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# API endpoints
@app.post("/predict")
def predict(data: input_data):
    input_array = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness, data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age]])

    prediction = model.predict(input_array)

    result = "Diabetes" if prediction == 1 else "Non Diabetes"
    return {"prediction": int(prediction), "result": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)