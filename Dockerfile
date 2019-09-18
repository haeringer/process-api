FROM ubuntu:18.04

# Update apt cache and install packages
RUN apt-get update \
  && apt-get install -y python3-pip \
  && pip3 install --upgrade pip

# Copy project files into container
COPY app /opt/system-api
WORKDIR /opt/system-api

# Install project dependencies
RUN pip3 install -r requirements.txt

# Run container as non-root
RUN useradd -ms /bin/bash system-api
USER system-api
