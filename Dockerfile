 # change if required

FROM python:latest
LABEL maintainer="bhawick@outlook.com"

WORKDIR /usr/src/workspace
COPY ./workspace/requirements.txt .
COPY ./workspace/setup.py .


RUN pip install jupyter && pip install jupytext
RUN pip install --no-cache-dir -r requirements.txt
