 # change if required

FROM python:latest
LABEL maintainer="bhawick@outlook.com"

WORKDIR /usr/src/workspace
COPY ./workspace/requirements.txt .
# network analysis workshop
#COPY ./workspace/setup.py .


RUN apt update && apt-get install -y nodejs && apt-get install -y npm
RUN pip install jupyter && pip install jupyterlab && pip install jupytext
RUN pip install --no-cache-dir -r requirements.txt
