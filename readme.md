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


---Extra---
deactivate - to deactivate the virtual environment