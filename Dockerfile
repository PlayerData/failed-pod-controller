FROM python:3.7.15-alpine

RUN mkdir /controller
WORKDIR /controller

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY controller.py .

CMD ["python", "controller.py"]
