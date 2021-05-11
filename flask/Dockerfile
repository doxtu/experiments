FROM python:3.9.5-alpine

LABEL developer="Nick Gonzales" \
      description="Test flask application for work stuff"

WORKDIR /app

ENV FLASK_APP=/app/app.py
ENV FLASK_ENV=development

# PROD
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install -r requirements.txt

# PROD
# COPY . .

EXPOSE 5000
