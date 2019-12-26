# portfolio
The website is designed by me during my self-learning of the Django. It is a typical design for portfolio website. In this project, the emphasize is given to back-end development of the website rather than the front-end. It has two separate applications called Blog &amp; Jobs. The jobs and blog have object with different methods and variables. They are also  included in that makes it super easy for admin user to upload his/her jobs and blogs in the proper section.



Steps to Visualize the Web:



1. You need to install Python as well as PostGreSQL on your computer to visualize the web. 

2. Setting a localdatabase: 

Then you should make changes to DATABASES of the setting.py >>

It requires user name and the password you have created during installation of PostGreSQL. Additionally, you need to install the Pgadmin to create database with specific name and you need to enter this name next to the "NAME" section. At the end you need to set the localhost and the port according to what is given by PostGresSQL during installation.





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database name',
        'USER':'your user name',
        'PASSWORD':'your password',
        'HOST': 'localhost',
        'PORT': 'your port',
      }
    }
    
    
    
    
    

2. You will also need the connectors between Django and PostGreSQL which are called psycopg2 and pillow. you can use pip tools in python to install them by following command in cmd: 


   pip install psycopg2
   
   
   pip install pillow


3. You need to create migration by writing the following command in cmd:
   python manage.py makemigrations


4. The last stem is migration by writing the following command in the cmd:
   python manage.py migrate
   
   Now you should be able to see the migrated files in your local database. You need to install Pgadmin to see it in your local 
   database.

5. Now open cmd and set your dir to project folder and run the manage.py by python as follow:
   python manage.py runserver

6. Open your browser and browse http://127.0.0.1:8000/
  
Enjoy your browsning ;)  
 

