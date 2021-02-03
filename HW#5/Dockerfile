FROM python:3.7
RUN apt-get update && apt-get install -y python python-pip
RUN pip install flask
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY docker.py ./HW#5/
ENTRYPOINT FLASK_APP=/HW#5/docker.py flask run --host=0.0.0.0 --port=8080
