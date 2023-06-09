# ------------------Creating Project------------------
'''
1. Create a folder for the project
run the following command in the terminal:
django-admin startproject mysite
now you will see a folder named mysite with a bunch of files in it

2. Create a development server
run the following command for that in the terminal by keeping in mind that you are in outer mysite folder:
py manage.py runserver
now you will see a url in the terminal

3. Create an app
run the following command for that in the terminal by keeping in mind that you are in outer mysite folder:
py manage.py startapp myapp
now you will see a folder named myapp with a bunch of files in it

4. Create a view
myapp/views.py:
#Create a view:
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World!")

#call the view:
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = 'index'),
]

5. Create a url
mysite/urls.py:
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("myapp/", include("myapp.urls")),
    path('admin/', admin.site.urls),
]

6. Database setup
run the following command:
python manage.py migrate

7. Create models

8. Activate models
add the app name in the INSTALLED_APPS list in settings.py
run the following command:
python manage.py makemigrations myapp

in summary:
-Change your models (in models.py).
-Run python manage.py makemigrations to create migrations for those changes
-Run python manage.py migrate to apply those changes to the database.


'''