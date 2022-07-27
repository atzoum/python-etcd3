FROM alpine:latest
RUN apk update && apk add python3 py3-pip git python3-dev g++
RUN pip3 install --upgrade pip setuptools build twine wheel
WORKDIR /etcd3
