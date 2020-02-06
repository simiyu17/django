# DJANGO SIMPLE API CRUD

This sample Create, Retrieve, Update and Delete API

Go to settings.py and update database settings your own mine are shown below

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_api',
        'USER': 'root',
        'PASSWORD': '*********',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#Create
Send a POST request to 'your_ip_address':'selected_port'/api/ for example  http://127.0.0.1:8000/api/
and provide json data body, below is an example
{
    "name": "Daniel Simiyu",
    "email": "sample@gmail.com",
    "contact": "0737546573",
}


#Retrive
To read all records, send a GET request to 'your_ip_address':'selected_port'/api/ for example  http://127.0.0.1:8000/api/
To read a single record, send a GET request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/api/2/

#Update
To update a single record, send a PUT request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/api/2/
and provide json data body, below is an example
{
    "name": "John Simiyu",
    "email": "sample@yahoo.com",
    "contact": "0737546573",
}

#Delete
To delete a single record, send a DELETE request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/api/2/
