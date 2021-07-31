# src-Eakadmik2
Contains the source code for Eakadmik 2 developed during Semester 4th in EAD class.

First Set Up the Database in MySql.  
To install requirements:  
```
pip install requests
pip install Django
pip install mysql-client
pip install mysqlclient
```
  
Then after cloning and setting up the VirtualEnv, run the following commands:
```
python manage.py makemigrations student_management_app
python manage.py migrate
python manage.py runserver
```
  
