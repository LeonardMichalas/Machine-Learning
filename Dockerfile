FROM python:2.7.9

RUN mkdir -p app

ADD webapp.py /app

WORKDIR /app

RUN pip install flask

EXPOSE 5000

CMD python webapp.py
