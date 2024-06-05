FROM python:3.10

WORKDIR /social

RUN pip install --upgrade pip
COPY requirements.txt /social
RUN pip install -r requirements.txt

COPY . /social

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]