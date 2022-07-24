#!/bin/zsh
# Docker Build Image
docker build . -t python-docker --label python-docker -f Dockerfile