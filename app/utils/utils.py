from keras.models import load_model
import os
from PIL import Image
import numpy as np

def preproccess_image(image_file):
    """
    Preprocess the image file for model input.
    
    Args:
        image_file: The image file to preprocess.
        
    Returns:
        A preprocessed image ready for model input.
    """
    
    # Open the image file
    with Image.open(image_file) as img:
        # Resize the image to a fixed size (e.g., 224x224)
        img = img.resize((32, 32))
        # Convert the image to RGB if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Convert the image to a numpy array
        img_array = np.array(img)
        # Normalize the pixel values to [0, 1]
        img_array = img_array / 255.0
        
        img = img_array.reshape(1, 32, 32, 3)  # Reshape for model input

    return img


path = os.path.dirname("...")
print(f"Diretório atual: {path}")
model = load_model(os.path.join('models', 'cifar10_model.keras'))