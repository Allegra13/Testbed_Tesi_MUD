FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    procps \
    tcpdump \
    iptables \
    curl \
    iputils-ping \
    dnsutils \
    python3 \
    python3-pip \
    vim \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install jsonschema

COPY ./start.sh /start.sh
COPY ./mud_schema.json /etc/firewall/mud_schema.json
COPY ./mud_parser.py /etc/firewall/mud_parser.py
COPY ./dhcpmasq.txt /etc/firewall/dhcpmasq.txt

RUN chmod +x /start.sh

CMD ["/start.sh"]
