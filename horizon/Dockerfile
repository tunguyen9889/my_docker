FROM rethinkdb/horizon:v2.0.0

RUN \
  apt-get update \
  && apt-get install --no-install-recommends -y python-setuptools python-dev build-essential php5-mcrypt python-pip \
  && pip install rethinkdb

ENV PORT 8181

COPY root /

WORKDIR /usr/app

CMD ["/bin/sh", "/opt/horizon/bin/start.sh"]
