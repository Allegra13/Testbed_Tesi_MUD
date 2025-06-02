#!/bin/sh
sysctl -w net.ipv4.ip_forward=1

for iface in eth0 eth1 eth2; do
  ip link set dev "$iface" up
done

ip route del default 2>/dev/null
ip route add default via 192.168.1.3 dev eth2
ip route replace 10.0.0.0/24 via 10.0.0.1 dev eth0
ip route replace 172.18.0.0/24 via 172.18.0.2 dev eth1
ip route replace 192.168.1.0/24 dev eth2
ip route replace 172.19.0.0/24 via 172.18.0.2 dev eth1

sleep infinity
