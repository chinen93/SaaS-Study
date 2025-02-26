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
django-admin startproject saas
```

### Create Django Application
```sh
python3 manage.py startapp app
```

Add app to INSTALLED_APPS in the settings.py file

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