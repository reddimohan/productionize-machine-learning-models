

import os
import yaml
import json

from flask_restplus import Namespace, Resource, fields
api = Namespace('Services', description='')
from flask import request, jsonify

from werkzeug.datastructures import FileStorage

# Import Globally loaded models file here so that we can use them
from . import models as model

"""
Creating a parser obj, so that you can display input form in your API docs
"""
parser = api.parser()
parser.add_argument('sample_text', type=str, help='Help text', location='form')
parser.add_argument('file', type=FileStorage, location='files')

@api.route('/')
class ClassName(Resource):
    def __init__(self, host):
        super(ClassName, self).__init__(host)
        self._init_models()
        self.config = self._get_config()
        # Add all global configuration in config.yaml so you access it through self.config
        print(self.config)

    @api.doc(parser= parser)
    def post(self):
        """
        request.form will give you the text input parameters sent by user
        request.files to receive files sent by user
        """
        print(request.form)
        if 'sample_text' not in request.form:
            return api.abort(400, "Input sample text required", status= "error")

        print(self.model)

        return { 'status': 'success', 'data': request.form['sample_text'] }, 200

    def _init_models(self):
        """
        Reading machine learning models from the memory. (We have already loaded models in app_server.py file)
        """
        self.model = model.model_data
        self.graph = model.graph


    def _get_config(self):
        """
        Add all your App configuration to config.yml
        """
        config = yaml.safe_load(open(os.path.join(self._get_cwd(),"config.yml")))
        return config

    def _get_cwd(self):
        """
        Get your current working dir
        """
        return os.getcwd()
