FROM python:3.7.4-slim-buster

RUN apt-get update && pip install --upgrade pip
RUN pip install Django
RUN pip install pillow

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]