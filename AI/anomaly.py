import time
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from pymongo import MongoClient

def process_real_time_data():
    # Connect to the MongoDB database
    client = MongoClient('mongodb://192.168.160.130:27017/')
    db = client['deeplearning_db']
    input_collection = db['valid_csv']
    output_collection = db['valid_packets']
    anomaly_collection = db['anomaly']  # New collection for anomalies

    while True:
        # Retrieve the data from the MongoDB collection
        data = list(input_collection.find({}, {'_id': 0}))

        # Check if there is data to process
        if data:
            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data)
            X = df.drop('ip_source', axis=1)
            

            # Standardize the features (using the same scaler as in the training script)
            scaler = StandardScaler()
            X_test = scaler.fit_transform(X)

            # Load the saved model
            loaded_model = load_model('trained_model_final.h5')

            # Make predictions
            predictions = loaded_model.predict(X_test)
            rounded_predictions = np.round(predictions)

            # Print or use the predictions as needed
            print("Predictions:")
            print(rounded_predictions)

            # Iterate through each prediction and check if the last column is equal to 1
            for i, pred in enumerate(rounded_predictions):
                if pred[-1] == 1:
                    # Append the entire document from the "valid_packets" collection to the "anomaly" collection
                    anomaly_collection.insert_one(data[i])
                    print("Anomaly detected and stored in the MongoDB collection.")

            # Clear the input MongoDB collection
            input_collection.delete_many({})
            print("Input MongoDB collection cleared.")

        else:
            print("No data found in the MongoDB collection. Waiting for new data...")

        # Wait for a certain amount of time before checking again
        time.sleep(1)  # Wait for 1 minute (adjust as needed)

if __name__ == "__main__":
    process_real_time_data()

