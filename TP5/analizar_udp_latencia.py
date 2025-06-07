from datetime import datetime
import re

# Archivos de log
LOG_CLIENTE = "cliente_udp_log.txt"
LOG_SERVIDOR = "servidor_udp_log.txt"

# Función para leer los logs y devolver un diccionario {mensaje_id: timestamp}
def leer_log(filename, etiqueta):
    tiempos = {}
    patron = re.compile(r"\[(.*?)\] " + re.escape(etiqueta) + r": (PingSlayers-\d+)")
    with open(filename, 'r') as f:
        for linea in f:
            match = patron.search(linea)
            if match:
                timestamp = datetime.fromisoformat(match.group(1))
                mensaje_id = match.group(2)
                tiempos[mensaje_id] = timestamp
    return tiempos

# Leer logs de envío y recepción
envios = leer_log(LOG_CLIENTE, "Enviado")
recepciones = leer_log(LOG_SERVIDOR, "Recibido")

# Cruce de mensajes por ID
mensajes_comunes = sorted(set(envios.keys()) & set(recepciones.keys()))

if not mensajes_comunes:
    print("No se encontraron mensajes coincidentes entre cliente y servidor.")
    exit(1)

# Calcular latencias
latencias = [
    (recepciones[msg] - envios[msg]).total_seconds() * 1000
    for msg in mensajes_comunes
]

# Cálculo de estadísticas
lat_prom = sum(latencias) / len(latencias)
lat_min = min(latencias)
lat_max = max(latencias)

jitters = [
    abs(latencias[i] - latencias[i - 1])
    for i in range(1, len(latencias))
]
jitter_prom = sum(jitters) / len(jitters) if jitters else 0

# Imprimir resultados
print(f"Análisis de {len(mensajes_comunes)} paquetes UDP")
print(f"Latencia promedio : {lat_prom:.2f} ms")
print(f"Latencia mínima   : {lat_min:.2f} ms")
print(f"Latencia máxima   : {lat_max:.2f} ms")
print(f"Jitter promedio   : {jitter_prom:.2f} ms")
