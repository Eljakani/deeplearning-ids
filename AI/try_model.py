import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

def process_real_time_data(csv_file_path):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Assuming the last column is the target variable and the rest are features
    X_test = df.iloc[:, :-1].values
    result = df.iloc[:, -1].values
    result = result.astype(float)
    result = np.resize(result, (len(result), 1))

    # Standardize the features (using the same scaler as in the training script)
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test)

    # Load the saved model
    loaded_model = load_model('trained_model.keras')  # Replace with the correct path if needed

    # Now you can use the loaded model to make predictions on the test data
    predictions = loaded_model.predict(X_test)

    # Assuming binary classification, you may want to round the predictions to 0 or 1
    rounded_predictions = np.round(predictions)

    # Print or use the predictions as needed
    print("Predictions:")
    print(rounded_predictions)

    merged_matrix = np.hstack((rounded_predictions, result))

    print("Merged Matrix (Horizontally):")
    print(merged_matrix)

if __name__ == "__main__":
    # Example usage with real-time data
    while True:
        csv_file_path = input("Enter the path to the CSV file with real-time data (or 'exit' to quit): ")
        if csv_file_path.lower() == 'exit':
            break

        process_real_time_data(csv_file_path)
