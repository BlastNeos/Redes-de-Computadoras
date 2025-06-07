from datetime import datetime

def leer_tiempos(filename, etiqueta):
    tiempos = []
    with open(filename, 'r') as f:
        for linea in f:
            if etiqueta in linea:
                ts_str = linea.split(']')[0][1:]
                tiempos.append(datetime.fromisoformat(ts_str))
    return tiempos

# Leer tiempos de envío y recepción
envios = leer_tiempos('cliente_log.txt', 'Enviado')
recepciones = leer_tiempos('server_log.txt', 'Recibido')

latencias_ms = [
    (recv -send).total_seconds() * 1000
    for send, recv in zip(envios, recepciones)
]

# Calcular estadísticas
latencia_promedio = sum(latencias_ms) / len(latencias_ms)
latencia_min = min(latencias_ms)
latencia_max = max(latencias_ms)

jitters = [
    abs(latencias_ms[i] - latencias_ms[i-1])
    for i in range(1, len(latencias_ms))
]
jitter_promedio = sum(jitters) / len(jitters)

print(f"Resultados para 100 paquetes:")
print(f"Latencia promedio: {latencia_promedio:.2f} ms")
print(f"Latencia mínima:  {latencia_min:.2f} ms")
print(f"Latencia máxima:  {latencia_max:.2f} ms")
print(f"Jitter promedio:  {jitter_promedio:.2f} ms")
