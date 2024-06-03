# Social Network

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/harish-work/vendor_management.git
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ virtualenv social-env
$ source env/bin/activate
```
Then install the dependencies:
```sh
(social-env)$ pip install -r requirements.txt
```
## Getting Started
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
