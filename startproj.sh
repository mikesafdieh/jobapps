### setup project and virtual env
cd ~
mkvirtualenv jobapps -p python3
pip install Django
django-admin startproject career_proj
cd career_proj
./manage.py startapp jobapps
# add `'jobapps.apps.JobappsConfig',` to INSTALLED_APPS in settings.py
# add `path('jobapps/', include('jobapps.urls')),` to urlpatterns in career_proj/urls.py

pip install django-extensions
pip install djangorestframework
# now add `'django_extensions',` and `rest_framework,` to INSTALLED_APPS in settings.py
# also add the below to (the bottom of) settings.py:
# ```
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }
# ```
# (Just some basic defaults for django-rest-framework)

touch jobapps/urls.py
# add an index url
# add an index view
# add some models

### setup the DB
psql
# CREATE DATABASE jobapps OWNER michaelsafdieh;
# \q

# add the following to DATABASES in settings.py:
# ```
# 'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'jobapps',
#     'USER': 'michaelsafdieh',
#     # 'PASSWORD': 'password', # NOTE: no password needed
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
# }
# ```

pip install psycopg2
./manage.py makemigrations jobapps
./manage.py migrate

# go to http://127.0.0.1:8000/jobapps/ in browser to check that initial index page is working properly

pip freeze > ~/career_proj/requirements.txt


