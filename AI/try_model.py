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
    collection = db['valid_csv']

    while True:
        # Retrieve the data from the MongoDB collection
        data = list(collection.find({}, {'_id': 0}))

        # Check if there is data to process
        if data:
            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data)

            # Standardize the features (using the same scaler as in the training script)
            scaler = StandardScaler()
            X_test = scaler.fit_transform(df)

            # Load the saved model
            loaded_model = load_model('trained_model_final.keras')

            # Make predictions
            predictions = loaded_model.predict(X_test)
            rounded_predictions = np.round(predictions)

            # Print or use the predictions as needed
            print("Predictions:")
            print(rounded_predictions)

            # Clear the MongoDB collection
            collection.delete_many({})
            print("MongoDB collection cleared.")

        else:
            print("No data found in the MongoDB collection. Waiting for new data...")

        # Wait for a certain amount of time before checking again
        time.sleep(1)  # Wait for 1 minute (adjust as needed)

if __name__ == "__main__":
    process_real_time_data()
