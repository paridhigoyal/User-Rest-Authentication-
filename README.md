
# User Authentication
This project consist of User authentication and authorization consists of User signup , sign in, logout, forget password, update password, profile update using django rest framework.

# Technology Stack
- Python 3.5.2
- Django
- MySQL Database

# Project Strurture
.
├── db.sqlite3
├── manage.py
├── user_authentication_drf_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── user_authentication_drf_project
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py


# Running locally
1.__Create a virtual environment :__ virtualenv venv <br/>
2.__Clone the repo :__   git@github.com:paridhigoyal/User-Rest-Authentication-.git<br/>
3.pip install -r requirements/dev.txt<br/>
4.__Create Database :__  python manage.py migrate<br/>
5.__Create admin :__  python manage.py createsuperuser<br/>
6.__Run project :__  python manage.py runserver.<br/>






