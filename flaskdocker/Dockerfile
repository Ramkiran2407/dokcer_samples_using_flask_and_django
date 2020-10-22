FROM python:3.8

# set the working directory in the container
COPY . /flask
WORKDIR /flask 

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
# COPY flaskdocker
EXPOSE 5001
# command to run on container start
ENTRYPOINT ["python"]
CMD [ "app.py" ]
