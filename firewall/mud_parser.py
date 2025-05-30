import time
import json
import urllib.request
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from jsonschema import validate, ValidationError

MUD_FILE_LOG = "/etc/firewall/dhcpmasq.txt"
CURRENT_URI = ""
POLICY_DB = {}

def read_mud_uri():
    try:
        with open(MUD_FILE_LOG, "r") as f:
            for line in f:
                if "MUD-URL" in line:
                    uri = line.strip().split()[-1]
                    if not (uri.startswith("http://") or uri.startswith("https://")):
                        return None
                    return uri
    except FileNotFoundError:
        print("[ERRORE] Log DHCP non trovato.")
    return None

def download_mud_file(uri):
    try:
        with urllib.request.urlopen(uri) as response:
            mud_data = json.load(response)
            return mud_data
    except Exception as e:
        print(f"[ERRORE] Scaricamento/parsing fallito: {e}")
        return None

def parse_and_apply_policy(mud_json):
    rules = []

    acls = mud_json.get("ietf-access-control-list:acls", {}).get("acl", [])

    for acl in acls:
        aces = acl.get("aces", {}).get("ace", [])
        for ace in aces:
            matches = ace.get("matches", {})
            actions = ace.get("actions", {})

            proto = "tcp" if "tcp" in matches else "udp" if "udp" in matches else None
            dst_port = matches.get(proto, {}).get("destination-port", None)
            action = actions.get("forwarding", "accept")

            if proto and dst_port:
                target = "ACCEPT" if action.lower() == "accept" else "DROP"
                rule = f"iptables -A FORWARD -p {proto} --dport {dst_port} -j {target}"
                print(f"[*] {rule}")
                subprocess.run(rule.split(), check=True)
                rules.append({
                    "protocol": proto,
                    "port": dst_port,
                    "action": action.upper()
                })

    POLICY_DB.clear()
    for r in rules:
        key = f"{r['protocol']}:{r['port']}"
        POLICY_DB[key] = r["action"]


def run_rest_api():
    class PolicyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith("/check"):
                query = self.path.split("?")[-1]
                params = dict(qc.split("=") for qc in query.split("&"))
                proto = params.get("protocol")
                port = params.get("port")

                key = f"{proto}:{port}"
                action = POLICY_DB.get(key, "DROP")

                self.send_response(200)
                self.end_headers()
                self.wfile.write(action.encode())

    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, PolicyHandler)
    httpd.serve_forever()


def validate_mud_schema(mud_data):
    with open("/etc/firewall/mud_schema.json") as f:
        schema = json.load(f)
    try:
        validate(instance=mud_data, schema=schema)
        return True
    except ValidationError as e:
        print(f"[ERRORE] MUD JSON non valido: {e}")
        return False


def main():
    global CURRENT_URI
    import threading
    threading.Thread(target=run_rest_api, daemon=True).start()

    while True:
        new_uri = read_mud_uri()
        if new_uri and new_uri != CURRENT_URI:
            CURRENT_URI = new_uri
            mud_data = download_mud_file(CURRENT_URI)
            if mud_data and validate_mud_schema(mud_data):
                parse_and_apply_policy(mud_data)
        time.sleep(5)

if __name__ == "__main__":
    main()
