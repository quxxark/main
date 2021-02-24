Creation of new Django-project:
> django-admin startproject <%PROJECT_DIRECTORY_NAME%>

Creation of new Django-application:
> python3.9 manage.py startapp <%APPLICATION_NAME%>

Start of testing server (localhost:8000 by default):
> ./manage.py runserver 5000

Accept the migrations:
> ./manage.py migrate

PROJECT STRUCTURE:
    urls.py - ROUTING of user's requests
    views.py - request's PROCESSING
    models.py - storing of data in the DB

Add created applications:
blog/blog/settings.py -- INSTALLED_APPS