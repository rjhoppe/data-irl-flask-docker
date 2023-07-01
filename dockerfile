FROM ubuntu:22.04
# RUN apt-get -y update && apt-get -y upgrade
# RUN apt-get -y install wget
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
#     apt-get -y install ./google-chrome-stable_current_amd64.deb

RUN apt-get -y update && apt-get -y upgrade
RUN apt -f install -y
RUN apt-get install -y wget

# Install Google Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN apt-get -y install python3.11 &&\
    apt-get -y install python3-pip
RUN apt-get -y install nano

# Install Chrome Driver
RUN apt-get install -yqq unzip
# The driver info is hardcoded and may needed to be updated over time - driver and chrome version must match
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/app/chromedriver/

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app
RUN chmod a+x main/docker_entry.sh

# start the server
# ENTRYPOINT [ "python" ]
CMD main/docker_entry.sh