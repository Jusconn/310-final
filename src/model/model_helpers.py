from tensorflow import keras
import numpy as np
import os

classes = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

model = None


"""
Initialize the model on API startup then use it for predictions.
"""
def init_model():
    global model
    model_path = os.path.join('src/model', 'fashion_model.h5')
    if os.path.exists(model_path):
        base = keras.models.load_model(model_path)
        model = keras.Sequential([base, keras.layers.Softmax()])

def predict_image(image_data):
    if model is None:
        return {"error": "Model not available"}
    
    predictions = model.predict(image_data, verbose=0)
    idx = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]))
    
    return {
        "class": classes[idx],
        "confidence": f"{confidence:.1%}"
    }
