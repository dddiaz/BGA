#FROM ubuntu:latest
FROM python:3-onbuild
MAINTAINER Daniel Diaz "daniel.delvin.diaz@gmail.com"
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
# We copy just the requirements.txt first to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#COPY . /app

# specify the port number the container should expose
# EXPOSE 5000


ENTRYPOINT ["python"]
CMD ["app.py"]
