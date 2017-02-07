FROM golang:1.7-alpine
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>

RUN \
  apk add --virtual --no-cache tzdata curl postgresql-client git alpine-sdk \
  && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
  && apk del tzdata \
  && rm -rf /var/cache/apk/*
RUN \
  go get github.com/tools/godep \
  && go get github.com/beego/bee \
  && go get -u github.com/Masterminds/glide/...
