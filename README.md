# Testbed_Tesi_MUD

Testbed per la tesi sperimentale sull'applicazione dello standard **MUD (Manufacturer Usage Description)**, progettato per simulare un ambiente di rete IoT con controllo dinamico delle policy.

## Descrizione

Questo progetto implementa un'infrastruttura Docker completa per testare l'applicazione delle policy MUD secondo lo standard [RFC 8520](https://datatracker.ietf.org/doc/html/rfc8520), simulando un ambiente a più livelli con firewall, gateway, dispositivi IoT e un MUD controller (`osmud`).

Il parser MUD (`mud_parser.py`) analizza i file MUD JSON e applica dinamicamente regole `iptables` per consentire o bloccare il traffico in base alla descrizione del dispositivo.

---

## Architettura

- **Firewall**: applica dinamicamente le regole di rete in base al file MUD.
- **Gateway1 / Gateway2**: interrogano il firewall per verificare il permesso delle comunicazioni.
- **Dispositivi IoT (devA, devB, devC)**: dispositivi simulati che generano traffico.
- **osmud**: servizio HTTP che ospita i file MUD.
- **Script**: `check_policy.py`, `start.sh`, `setup.sh`, `mud_parser.py`

Tutti i container sono connessi in una rete simulata multilivello con Docker.

---

## Come usare

### Requisiti

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Avvio del testbed

```bash
docker compose build
docker compose up -d
```

### Verifica che tutti i container siano attivi

```bash
docker ps
```

### Esecuzione test automatico di connettività

```bash
./test_full_mesh_ping.sh
```

## Struttura progetto 

Testbed_Tesi_MUD/
│
├── docker-compose.yml
├── firewall/
│   ├── mud_parser.py
│   ├── mud_schema.json
│   ├── dhcpmasq.txt
│   ├── logs/
│   └── start.sh
│
├── gateways/
│   ├── gateway1/
│   │   ├── check_policy.py
│   │   ├── rest_api.py
│   │   └── setup.sh
│   └── gateway2/
│       ├── check_policy.py
│       └── setup.sh
│
├── devices/
│   ├── devA/
│   │   ├── Dockerfile
│   │   └── start.sh
│   ├── devB/
│   │   ├── Dockerfile
│   │   └── start.sh
│   └── devC/
│       ├── Dockerfile
│       └── start.sh
│
├── osmud/
│   ├── Dockerfile
│   ├── mud-ssl.conf
│   ├── mudfiles/
│   │   └── mud_firewall.json
│   └── start.sh
│
├── test_full_mesh_ping.sh
├── LICENSE
└── README.md

## Licenza

Questo progetto è distribuito con licenza GPLv3.
Per maggiori dettagli consulta il file LICENSE.

## Autore

Allegra Farabullini
Università degli studi di Firenze - Tesi di laurea 2025
© 2025 Allegra Farabullini. Tutti i diritti riservati.

## Note

Lo script mud_parser.py supporta il parsing del file MUD e l’applicazione delle regole iptables in tempo reale.

Il file mud_schema.json consente la validazione dello schema MUD ufficiale.

Il sistema supporta il caricamento dinamico delle policy e l’interrogazione REST da gateway.

I test di connettività sono automatizzati con lo script test_full_mesh_ping.sh.

## Contribuisci

Contributi, segnalazioni di bug e suggerimenti sono benvenuti.
Apri una issue o una pull request per partecipare allo sviluppo.


Grazie per aver scelto Testbed_Tesi_MUD!
Per domande o approfondimenti contattami.