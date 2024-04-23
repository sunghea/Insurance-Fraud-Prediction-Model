from flask import Flask, render_template, request
import pickle
import numpy as np
from pymongo import MongoClient

app = Flask(__name__)

# Load the saved model
with open('models/svc_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.insurance_claims
collection = db.model_test

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index2.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    # Convert the JSON data to numpy array
    features = np.array(data['features']).reshape(1, -1)
    # Make prediction
    prediction = loaded_model.predict(features)
    
    # Store the predictions in MongoDB
    result = {
        "id": data['id'],
        "features": data['features'],
        "prediction": prediction[0]
    }
    collection.insert_one(result)
    
    # Return the prediction as JSON
    return {'prediction': prediction[0]}


if __name__ == '__main__':
    app.run(debug=True)
