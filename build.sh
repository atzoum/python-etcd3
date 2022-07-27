#!/bin/bash

docker build --platform linux/arm64 -t etcd3-rs-builder . -f Dockerfile.builder && \
docker run -ti --platform linux/arm64 --rm -v $(pwd):/etcd3 etcd3-rs-builder sh -c 'pip3 wheel . -w dist' && \
docker build --platform linux/amd64 -t etcd3-rs-builder . -f Dockerfile.builder && \
docker run -ti --platform linux/amd64 --rm -v $(pwd):/etcd3 etcd3-rs-builder sh -c 'python3 setup.py sdist && pip3 wheel . -w dist' && \
docker build --platform linux/amd64 -t etc-publisher . -f Dockerfile.publisher && \
docker run -ti --platform linux/amd64 --rm -v $(pwd):/etcd3 etc-publisher sh -c 'twine upload dist/*' && \
echo "Done!"

