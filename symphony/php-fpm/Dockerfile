FROM php:7-fpm-alpine
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>

# Install symphony
RUN \
  apk add --no-cache curl tzdata \
  && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
  && apk del tzdata \
  && curl -k -LsS https://symfony.com/installer -o /usr/local/bin/symfony \
  && chmod a+x /usr/local/bin/symfony \
  && symfony self-update \
  && symfony demo

EXPOSE 8000 9000

WORKDIR /var/www/html/symfony_demo

# Run symphony demo
CMD ["php", "bin/console", "server:run"]
