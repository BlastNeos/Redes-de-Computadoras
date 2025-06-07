import socket
from datetime import datetime

HOST = '0.0.0.0'  # Escucha en todas las interfaces
PORT = 12345      # Puerto TCP a utilizar
LOG_FILE = "server_log.txt"

def log_message(mensaje):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] Recibido: {mensaje}\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Servidor] Esperando conexión en {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[Servidor] Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            mensaje = data.decode()
            print(f"[Servidor] Mensaje recibido: {mensaje}")
            log_message(mensaje)
