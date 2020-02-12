# DJANGO SIMPLE API CRUD WITH JWT AUTHENTICATION

This sample Create, Retrieve, Update and Delete API with Json Web Token


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

#Create User
First Create user by running the following command from project folder: python manage.py createsuperuser

#Obtain Token
Send a POST request to 'your_ip_address':'selected_port'/obtain_token for example  http://127.0.0.1:8000/obtain_token
and provide json data body, as shown
{
    "username": "***username****",
    "password": "***********",
}

You should get something like {"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'"}
 
#Create
Send a POST request to 'your_ip_address':'selected_port'/api/ for example  http://127.0.0.1:8000/dataapi/
and provide json data body, below is an example
{
    "name": "Daniel Simiyu",
    "email": "sample@gmail.com",
}
 
This is a protected API resource and so you need to attach the obtained token to requests, with an HTTP Authorization header, in the form of:  Bearer <THE_TOKEN>
example "Authorization: Bearer YOUR_JWT_TOKEN"

#Retrive
To read all records, send a GET request to 'your_ip_address':'selected_port'/api/ for example  http://127.0.0.1:8000/dataapi/
To read a single record, send a GET request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/dataapi/2/

This is a protected API resource and so you need to attach the obtained token to requests, with an HTTP Authorization header, in the form of:  Bearer <THE_TOKEN>
example "Authorization: Bearer YOUR_JWT_TOKEN"
#Update
To update a single record, send a PUT request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/dataapi/2/
and provide json data body, below is an example
{
    "name": "John Simiyu",
    "email": "sample@yahoo.com",
}

This is a protected API resource and so you need to attach the obtained token to requests, with an HTTP Authorization header, in the form of:  Bearer <THE_TOKEN>
example "Authorization: Bearer YOUR_JWT_TOKEN"
#Delete
To delete a single record, send a DELETE request to 'your_ip_address':'selected_port'/api/'record_pk' for example  http://127.0.0.1:8000/dataapi/2/

This is a protected API resource and so you need to attach the obtained token to requests, with an HTTP Authorization header, in the form of:  Bearer <THE_TOKEN>
example "Authorization: Bearer YOUR_JWT_TOKEN"
