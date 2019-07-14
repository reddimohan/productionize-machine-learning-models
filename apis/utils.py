import os
import yaml

class Utils(object):
    """docstring for Utils."""

    def __init__(self):
        super(Utils, self).__init__()
        self.get_config()

    def upload_file(self, img_object):
        """
        Takes image object as input and saves into uploads folder
        """
        self.uploads = self._get_upload_folder()
        filename = self._get_filename(img_object)
        if not os.path.isdir(self.uploads):
            os.makedirs(self.uploads)

        img_object.save(os.path.join(self.uploads, filename))

        return os.path.join(self.uploads, filename)


    def _get_upload_folder(self):
        upload_folder = self._create_folder(os.path.join(self._get_cwd(), self.config['DOC_UPLOAD_DIR']))
        return upload_folder

    def _create_folder(self, path):
        """
        Takes the path and create the folder if not existed
        """
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True) # to create parent dir
        return path

    def _get_filename(self, img_object):
        return img_object.filename

    def get_config(self):
        """
        Add all your App configuration to config.yml
        """
        self.config = yaml.safe_load(open(os.path.join(self._get_cwd(),"config.yml")))

    def _get_cwd(self):
        return os.getcwd()
