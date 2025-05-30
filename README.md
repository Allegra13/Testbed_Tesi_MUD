# Testbed_Tesi_MUD

**Testbed_Tesi_MUD** è un testbed in Docker che simula l'applicazione dello standard MUD (Manufacturer Usage Description, RFC 8520) in una rete IoT. Il progetto include container per dispositivi IoT simulati, firewall, gateway e osMUD server.

## Componenti principali

- **firewall**: applica dinamicamente le policy MUD (iptables)
- **gateway1/gateway2**: inoltrano richieste e traffico
- **osmud**: server MUD che ospita i file JSON
- **devA, devB, devC**: dispositivi IoT simulati

## Avvio del testbed

Assicurati di avere Docker e Docker Compose installati.

Per avviare il testbed:

```bash
docker compose build
docker compose up -d

Per fermare e rimuovere tutto:

```bash
docker compose down