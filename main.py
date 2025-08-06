from fastapi import FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from fastapi import Depends
import secrets
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np
from dotenv import load_dotenv
import os

# Loading environment variable
load_dotenv()

# Load the model
path = os.path.join(
    os.path.dirname(__file__), "models", "diabetes_prediction_model.pkl"
)
with open(path, "rb") as file:
    model = pickle.load(file)

# Initialize FastAPI
app = FastAPI(title="Diabetes Prediction API")
security = HTTPBasic()

# User Authentication
BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")


def authenticates(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, BASIC_AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, BASIC_AUTH_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


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
def predict(data: input_data, username: str = Depends(authenticates)):
    input_array = np.array(
        [
            [
                data.Pregnancies,
                data.Glucose,
                data.BloodPressure,
                data.SkinThickness,
                data.Insulin,
                data.BMI,
                data.DiabetesPedigreeFunction,
                data.Age,
            ]
        ]
    )

    prediction = model.predict(input_array)

    result = "Diabetes" if prediction == 1 else "Non Diabetes"
    return {"prediction": int(prediction), "result": result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
