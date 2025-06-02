# gateways/gateway2/Dockerfile
FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    dnsmasq \
    tcpdump \
    iproute2 \
    iputils-ping \
    iptables \
    curl \
    python3-pip \
    procps \
    && apt-get clean

RUN pip3 install requests
RUN pip3 install flask requests
COPY start.sh /start.sh
COPY check_policy.py /etc/gateway2/check_policy.py
RUN chmod +x /setup.sh

CMD ["/start.sh"]
