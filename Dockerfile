FROM python:3.11.1-alpine

RUN mkdir /controller
WORKDIR /controller

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY controller.py .

CMD ["python", "controller.py"]
