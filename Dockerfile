FROM python:3.8.5

WORKDIR /apps

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src ./