from flask import Flask, request
import requests

app = Flask(__name__)

FIREWALL_API = "http://firewall:8080"

@app.route('/check', methods=['GET'])
def check():
    protocol = request.args.get('protocol')
    port = request.args.get('port')
    try:
        r = requests.get(f"{FIREWALL_API}/check", params={"protocol": protocol, "port": port})
        return r.text, r.status_code
    except Exception as e:
        return f"[ERRORE] Non riesco a contattare il firewall: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
