import requests
import sys

def check_policy(protocol, port):
    try:
        url = f"http://gateway1:8080/check?protocol={protocol}&port={port}"
        response = requests.get(url)
        print(f"[INFO] Risposta gateway1: {response.text}")
    except Exception as e:
        print(f"[ERRORE] Connessione a gateway1 fallita: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 check_policy.py <protocol> <port>")
    else:
        check_policy(sys.argv[1], sys.argv[2])
