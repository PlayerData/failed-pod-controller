FROM python:3.11.0-alpine

RUN mkdir /controller
WORKDIR /controller

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY controller.py .

CMD ["python", "controller.py"]
