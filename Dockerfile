FROM python:3.11.3-slim-buster

RUN mkdir app
WORKDIR app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "django-start.sh"]