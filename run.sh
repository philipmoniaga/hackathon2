#!/bin/bash
eval $(docker-machine env default)
docker build -t intercom .
docker run -v `pwd`/src:/opt/intercom/src  -h `whoami` -t -d intercom