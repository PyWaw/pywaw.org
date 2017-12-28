FROM python:3.6.4

ADD /requirements /app/requirements

RUN pip install -r /app/requirements/production.txt

ADD / /app

WORKDIR /app/pywaw

CMD ../containers/run.sh