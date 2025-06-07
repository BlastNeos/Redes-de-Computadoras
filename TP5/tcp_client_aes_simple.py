import socket
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

HOST = '192.168.0.85'
PORT = 12345
INTERVALO = 1 
MAX_MENSAJES = 10
CLAVE = b'1234567890abcdef'

# Crear socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

for i in range(1, MAX_MENSAJES + 1):
    mensaje = f"PingSlayers-{i}".encode()

    iv = get_random_bytes(16)
    cipher = AES.new(CLAVE, AES.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje, AES.block_size))

    # Enviar IV + mensaje cifrado
    sock.sendall(iv + mensaje_cifrado)
    print(f"Enviado: PingSlayers-{i}")
    time.sleep(INTERVALO)

sock.close()