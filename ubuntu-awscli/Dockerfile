FROM ubuntu:18.04

MAINTAINER mr.anhtu9889@gmail.com

RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  curl \
  dnsutils \
  netcat \
  jq \
  python3-pip \
  python3-setuptools \
  && pip3 install --no-cache-dir -U awscli \
  && apt-get clean autoclean \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && echo complete -C '/usr/local/bin/aws_completer' aws >> ~/.bashrc
