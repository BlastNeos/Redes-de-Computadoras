import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Configuración
IP = '0.0.0.0'
PORT = 12345
CLAVE = b'1234567890abcdef'  # Clave de 16 bytes
BUFFER_SIZE = 1024
MENSAJES_ESPERADOS = 10

# Crear socket TCP
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((IP, PORT))
server_sock.listen(1)

print("Servidor TCP escuchando...")
conn, addr = server_sock.accept()
print(f"Conexión desde {addr}")

contador = 0
while contador < MENSAJES_ESPERADOS:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break

    iv = data[:16]
    contenido = data[16:]

    cipher = AES.new(CLAVE, AES.MODE_CBC, iv)
    try:
        mensaje = unpad(cipher.decrypt(contenido), AES.block_size).decode()
    except:
        mensaje = "[Error al descifrar]"

    print(f"Recibido: {mensaje}")
    contador += 1

conn.close()
server_sock.close()
