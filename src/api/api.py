from flask import Flask, request
from flask_cors import CORS
from api_helpers import handle_prediction
from model.model_helpers import init_model


"""
This file contains the API endpoints for the Fashion-MNIST classifier.
It initializes the model and handles image predictions.
"""

app = Flask(__name__)

CORS(app)

init_model()

@app.route('/predict', methods=['POST'])
def predict():
    return handle_prediction(request)

if __name__ == "__main__":
    app.run(port=5001)
