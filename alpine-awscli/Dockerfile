FROM python:3.7-alpine

MAINTAINER mr.anhtu9889@gmail.com

RUN \
  apk add --virtual --update --no-cache less groff jq \
  && pip install --no-cache-dir -U pip awscli \
  && rm -rf /var/cache/apk/*
