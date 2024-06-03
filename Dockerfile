FROM python:3.10

WORKDIR /social

RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /social

RUN python manage.py makemigrations
RUN python manage.py migrate