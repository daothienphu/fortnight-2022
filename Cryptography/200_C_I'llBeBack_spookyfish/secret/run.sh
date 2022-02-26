#!/bin/bash

docker container rm -f illbeback

docker build -t illbeback .

docker run -d -p 20302:69 --name=illbeback illbeback