import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path=r"C:\Users\ShadanAlamKaifee\Documents\Projects\Diabetes_Prediction\data\diabetes_data.csv"):
    df = pd.read_csv(path)
    print(df.head())
    return df

def split_data(df, test_size=0.2, random_state=42):
    x = df.drop(columns=["Outcome"])
    y = df["Outcome"]
    return train_test_split(x, y, test_size=test_size, random_state=random_state)

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train distribution: {y_train.value_counts()}")
