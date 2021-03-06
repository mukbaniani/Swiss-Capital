FROM python:3.8.5
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .