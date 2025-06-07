import socket
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


SERVER_IP = '192.168.0.85' 
SERVER_PORT = 12345
CLAVE = b'1234567890abcdef'  # Clave de 16 bytes (AES-128)
NUM_MENSAJES = 10
INTERVALO_SEG = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1, NUM_MENSAJES + 1):
    mensaje = f"PingSlayers-{i}".encode()
    
    iv = get_random_bytes(16)
    cipher = AES.new(CLAVE, AES.MODE_CBC, iv)
    mensaje_cifrado = iv + cipher.encrypt(pad(mensaje, AES.block_size))
    
    sock.sendto(mensaje_cifrado, (SERVER_IP, SERVER_PORT))
    print(f"Enviado: PingSlayers-{i}")
    
    time.sleep(INTERVALO_SEG)

sock.close()
