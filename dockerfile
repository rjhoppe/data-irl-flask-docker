FROM python:3.11.4-alpine3.18
RUN apk --update add bash nano

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app
RUN chmod a+x main/docker_entry.sh

# start the server
# ENTRYPOINT [ "python" ]
CMD main/docker_entry.sh