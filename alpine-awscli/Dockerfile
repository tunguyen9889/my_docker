FROM alpine:latest
MAINTAINER mr.anhtu9889@gmail.com

RUN \
  apk add --virtual --update --no-cache python py-pip jq \
  && pip install --no-cache-dir awscli \
  && rm -rf /var/cache/apk/*

