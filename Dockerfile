FROM python:3.12.0-alpine

RUN mkdir /controller
WORKDIR /controller

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY controller.py .

CMD ["kopf", "run", "controller.py", "--standalone", "--all-namespaces"]
