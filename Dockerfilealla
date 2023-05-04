# We're using Debian Slim Buster image
FROM python:3.9.6-slim-buster

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Installing Required Packages

ENV PATH="/home/bot/bin:$PATH"

# make directory
RUN mkdir /scarletbot/
COPY . /scarletbot
WORKDIR /scarletbot
RUN pip install telegram

# Install requirements

# Starting Worker
CMD ["python3","-m","scarletbot"]
