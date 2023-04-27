FROM python:3.11

RUN mkdir /service
WORKDIR /service
COPY service/ /service/
RUN pip install pip -U

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 5000

ENV FLASK_ENV="docker"

CMD ["python", "app.py"] 
