uv venv - to create virtual environement
.venv\Scripts\activate - to activate virtual environment
uv pip install Django

django-admin startproject firstDjangoProject - (Project name)
cd firstDjangoProject (Project)

python manage.py runserver


----setup complete----
outer firstDjangoProject is the root folder and all folders present in it at sam level of inner firstDjangoProject are root directories

make views.py file in inner project folder

write the cod ein views.py file
then handle the urls in urls.py file

make templates folder in outer project folder - it will have HTML files
make static folder in outer project folder - all css and js will go here

create index.html file in the templates folder

go to settings.py folder and in templates section, mention the templates in DIRs so that views.py can know where templates are present and from where it can get index.html file


----Jinja Template----
We make apps by using manage.py file
command to make app - python manage.py startapp chai   - chai is app name
After running above command, app folder will be made along with some files.
Now, we have to tell our main project that we have made a new app - go to settings.py and in INSTALLED_APPS add the new app name. 

Now in each app, we can have its templates folder where all our html files will be there. According to industry practice, first we have to create template folder in chai app, then inside that template folder we again have to create the fodler with name of our project, then inside that project folder we can create html files. This is industry practice.

Create a html file.
Go to views file in chai app folder and a function to render this file
Create urls.py file in chai app as it is not by default present, and then copy the stuff present in main urls.py file and paste it in chai app urls.py file
Now to create connection between main urls.py file and chai urls.py file, we have to include chai urls.py file in main urls.py file. Define urls in it.

Create a layout.html file in root template folder


---To connect django with tailwind---
First activate virtual environment.
In the outermost or starting folder of the project install tailwind -  uv pip install django-tailwind
Install pip -  python -m ensurepip --upgrade
Run command - python.exe -m pip install --upgrade pip
Install - pip install 'django-tailwind[reload]'
In the setting.py, add 'tailwind' in the apps 
Go to your main project folder -  cd firstDjangoProject
Run command - python manage.py tailwind init
Now we have new theme app created after running this command, add 'theme' in the app section of settings.py
In settings.py add some configurations - 
    TAILWIND_APP_NAME = 'theme'
    INTERNAL_IPS = '127.0.0.1'
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
Install tailwind - python manage.py tailwind install
In the main layout.html file, add - {% load static tailwind_tags %}
                                    {% tailwind_css %}
Tailwind is install but to keep it working we have follow somemore steps -
Open the another terminal and also activate virtual environment in it
cd to main project folder - cd firstDjangoProject
Run command - python manage.py tailwind start
Add another app in settings.py - 'django_browser_reload',
Add middleware in settings.py - 'django_browser_reload.middleware.BrowserReloadMiddleware'
In urls.py add - path("__reload__/", include("django_browser_reload.urls")),
TAILWIND INSTALLED SUCCESSFULLY


---Additional settings---
run - python manage.py migrate



---Extra---
deactivate - to deactivate the virtual environment