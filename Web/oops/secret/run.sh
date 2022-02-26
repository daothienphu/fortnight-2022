#!/bin/bash

docker container rm -f oops

docker build -t oops .

docker run -d -p 35001:80 --name=oops oops
