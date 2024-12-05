FROM python:3.13.1-alpine

# Ref https://github.com/docker-library/docker/issues/240 we need to explicitly install python
RUN apk --no-cache add --virtual builds-deps build-base python3

RUN mkdir /controller
WORKDIR /controller

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY controller.py .

CMD ["kopf", "run", "controller.py", "--standalone", "--all-namespaces"]
