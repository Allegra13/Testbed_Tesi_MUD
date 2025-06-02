#!/bin/sh

sysctl -w net.ipv4.ip_forward=1

ip route del default
ip route add default via 192.168.1.3 dev eth2

ip route add 10.0.0.0/24 via 172.18.0.1 dev eth0
ip route add 172.18.0.0/24 via 172.18.0.1 dev eth0
ip route add 192.168.1.0/24 via 172.18.0.1 dev eth0
ip route add 172.30.0.0/24 via 172.18.0.1 dev eth0
ip route add 172.19.0.0/24 dev eth1
ip route add 10.0.0.0/24 via 192.168.1.10

sleep infinity
