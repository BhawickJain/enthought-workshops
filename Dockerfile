 # change if required

FROM python:latest
LABEL maintainer="bhawick@outlook.com"

WORKDIR /usr/src/workspace
COPY ./workspace/requirements.txt .
# network analysis workshop
#COPY ./workspace/setup.py .


# Install node via NPM
# see https://github.com/jupyterlab/jupyterlab/issues/4327
RUN apt update && apt-get install -y npm
RUN npm install -g npm

# Install Jupyter
RUN pip install jupyter && pip install jupyterlab && pip install jupytext
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
