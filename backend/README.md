# SaaS-Study - Backend

## Virtual Environment to develop

``` sh
pip3 install virtualenv

virtualenv venv
```

### Activate Environment
```sh
source ./venv/bin/activate
```

## Django Project

### Install Django
```sh
pip3 install Django
```

### Create Django Project
```sh 
django-admin startproject saas_project
```

### Create Django Application
```sh
mkdir apps/<folder>
python3 manage.py startapp app_name ./apps/<folder>
```

Change apps/app_name/app.py AppConfig name to be "apps.app_name"

Add app to INSTALLED_APPS in the settings.py file as "apps.app_name"

## Dependencies

### Freeze Dependencies
```sh
pip3 freeze > requirements.txt
```

### Install Dependencies
```sh
pip3 install -r requirements.txt
```

## Run Django
```sh
python3 manage.py runserver
```

### Migrate Database
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```