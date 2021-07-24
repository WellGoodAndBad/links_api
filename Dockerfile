FROM python:3.8

COPY . /time_links
WORKDIR /time_links
RUN apt-get update && apt-get install -y netcat
RUN pip install -r requirements.txt