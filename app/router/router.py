from flask import Blueprint, render_template, request
from utils.utils import preproccess_image, model
import numpy as np
from PIL import Image

CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']    

router = Blueprint("main", __name__)

@router.get('/')
def index():
    return render_template('index.html')


@router.post('/predict')
def predict():

    if request.method == 'POST':
        file = request.files['image']
        if file:
            file = Image.open(file.stream)
            file.save('uploaded_image.png')
            image = preproccess_image('uploaded_image.png')

            prediction = model.predict(image)
            predicted_class = CLASSES[np.argmax(prediction)]

            return render_template('result.html', prediction=predicted_class)