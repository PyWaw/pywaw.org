FROM python:3.6.4

RUN pip install uwsgi==2.0.15

ADD /requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD / /app

WORKDIR /app/pywaw

CMD ../containers/run.sh