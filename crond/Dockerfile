FROM ubuntu:16.04
MAINTAINER Tu A. Nguyen <mr.anhtu9889@gmail.com>
ADD packtpub-ebook-claim.sh /usr/bin/packtpub-ebook-claim.sh
ENV TERM=xterm-256color
RUN \
  chmod +x /usr/bin/packtpub-ebook-claim.sh \
  && apt-get clean && apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y --force-yes cron curl \
  && apt-get clean autoclean \
  && apt-get autoremove -y \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
  && env |sed 's/^\(.*\)$/export \1/g' > /root/.profile \
  && rm -f /etc/localtime \
  && ln -s /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
ADD mycron /etc/cron.d/mycron
CMD ["cron", "-f"]
