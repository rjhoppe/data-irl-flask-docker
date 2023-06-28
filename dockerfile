FROM python:3.11.4-alpine3.18

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . app/

# start the server
CMD CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
