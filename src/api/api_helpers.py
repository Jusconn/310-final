import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PIL import Image
import numpy as np
import io
from flask import jsonify
from process_image import preprocess_image
from model.model_helpers import predict_image


"""
Handle the prediction request from the Flask API.
This function processes the uploaded image, makes predictions using the model,
and returns the result in JSON format.
"""

def handle_prediction(request):
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    if not file.filename:
        return jsonify({"error": "No file selected"}), 400
    
    try:
        image = Image.open(io.BytesIO(file.read()))
        image_array = np.array(image)
        processed = preprocess_image(image_array)
        result = predict_image(processed)
        
        return jsonify({
            "filename": file.filename,
            "class": result["class"],
            "confidence": result["confidence"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    