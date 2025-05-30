#!/bin/sh
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.conf.eth0.send_redirects=0
sysctl -w net.ipv4.conf.all.send_redirects=0

ip route add 172.18.0.0/24 via 192.168.1.10 dev eth1
ip route add 172.19.0.0/24 via 192.168.1.11 dev eth1
ip route add 172.18.0.2 dev eth1
ip route add 192.168.1.0/24 dev eth1
ip route add 192.168.1.1 dev eth1

python3 /etc/firewall/mud_parser.py &

sleep infinity