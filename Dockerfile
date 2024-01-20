
FROM python:3.11.6

# setup environment variable
ENV DockerHOME=/home/app/

# set work directory
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy the whole project to your Docker home directory
COPY . $DockerHOME

# run this command to install all dependencies
COPY requirements.txt /home/app/drf_api/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
