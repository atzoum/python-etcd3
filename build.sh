#!/bin/bash

docker build --platform linux/amd64 -t etc-builder . -f Dockerfile.builder
docker run -ti --platform linux/amd64 --rm -v $(pwd):/etcd3 etc-builder sh -c 'python3 setup.py sdist && twine upload dist/*'
