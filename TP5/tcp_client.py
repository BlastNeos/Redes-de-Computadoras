import socket
import time

HOST = '192.168.0.85'  
PORT = 12345
INTERVALO = 2  
GRUPO = "PingSlayers"
MAX_MENSAJES = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(1, MAX_MENSAJES + 1):
        mensaje = f"{GRUPO}-{i:04}"
        s.sendall(mensaje.encode())
        print(f"[Cliente] Enviado: {mensaje}")
        time.sleep(INTERVALO)
