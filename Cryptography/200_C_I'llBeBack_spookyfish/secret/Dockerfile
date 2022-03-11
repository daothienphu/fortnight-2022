FROM python:3.8-slim-buster
WORKDIR /

COPY ./flag.txt ./flag.txt
COPY ./encrypt.py ./encrypt.py

CMD [ "python3", "encrypt.py" ]