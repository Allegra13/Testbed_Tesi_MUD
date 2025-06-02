# gateways/gateway1/Dockerfile
FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y \
    dnsmasq \
    tcpdump \
    iproute2 \
    iputils-ping \
    iptables \
    curl \
    procps \
    python3-pip \
    && apt-get clean

RUN pip3 install requests
RUN pip3 install flask requests
COPY rest_api.py /etc/gateway1/
COPY start.sh /start.sh
COPY check_policy.py /etc/gateway1/check_policy.py
RUN chmod +x /setup.sh

CMD ["/start.sh"]