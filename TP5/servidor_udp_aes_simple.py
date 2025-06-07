# servidor_udp_aes_simple.py
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Configuración
IP = '0.0.0.0'
PORT = 12345
CLAVE = b'1234567890abcdef'  # Clave de 16 bytes (AES-128)
BUFFER_SIZE = 1024

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print("Servidor UDP escuchando...")

contador = 0
while contador < 10:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    iv = data[:16]
    contenido = data[16:]

    cipher = AES.new(CLAVE, AES.MODE_CBC, iv)
    try:
        mensaje = unpad(cipher.decrypt(contenido), AES.block_size).decode()
    except:
        mensaje = "[Error al descifrar]"

    print(f"Recibido de {addr}: {mensaje}")
    contador += 1

sock.close()
