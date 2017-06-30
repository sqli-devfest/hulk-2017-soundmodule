FROM resin/raspberry-pi-python:3.4-slim

LABEL Description="Devfest 2017 Sound module image" Vendor="SQLI" Version="1.0"

RUN apt-get update && apt-get install -y build-essential libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libportmidi-dev

ADD application/requirements.txt application/requirements.txt
WORKDIR /application

RUN pip install -r requirements.txt

ADD application /application

ENV LD_LIBRARY_PATH=/var/lib:/lib:/opt/vc/lib/


CMD /usr/local/bin/python3 soundmodule.py
