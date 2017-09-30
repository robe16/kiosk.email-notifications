FROM resin/rpi-raspbian:latest
MAINTAINER robe16

# Port number to listen on
ARG portApplication

# Update
RUN apt-get update && apt-get install -y python python-pip

WORKDIR /message_board

# Bundle app source
COPY src /message_board

# Copy app dependencies
COPY requirements.txt requirements.txt

# Install app dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE ${portApplication}

# Run application
CMD python run.py ${portApplication}