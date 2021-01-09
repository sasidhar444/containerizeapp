FROM python:3.6.5-alpine

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

CMD ["python","server.py"]
