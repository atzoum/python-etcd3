FROM openresty/openresty:1.19.9.1-10-alpine-fat
RUN apk update && apk add python3 py3-pip git python3-dev
RUN pip3 install --upgrade wheel pip setuptools
WORKDIR /etcd3
