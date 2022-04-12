# Hack-a-roo-22

# 1) Front-End Application
## This is the code of front-end of the Application 'EYE-CONIC'. Tech Stack - Angular, Bootstrap, SCSS

## Terminal Commands to run the application

1. Install NodeJs from [NodeJs Official Page](https://nodejs.org/en).
2. Open Terminal
3. Go to your file project
4. Run in terminal: ```npm install -g @angular/cli```
5. Then: ```npm install```
6. And: ```npm start```
7. Navigate to [localhost:4200](localhost:4200)

The naming convention used in the application makes the project self-explanatory. 
Components:
1. Landing Page:
2. Navigation bar
3. License Plate Scan and Results:
4. About the project
5. Team of Eye Conic

Django:

The execution starts at checkImage() when the scan button is clicked on Angular UI. It hits the django port i.e http://127.0.0.1/checkImage API.
We created a flag to check recursively in the output.txt file. Since the MobileNet_V2 takes some time to produce the string of license and place it output.txt, we are required to wait until it is placed. Until then loading screen is loaded on the UI.

Once the recursive check is triggered, we trigger the output.txt file size and sleep for 10 seconds, and check the size again, if the size is increased, it will immediately access the last updated string in the file and perform DB operations to match the license plate in the SQLite 3 database and provide necessary response to the UI. Also, the email service and issue ticket are triggered prior to sending the HttpResonse to the Angular UI. 

In the drone/urls.py, we update the endpoint for the checkImage(). 

Required commands:

python -m pip install django
django-admin startproject <projectName>
django-admin startapp <appname>
python manage.py runserver
After model changes, 
python manage.py makemigrations

and run server. 
If you want to check database tables,
 python manage.py dbshell
python manage.py migrate
