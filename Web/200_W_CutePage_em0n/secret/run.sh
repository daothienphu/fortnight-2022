#!/bin/bash

cd level1
docker-compose down 
docker-compose up -d --build
cd ../level2
docker-compose down 
docker-compose up -d --build 
cd ../level3
docker-compose down 
docker-compose up -d --build
cd ../level4
docker-compose down 
docker-compose up -d --build
cd ../level5
docker-compose down 
docker-compose up -d --build