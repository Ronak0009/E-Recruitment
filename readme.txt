* * Steps to Execute code: * *

1. Extract the files from the zip file.
2. Open the code folder using Visual Studio Code Editor.
3. For running the code make sure Python 3 and django framework is installed in your system.
4. If you want to install django framework in a virtual enviroment.
   Write the following steps in cmd:
   - pip install virtualenvwrapper-win
   - mkvirtualenv "environment-name" (example-recruitment)
   - pip install django 
5. Install all dependencies from requirements.txt
   - pip install -r requirements.txt
6. Open MySQL Command line Client and enter the following commands:
   - create user 'project1'@'localhost' identified by 'project1';
   - grant all privileges on * . * to 'project1'@'localhost';
   - create database recruitment_project;
7. Now change DATABASES variable in settings.py file according to your MySQL credentials.
8. Now in VS code open terminal and enter this following command:
   - python manage.py makemigrations
   - python manage.py migrate
9. Now by using the following command server will start on port 8000
   - python manage.py runserver
10. Open the following url:
   - 127.0.0.1:8000/main-dashboard