# sense-hat-docker
Sense-Hat in a docker container

Prerequiste: 
1 - Docker 
2 - ... 

To run the docker:
docker run --device /dev/fb1:/dev/fb1 --device /dev/i2c-1 --device /dev/input/event0 sensors_microservice

To open a shell on the Docker:
docker run -it --rm --device /dev/fb1:/dev/fb1 --device /dev/i2c-1 --device /dev/input/event0 --entrypoint bash sensors_microservice:latest

