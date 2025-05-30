#!/bin/sh

ip route del default
ip route add default via 10.0.0.1 dev eth0
ip route add 172.18.0.0/24 via 10.0.0.1
ip route add 172.19.0.0/24 via 10.0.0.1
ip route add 192.168.1.0/24 via 10.0.0.1

echo "192.168.1.1 osmud" >> /etc/hosts
echo "nameserver 8.8.8.8" > /etc/resolv.conf

sleep infinity
