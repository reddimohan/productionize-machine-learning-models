# Flask template to productionize Machine learning models

#### Screenshot
![Imgur](https://i.imgur.com/noJ5HDL.png)


#### Required python version
```sh
$ python --version
Python 3.5.5
```

### Flask Library
* Flask-RESTPlus

### Steps to setup
Clone repo ...

```sh
$ git clone https://<your-user-id>@bitbucket.org/productionize-ml-model.git
```

##### Create new virtual env using anaconda
```sh
$ conda create --name <proj_name35> python=3.5
```

##### Activate virtual env
```sh
$ source activate <proj_name35>
```

##### Model
Sample model (the model I used for this tutorial) can be download from the below link. Script that I used to train the model is https://github.com/reddimohan/Custom-image-classification-using-Inception-v3
```sh
Model link: https://1drv.ms/u/s!ArDo8DV9hhHCgTL-SFawrYAmU_DT?e=1TZYw6
```

##### Install libraries

```sh
$ pip install -r requirements.txt
```

##### Run the REST api in local with debug level
```sh
$ cd productionize-ml-model/
$ python app_server.py --debug
```

##### Run API in production mode
```sh
$ gunicorn --bind 0.0.0.0:5000 wsgi:application -w 1
```

##### Digitalocean has very good tutorial on deploying this to nginx, gunicorn so that it accepts multiple requests
```sh
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
```
