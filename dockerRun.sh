#!/usr/bin/env bash

CONTAINER_NAME=python-addy
echo "****** Setting docker container name as ${CONTAINER_NAME} ******"

IMAGE_NAME=${CONTAINER_NAME}:dev
echo "****** Set docker image name as ${IMAGE_NAME} ******"
PORT=80
echo "****** Set docker image PORT to ${PORT} ******"

echo "****** Stop running Docker containers with image tag ${CONTAINER_NAME}, and remove them ******"
docker stop $(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')
docker rm $(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')

echo "****** Docker build image with name ${IMAGE_NAME} ******"
docker build -t ${IMAGE_NAME} -f Docker/Dockerfile .

echo "****** Run Docker container of the image in detatched mode: ${IMAGE_NAME} with name ${CONTAINER_NAME} ******"
docker run --rm -i -p ${PORT}:${PORT} \
    -e HOST_HOSTNAME=`hostname` \
    --name ${CONTAINER_NAME} \
    ${IMAGE_NAME}