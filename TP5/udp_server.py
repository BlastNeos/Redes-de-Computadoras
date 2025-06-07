import socket
from datetime import datetime

HOST = '0.0.0.0'
PORT = 12345
LOG_FILE = "servidor_udp_log.txt"

def log_mensaje(mensaje):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] Recibido: {mensaje}\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[Servidor UDP] Escuchando en {HOST}:{PORT}...")

    while True:
        data, addr = s.recvfrom(1024)
        mensaje = data.decode()
        print(f"[Servidor UDP] Recibido desde {addr}: {mensaje}")
        log_mensaje(mensaje)
