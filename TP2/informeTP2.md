# TP2 - Evaluación de Performance en Redes y Topologías Multi-Path

## Resumen Ejecutivo

En este trabajo nos propusimos diseñar, implementar y evaluar una red de laboratorio basada en topologías multi-path. Para ello, configuramos una serie de PCs, switches y routers siguiendo una estructura modular. Cada grupo de computadoras se conectó a un switch, que a su vez se enlazaba con un router y así sucesivamente, formando una red escalable. 

Utilizamos tanto enrutamiento estático como dinámico, y realizamos pruebas de conectividad mediante ICMP (ping). Para evaluar el rendimiento de la red, empleamos herramientas como **iperf3** y **Wireshark**, comparando el comportamiento de los protocolos **TCP y UDP** en diferentes escenarios. Nuestro enfoque principal fue analizar el ancho de banda, los tiempos de respuesta y la pérdida de paquetes.

## Introducción

El desarrollo de esta red experimental se realizó en un entorno físico, permitiendo poner a prueba el diseño de una topología segmentada en grupos, donde cada segmento contaba con su propio switch y se comunicaba con el resto mediante routers. Este enfoque nos permitió trabajar con una red modular y fácilmente escalable. 

Durante la experiencia también exploramos las diferencias entre enrutamiento estático y dinámico, evaluando sus beneficios y desventajas en función de los resultados obtenidos durante las pruebas.

## Objetivos

El objetivo general fue evaluar el rendimiento de la red física bajo distintas condiciones. Para ello, buscamos aplicar enrutamiento estático en los hosts, incorporar enrutamiento dinámico donde fuera conveniente, y validar la interoperabilidad de los componentes en entornos mixtos (físicos y virtuales). También nos enfocamos en la escalabilidad y en la capacidad de detectar cuellos de botella o limitaciones de configuración.

## Equipos y Herramientas Utilizadas

Para el armado de la red utilizamos 2 o 3 PCs por grupo, cada una con direcciones IP estáticas. Estos dispositivos se conectaban a través de switches, y los switches a su vez a routers, que cumplían el rol de nexo entre los distintos grupos. Dependiendo de la disponibilidad, usamos cables UTP, fibra óptica u otros medios de conexión.

A nivel software, trabajamos principalmente con **iperf3**, una herramienta esencial para medir el rendimiento de red, y con **Wireshark**, que nos permitió capturar y analizar el tráfico. Las pruebas de conectividad se realizaron sobre sistemas operativos con soporte para comandos como `ping`, `ipconfig`, `ifconfig` o `ip addr`.

## Topología de Red

La red que diseñamos seguía un patrón modular. Cada grupo local tenía entre dos y tres PCs conectadas a un switch. Estas máquinas se comunicaban internamente utilizando direcciones IP fijas, permitiendo pruebas básicas de conectividad. 

Los switches se conectaban a routers que actuaban como puertas de enlace hacia otros grupos. Esta estructura se repetía de forma sistemática, permitiendo ampliar la red de manera sencilla y manteniendo la coherencia en la configuración general.

## Configuración y Pruebas de Conectividad

Una vez asignadas las direcciones IP a cada dispositivo, validamos su correcta configuración mediante comandos básicos en cada sistema operativo. 

Probamos la comunicación local dentro de cada segmento, enviando paquetes ICMP entre dispositivos del mismo grupo. Por ejemplo, se realizaron pings exitosos desde `192.168.1.20` a `192.168.1.27` y `192.168.1.11`.

![ping27](https://github.com/user-attachments/assets/bfedccd0-bd34-4d89-b5e2-9f9fed72c299)

![pin11](https://github.com/user-attachments/assets/6d6e69d9-d02d-4434-81e4-e9ee91de4f8c)

Figuras 1 y 2: ping desde 192.168.1.20 a 192.168.1.27 y a 192.168.1.11

Luego, avanzamos con pruebas entre grupos distintos, es decir, entre dispositivos ubicados detrás de routers diferentes. Esto nos permitió verificar que las rutas estuvieran bien configuradas y que la red permitiera el tráfico entre segmentos. Un ejemplo fue el envío de paquetes desde `192.168.1.27` a `34.27.143.1192`.

![ping34](https://github.com/user-attachments/assets/8a1334e7-01b0-47d0-a6e6-1656a38c87d6)

Figura 3: envio de paquetes desde 192.168.1.27 a 34.27.143.1192


## Evaluación del Rendimiento con iperf3

Para evaluar la performance de la red, descargamos e instalamos **iperf3** desde [iperf.fr](https://iperf.fr) en todos los equipos involucrados. Esta herramienta nos permitió medir tanto tráfico **TCP** como **UDP**, configurando parámetros como el ancho de banda, duración de las pruebas y tamaño de los paquetes.

Entre los comandos más usados destacamos:

- `-u` para pruebas con UDP  
- `-n` y `-l` para definir el número y tamaño de paquetes  
- `-t` para establecer la duración  
- `-b` para ajustar el ancho de banda

Los resultados nos dieron una idea clara del comportamiento de la red en distintos escenarios de carga.

## Análisis de Tráfico con Wireshark

Finalmente, realizamos capturas de tráfico entre hosts de distintos grupos, simulando una conexión cliente-servidor. Con **Wireshark** pudimos observar el flujo de paquetes, los protocolos utilizados, y medir posibles pérdidas o retrasos. Esta herramienta resultó clave para validar el comportamiento interno de la red y reforzar las conclusiones obtenidas con iperf3.

---![iperf(-s)](https://github.com/user-attachments/assets/b3e78bf8-db6e-4503-b08e-921b58d6f916)


> Trabajo Práctico N°2 - Cátedra de Redes
