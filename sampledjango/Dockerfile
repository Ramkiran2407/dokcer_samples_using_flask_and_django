FROM python:3.8

# set the working directory in the container
COPY . /django
WORKDIR /django 

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory

# EXPOSE 8000
# command to run on container start
ENTRYPOINT ["python"]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]
