# /docker-server/server_dev/Dockerfile
FROM python:3.8  

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim 

RUN mkdir /srv/sProject 
ADD . /srv/sProject 

WORKDIR /srv/sProject 

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]