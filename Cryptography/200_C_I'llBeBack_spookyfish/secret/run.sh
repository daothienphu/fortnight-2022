#!/bin/bash

docker container rm -f illbeback

docker build -t illbeback .

docker run -d -p 35000:5000 --name=illbeback illbeback