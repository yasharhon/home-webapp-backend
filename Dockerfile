# SERVER IMAGE
# Get the base image
FROM python:3.7 AS tornado-server

# Install packages
RUN pip install tornado jsonpickle

# Mount the application code to the image
COPY . project
COPY ./Controls project/Controls

# Mount and install packages
COPY packages project/packages
RUN pip install project/packages/*.whl

# Set working directory
WORKDIR /project

# Expose port. Necessary?
EXPOSE 8000