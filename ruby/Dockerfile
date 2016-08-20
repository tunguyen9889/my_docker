# My first Dockerfile building Ruby on Rails with RVM and PostgreSQL
FROM ubuntu:16.04
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>
ENV RUBY ruby
ENV RUBY_VERSION 2.3.0
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN \
  apt-get clean && apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y --force-yes \
  apt-utils \
  curl \
  git \
  make \
  gcc \
  nodejs \
  pkg-config \
  ca-certificates
RUN command curl -sSL https://rvm.io/mpapis.asc | gpg --import - \
  && \curl -L https://get.rvm.io | bash -s stable \
  && usermod -aG rvm root \
  && apt-get clean autoclean \
  && apt-get autoremove -y \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV INSTALL_CMD bundle exec rake install
ENV START_CMD bundle exec rake start
RUN \
  echo "source /usr/local/rvm/scripts/rvm" >> /etc/profile \
  && echo "rvm --default use $RUBY-$RUBY_VERSION" >> /etc/profile \
  && echo "gem: --no-document" >> ~/.gemrc
CMD source /usr/local/rvm/scripts/rvm
RUN \
  rvm install ${RUBY}-${RUBY_VERSION} \
  && rvm --default use ${RUBY}-${RUBY_VERSION} \
  && rvm ${RUBY}-${RUBY_VERSION} do gem install --no-rdoc --no-ri \
  bundler \
  rails \
  nokogiri
EXPOSE 3000
