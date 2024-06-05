# Social Network

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/harish-work/social-network.git
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
```

## Screenshots
1. Login.
![image](https://github.com/harish-work/social-network/assets/163814679/c22da97a-18e3-4ee1-9262-1a8a53be1620)

2.Get all accpected friends list.
!note to pass the token the header.
![image](https://github.com/harish-work/social-network/assets/163814679/68dc396c-c238-48d6-a686-2fa8dcb53672)

3.Get all pending friend request.
!note to pass the token the header.
![image](https://github.com/harish-work/social-network/assets/163814679/937a0f84-8198-43b9-827f-f77c907be72f)

4.Seacrh all users.
!note to pass the token the header.
![image](https://github.com/harish-work/social-network/assets/163814679/108f6fbf-7dc4-45a3-b1df-f71b637a9b62)


