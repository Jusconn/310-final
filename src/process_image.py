from PIL import Image
import numpy as np

#makes image compatible with model
def preprocess_image(img_array):
    # Convert to grayscale if needed
    if len(img_array.shape) == 3:
        img_array = np.mean(img_array, axis=2)
    
    # Resize to 28x28
    if img_array.shape != (28, 28):
        img = Image.fromarray(img_array.astype('uint8'))
        img = img.resize((28, 28))
        img_array = np.array(img)
    
    # Invert and normalize
    img_array = 255 - img_array
    img_array = img_array / 255.0
    
    return img_array.reshape(1, 28, 28)


"""
The above function was AI generated to preprocess images to be compatible with the Fashion-MNIST model.
It converts the image to grayscale, resizes it to 28x28 pixels, inverts the colors, normalizes 
the pixel values to the range [0, 1], and adds a batch dimension.
This is necessary because the Fashion-MNIST model expects input images in this specific format.
The function handles both RGB and grayscale images, ensuring that the input is always a single-channel image
with the correct dimensions.
"""