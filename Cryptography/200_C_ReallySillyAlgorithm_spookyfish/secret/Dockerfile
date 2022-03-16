FROM python:3.8-slim-buster
WORKDIR /

COPY ./flag.txt ./flag.txt
COPY ./server.py ./server.py
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt
CMD [ "python3", "server.py" ]