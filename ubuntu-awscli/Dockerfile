FROM ubuntu:latest

MAINTAINER mr.anhtu9889@gmail.com

RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  curl \
  dnsutils \
  netcat \
  jq \
  ca-certificates \
  unzip \
  && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
  && unzip awscliv2.zip \
  && ./aws/install \
  && apt-get clean autoclean \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* awscliv2.zip /aws \
  && echo complete -C '/usr/local/bin/aws_completer' aws >> ~/.bashrc
