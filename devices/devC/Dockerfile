# devices/devC/Dockerfile
FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
  isc-dhcp-client \
  iproute2 \
  procps \
  iputils-ping \
  dnsutils \
  curl \
  iptables && \
  apt-get clean

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
