FROM ubuntu:20.04
LABEL INSTANCE_TYPE="hello-world"
MAINTAINER robin.rsu@gmail.com

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONIOENCODING utf-8
ENV PYTHONUNBUFFERED=1

ENV TZ="Asia/Taipei"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install tzdata curl vim && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

## Change TimeZone
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

EXPOSE 5000

# set work directory
WORKDIR /opt

# install dependencies
COPY ./flaskr /opt/flaskr
COPY run.py requirements.txt logging.ini ./
RUN pip install -r requirements.txt
RUN mkdir /opt/logs

ENV FLASK_APP="flaskr"
ENV FLASK_ENV="development"

CMD flask run --host=0.0.0.0 --no-reload

