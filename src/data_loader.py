import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path=r"C:\Users\ShadanAlamKaifee\Documents\Projects\Diabetes_Prediction\data\diabetes_data.csv"):
    df = pd.read_csv(path)
    print(df.head())
    return df

if __name__ == "__main__":
    df = load_data()
  