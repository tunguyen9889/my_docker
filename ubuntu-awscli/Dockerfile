FROM ubuntu:18.04

MAINTAINER mr.anhtu9889@gmail.com

RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  curl \
  dnsutils \
  jq \
  python3-minimal \
  python3-distutils \
  && curl --insecure https://bootstrap.pypa.io/get-pip.py | python3 \
  && pip install --no-cache-dir -U awscli \
  && apt-get clean autoclean \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && echo complete -C '/usr/local/bin/aws_completer' aws >> ~/.bashrc
