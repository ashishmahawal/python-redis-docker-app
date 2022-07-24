#!/bin/zsh
cwd=$(pwd)
source ${cwd}/scripts/undeploy.sh
docker stop python-docker
docker rm python-docker

# Create Network Bridge -- redis
docker network create redis
echo "[INFO] Created Docker Network Bridge --> redis"

# Run container in detached mode and publish at http://localhost:8000
docker run --name=python-docker -d -p 8000:5000 python-docker
echo "[INFO] Started python-docker Application ,Access app at http://localhost:8000"

# Connect containers to common (redis) network
docker network connect redis python-docker
docker network connect redis redis
echo "[INFO] Both redis and python app joined to network -- redis"
