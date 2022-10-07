FROM python:3.9


RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

RUN python manage.py makemigrations \
    && python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]