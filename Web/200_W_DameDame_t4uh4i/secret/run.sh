#!/bin/bash

docker container rm -f damedame

docker build -t damedame .

docker run -d -p 35000:80 --name=damedame damedame
