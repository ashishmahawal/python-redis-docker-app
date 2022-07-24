# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /code
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]