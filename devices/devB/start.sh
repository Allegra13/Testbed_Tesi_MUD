#!/bin/sh

ip route del default
ip route add default via 172.18.0.1 dev eth0
ip route add 10.0.0.0/24 via 172.18.0.1
ip route add 192.168.1.0/24 via 172.18.0.1
ip route add 172.19.0.0/24 via 172.18.0.1

sleep infinity