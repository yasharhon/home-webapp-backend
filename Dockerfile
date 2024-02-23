# SERVER IMAGE
# Get the base image
FROM python:3.7 AS tornado-server

# Install packages
RUN pip install tornado

# Mount the application code to the image
COPY . project
COPY ./Controls project/Controls

# Set working directory
WORKDIR /project

# Expose port. Necessary?
EXPOSE 8000