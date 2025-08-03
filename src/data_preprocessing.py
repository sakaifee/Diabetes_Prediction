import pandas as pd
from sklearn.preprocessing import StandardScaler
from data_loader import load_data 

def preprocess_data(path: str) -> pd.DataFrame:
    # Load data
    df = load_data(path)
    print(df.head())

    # Separate features and labels
    x = df.drop(columns="Outcome", axis=1)
    y = df["Outcome"]
    print(x)
    print(y)

    # Standardize features
    scaler = StandardScaler()
    scaler.fit(x)
    standardized_data = scaler.transform(x)
    print(standardized_data)

    # Taking standardized data and fit in variable "x"
    x = standardized_data
    y = df["Outcome"]
    print(x)
    print(y)

    return x, y

if __name__ == "__main__":
    path = r"C:\Users\ShadanAlamKaifee\Documents\Projects\Diabetes_Prediction\data\diabetes_data.csv"
    df = load_data()
    preprocess_data(path)