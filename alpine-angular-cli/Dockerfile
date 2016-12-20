FROM node:6.9.2-alpine
MAINTAINER anhtu@siliconstraits.com

RUN \
  apk add --update  --no-cache make gcc g++ python bash \
  && npm install -g angular-cli \
  && rm -rf /var/cache/apk/*

