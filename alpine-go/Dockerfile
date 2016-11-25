FROM golang:1.7-alpine
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>

RUN \
  apk add --no-cache tzdata curl postgresql-client git \
  && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
  && apk del tzdata
RUN go get github.com/tools/godep
RUN go get github.com/beego/bee
