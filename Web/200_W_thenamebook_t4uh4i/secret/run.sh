#!/bin/bash

docker container rm -f thenamebook

docker build -t thenamebook .

docker run -d -p 35002:80 --name=thenamebook thenamebook
