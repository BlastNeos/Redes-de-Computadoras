import socket
import time
from datetime import datetime

SERVER_IP = '192.168.0.85'  
PORT = 12345
INTERVALO = 1  
GRUPO = "PingSlayers"
MAX_MENSAJES = 100
LOG_FILE = "cliente_udp_log.txt"

def log_mensaje(mensaje):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] Enviado: {mensaje}\n")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    for i in range(1, MAX_MENSAJES + 1):
        mensaje = f"{GRUPO}-{i:04}"
        s.sendto(mensaje.encode(), (SERVER_IP, PORT))
        print(f"[Cliente UDP] Enviado: {mensaje}")
        log_mensaje(mensaje)
        time.sleep(INTERVALO)
