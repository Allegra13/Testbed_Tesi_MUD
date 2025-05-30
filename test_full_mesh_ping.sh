#!/bin/bash

containers=("devA" "devB" "devC" "gateway1" "gateway2" "firewall" "osmud")

# Mappa IP per ciascun container
declare -A ips
ips[devA]="10.0.0.4"
ips[devB]="172.18.0.3"
ips[devC]="172.19.0.2"
ips[gateway1]="10.0.0.2"
ips[gateway2]="172.18.0.2"
ips[firewall]="10.0.0.1"
ips[osmud]="192.168.1.1"

echo "=============================="
echo " TEST DI PING COMPLETO (FULL MESH)"
echo "=============================="

for src in "${containers[@]}"; do
    echo -e "\n--- Da $src ---"
    for dst in "${containers[@]}"; do
        if [ "$src" != "$dst" ]; then
            ip=${ips[$dst]}
            echo -n "Ping verso $dst ($ip): "
            docker exec "$src" ping -c 1 -W 1 "$ip" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                echo "OK"
            else
                echo "FALLITO"
            fi
        fi
    done
done

echo -e "\n=============================="
echo "     TEST COMPLETATO"
echo "=============================="
