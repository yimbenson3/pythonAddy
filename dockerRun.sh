#!/usr/bin/env bash

CONTAINER_NAME=python-addy
echo "****** Setting docker container name as ${CONTAINER_NAME} ******"

IMAGE_NAME=${CONTAINER_NAME}:dev
echo "****** Set docker image name as ${IMAGE_NAME} ******"
PORT=5000
echo "****** Set docker image PORT to ${PORT} ******"

echo "****** Create target jar******"
mvn clean package

echo "****** Stop running Docker containers with image tag ${CONTAINER_NAME}, and remove them ******"
docker stop $(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')
docker rm $(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')

echo "****** Docker build image with name ${IMAGE_NAME} ******"
docker build -t ${IMAGE_NAME} -f Docker/Dockerfile .

echo "****** Run Docker container of the image in detatched mode: ${IMAGE_NAME} with name ${CONTAINER_NAME} ******"
docker run -d --rm -i -p ${PORT}:${PORT} \
    --name ${CONTAINER_NAME} \
    ${IMAGE_NAME}