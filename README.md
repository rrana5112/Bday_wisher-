# Bday_wisher-

This project is for learning Django filter queries and background task scheduling using celery

We store people's info like Name, DOB, Email and relation type (Family,Friend, Colleague etc) and also the Bday wishes templates (Text only) and schedule a background task for sending wishes on their bdays

The background task will execute exactly on 12:00:00 AM.

To use this project : 

1. Clone this Repo.

2. Create a virtual environment

3. run the command : pip install -r requirements.txt to install the dependency

4. Create a superuser for accessing admin panel. Default credentials : username : rohit, password : 1234

5. use python manage.py runserver to run the project

In wishes model you define the text and category of bday templates. In People model we store person's details whome you want to send wishes.

# TODO : 

1. Add HTML template messages,
2. Allow user to set templates on person basis.
3. Functionality for multiple user to add their data (Access Controls and other user data encryption thing).
