#!/bin/bash

docker container rm -f reallysillyalgorithm

docker build -t reallysillyalgorithm .

docker run -d -p 20314:42 --name=reallysillyalgorithm reallysillyalgorithm