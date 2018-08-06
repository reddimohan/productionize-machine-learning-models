# Flask template to productionize Machine learning models
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
