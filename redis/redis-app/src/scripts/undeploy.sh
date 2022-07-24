#!/bin/zsh

# Disconnect containers to common (redis) network
docker network disconnect redis python-docker
docker network disconnect redis redis

docker stop python-docker
docker rm python-docker

# Remove Network
docker network rm redis

echo "[INFO] Application and Network are now stopped"