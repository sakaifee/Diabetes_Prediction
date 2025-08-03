from sklearn.preprocessing import StandardScaler
from data_loader import load_data
from data_preprocessing import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn import svm


def training_data(X_train, Y_train):
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify = Y, random_state=2)
    classifier = svm.SVC(kernel="linear")
    classifier.fit(X_train, Y_train)
    print(classifier)
    print("Model training complete")
    return classifier 

def predict_model(model, X_test, Y_test):
    prediction = model.predict(X_test)
    accuracy = (prediction == Y_test).mean()
    print("Model Accuracy: ", accuracy)
    return prediction

if __name__ == "__main__":
    # Load data
    df = load_data()
    X = df.drop(columns="Outcome", axis=1)
    Y = df["Outcome"]

    # Data standardization
    path = r"C:\Users\ShadanAlamKaifee\Documents\Projects\Diabetes_Prediction\data\diabetes_data.csv"
    preprocess_data(path)

    # Train-test split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify = Y, random_state=2)

    # Train the model
    model = training_data(X_train, Y_train)

    # Model accuracy
    prediction = predict_model(model, X_test, Y_test)

  
