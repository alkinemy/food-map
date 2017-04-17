FROM python:3-alpine

MAINTAINER joke111 <alta.second@gmail.com>

# Update system
RUN apk upgrade --no-cache

# Prepare app environment
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir -r Pipfile.lock.txt

#ENTRYPOINT ["python", "run.py"]