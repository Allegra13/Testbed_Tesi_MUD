#!/bin/sh
ip route del default
ip route add default via 192.168.1.3 dev eth0

apache2ctl -D FOREGROUND &

sleep infinity