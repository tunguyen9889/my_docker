# Reference link: https://getcarina.com/docs/tutorials/schedule-tasks-cron/
FROM alpine:latest
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>

RUN \
  apk add --update --virtual --no-cache curl tzdata \
  && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
  && apk del tzdata \
  && rm -rf /var/cache/apk/*

ADD crontime /tmp/crontime
COPY tasks/ /etc/periodic/
RUN cat /tmp/crontime | crontab - \
  && rm -f /tmp/crontime \
  && chmod -R +x /etc/periodic/

CMD ["crond", "-f", "-d", "8"]
