

import os
import yaml
import json

from flask_restplus import Namespace, Resource, fields
api = Namespace('Services', description='')
from flask import request, jsonify

from werkzeug.datastructures import FileStorage
import pandas as pd
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

from . import utils

# Import Globally loaded models file here so that we can use them
from . import models as model

"""
Creating a parser obj, so that you can display input form in your API docs
"""
parser = api.parser()
# parser.add_argument('image', type=str, help='Help text', location='form')
parser.add_argument('image', type=FileStorage, help='Upload cat or dog image to classify.', location='files')

@api.route('/')
class ClassName(Resource):
    def __init__(self, host):
        super(ClassName, self).__init__(host)
        self.utils = utils.Utils()
        self._init_models()
        self.config = self.utils.get_config()
        # Add all global configuration in config.yaml so you access it through self.config
        print(self.config)


    @api.doc(parser= parser)
    def post(self):
        """
        request.files Choose an image to classify
        """
        if 'image' not in request.files:
            return api.abort(400, "Select an image to classify", status= "error")

        image_obj = request.files['image']

        self.predict(image_obj)

        return { 'status': 'success', 'prediction': 'work-in-progress' }, 200


    def predict(self, image_obj):
        image_name = self.utils.upload_file(image_obj)

        df = pd.DataFrame({
            "file_name": [image_name]
        })
        nb_samples = df.shape[0]

        batch_size = 1
        IMAGE_WIDTH, IMAGE_HEIGHT = 256, 256
        FAST_RUN = False
        IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
        test_gen = ImageDataGenerator(rescale=1./255)
        test_generator = test_gen.flow_from_dataframe(
            df,
            [image_name],
            x_col='file_name',
            y_col=None,
            class_mode=None,
            target_size=IMAGE_SIZE,
            batch_size=batch_size,
            shuffle=False
        )
        print(nb_samples, batch_size)
        print(np.ceil(nb_samples/batch_size))
        predict = self.model.predict_generator(test_generator, steps=np.ceil(nb_samples/batch_size))
        # predict = self.model.predict_generator(test_generator)
        df['category'] = np.argmax(predict, axis=-1)
        df["category"] = df["category"].replace({0: 'cat', 1: 'dog'})
        print(df)

    def _init_models(self):
        """
        Reading machine learning models from the memory. (We have already loaded models in app_server.py file)
        """
        self.model = model.classifier
        self.graph = model.graph
