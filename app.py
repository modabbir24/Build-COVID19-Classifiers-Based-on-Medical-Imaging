import os
from flask import Flask, render_template, request, send_from_directory
from keras_preprocessing import image
from keras.models import load_model
import numpy as np

import tenserflow as tf
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image


app = Flask(__name__)

STATIC_FOLDER = 'static'
# Path to the folder where we'll store the upload before prediction
UPLOAD_FOLDER = STATIC_FOLDER + '/uploads'
# Path to the folder where we store the different models
MODEL_FOLDER = STATIC_FOLDER + '/models'


def load__model():
    """Load model once at running time for all the predictions"""
    print('[INFO] : Model loading ................')
    global model
    # model = tf.keras.models.load_model(MODEL_FOLDER + '/catsVSdogs.h5')
    model = load_model(MODEL_FOLDER + '/Covid19_XrayDetector.h5')
    global graph
    graph = tf.get_default_graph()
    print('[INFO] : Model loaded')


# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Process file and predict his label
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        fullname = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(fullname)
        xtest_image = image.load_img(fullname, target_size=(224, 224))
        xtest_image = image.img_to_array(xtest_image)
        xtest_image = np.expand_dims(xtest_image, axis = 0)
        result = model.predict_classes(xtest_image)

        if results[0][0] == 0:
            prediction = 'Positive Covid-19'
        else:
            prediction = 'Negative Covid-19'

        return render_template('predict.html', image_file_name=file.filename, label=result)


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


def create_app():
    load__model()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
