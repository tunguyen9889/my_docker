FROM alpine:3.4
MAINTAINER mr.anhtu9889@gmail.com

ENV APP_HOME /usr/src/app
ENV FLASK_APP $APP_HOME/server.py
EXPOSE 5000

RUN \
  apk add --update --no-cache wget tar openjdk7-jre py-setuptools alpine-sdk python-dev py-pip libtool \
  && update-ca-certificates \
  && pip install --upgrade pip \
  && rm -rf /var/cache/apk/*

RUN \
  mkdir -p $APP_HOME/or-tools \
  && wget -qO- https://github.com/google/or-tools/releases/download/v5.0/or-tools_python_examples_v5.0.3919.tar.gz \
  | tar xz -C $APP_HOME/or-tools --strip-components 1 \
  && cd $APP_HOME/or-tools \
  && python2 setup.py install --user

ADD server.py $APP_HOME/
ADD requirements.txt $APP_HOME/

RUN \
  pip install -r $APP_HOME/requirements.txt

WORKDIR $APP_HOME

CMD ["flask", "run", "--host=0.0.0.0"]

