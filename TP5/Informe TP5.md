# Informe del trabajo práctico 5

### **Federico I Soria**
### **Fernando Zarate**  
### **"Ping Slayers"**

## Introducción

Se buscó con este trabajo práctico demostrar la capacidad de manipular librerías de networking en Python
y analizar el comportamiento de la capa de transporte al transmitir tanto paquetes TCP como UDP entre
dos nodos. 
Para ello, se desarrollaron scripts que enviaron paquetes identificatorios con intervalos de un
segundo y posteriormente, se capturó el tráfico con la herramienta de Wireshark para obtener 
métricas de latencia y jitter.

## Desarrollo de protocolo tcp - tcp_client.py

Se desarrollaron scripts para enviar paquetes TCP desde una computadora y recibirlos en otra computadora en la cual estamos capturando tráfico con Wireshark. 
Cada uno de estos paquetes tiene un identificador que consiste en el nombre del grupo (PingSlayers) más un número que se incrementa.
En la computadora que funciona como SENDER se llama al script tcp_client.py:

![imagen](https://github.com/user-attachments/assets/4a6647d4-3146-4b4d-83af-a200f03b13f3)

Mediante el comando ifconfig podemos conocer la direccion IP de cada computadora, en este caso la direccion IP de la computadora que ejecuta el script cliente es “192.168.0.181” 
y el de la computadora que ejecuta el server es “192.168.0.85” como podemos ver en el código.

![imagen](https://github.com/user-attachments/assets/1d12c480-522b-4d8c-9f9c-00e1c5a3223b)

A continuación se muestran los llamados a las versiones prototipo de server.py y client.py

<img src="https://github.com/user-attachments/assets/1fca40b1-ebd8-49e6-aa24-8765850154b8" weight="350"/>

<img src="https://github.com/user-attachments/assets/ab1981a9-ee72-4f6f-8f8f-f031016b1c08" width="700"/>

Para el análisis del payload se utilizó como herramienta a Wireshark, filtrando el puerto 12345 para ver 
los datos de nuestro interés:

![imagen](https://github.com/user-attachments/assets/bb8883bc-771b-41ad-9498-d060a8589775)

Viendo ese paquete en particular podemos ver que la fuente es la dirección IP del cliente (192.168.0.181), el protocolo es TCP y el contenido del mensaje es “PingSlayers–0008”

## Logging y cálculo de métricas

Se implementó una funcionalidad que permite guardar en un archivo (log) todos los paquetes enviados y recibidos, incluyendo una marca de tiempo (timestamp) del momento en que fueron enviados/recibidos.

<img src="https://github.com/user-attachments/assets/79a3ab00-0fc4-477b-998f-5f85460c74c7" width="500"/>

<img src="https://github.com/user-attachments/assets/51908fb4-3dfb-4363-a5d9-6a0b694090f4" width="500"/>


En base a esos logs se realizará el análisis de la latencia, lo cual se realiza mediante el script "analizar_latencia.py":

![imagen](https://github.com/user-attachments/assets/c1ce4c4d-81b8-4d82-8c01-605f095d04b2)

Que al ejecutarse nos otorga los siguientes resultados:

![imagen](https://github.com/user-attachments/assets/245d1433-647d-4d11-b9ab-efdfa5ee4fba)

## Desarrollo de protocolo udp - udp_client.py

Se adoptó una metodología análoga a la utilizada en TCP, pero adaptando el modelo de sockets al enfoque
sin conexión característico de UDP. Para ello se desarrollaron scripts de servidor y cliente que 
enviaron 100 datagramas consecutivos, cada uno con un identificador único, a intervalos de un segundo.
Durante el proceso se registraron en archivos de log todos los eventos de envío (“SENT”) y recepción 
(“RECV” o “TIMEOUT”), lo cual permitió posteriormente calcular las métricas de latencia y jitter y 
comparar el comportamiento de ambos protocolos.

Analizamos los paquetes usando wireshark usando el filtro udp.port==12345
Viendo ese paquete en particular podemos ver que la fuente es la dirección IP del cliente (192.168.0.181), el protocolo es UDP. Ahora veamos el contenido.

![imagen](https://github.com/user-attachments/assets/b16a7e0c-0e5f-4d24-b39a-fc7be413c6dd)

Se puede inspeccionar que el contenido del paquete es “PingSlayers–0012”

![imagen](https://github.com/user-attachments/assets/959fbf80-9c00-4a40-b8b6-468d7d86c82d)

Para analizar la latencia promedio y el jitter desarrollamos el script adjunto dentro del repositorio llamado "analizar_udp_latencia.py" cuya ejecución muestra el siguiente resultado:

![imagen](https://github.com/user-attachments/assets/b41b2a0e-29bc-438d-9073-bc32df494243)

## Comparación de protocolos
![imagen](https://github.com/user-attachments/assets/eaa7bf1f-4a52-461e-8bb2-d2c05cf0940d)

![imagen](https://github.com/user-attachments/assets/3e2fe043-2afd-467a-abb3-f1601501f44e)

A partir de estos datos se obtienen las siguientes conclusiones: 
Aunque UDP suele ser más rápido por no requerir establecimiento de conexión ni acuses de recibo, en esta prueba el comportamiento de la red fue muy similar para ambos protocolos, con diferencias mínimas. 
Esto sugiere que la red bajo prueba es estable, tiene poco ruido o congestión, y que la medición fue probablemente limitada más por el sistema operativo o la lógica de aplicación que por el protocolo en sí.
TCP es más fiable, y en esta prueba incluso logró una latencia promedio inferior.
UDP puede ser más veloz en redes inestables o cuando se optimiza a bajo nivel, pero no garantiza orden ni entrega.

## Encriptación
### Encriptación simétrica
La encriptación simétrica se basa en el uso de una única clave para cifrar y descifrar los datos, de modo que tanto el emisor como el receptor deben conocer y compartir esta clave de forma previa a la comunicación.
Entre los algoritmos más utilizados en este tipo de encriptación se encuentran AES, DES y ChaCha20.
Una de sus principales ventajas es la velocidad: es considerablemente más rápida que la encriptación asimétrica, lo que la hace ideal para cifrar grandes volúmenes de información. 
Sin embargo, presenta una desventaja importante: si la clave es interceptada, toda la comunicación queda comprometida.
Como ventaja, es rápida y eficiente para manejar grandes cantidades de datos pero esto requiere un canal seguro para compartir la clave de antemano.

## Encriptación asimétrica
En este caso, se utilizan dos claves distintas pero relacionadas: una clave pública y una clave privada. 
La clave pública puede ser compartida libremente, y sirve para cifrar los datos, mientras que la clave privada (que debe mantenerse en secreto) es la única que puede descifrarlos.
Este tipo de encriptación es más segura para establecer comunicaciones sin necesidad de que las partes se hayan conocido previamente, aunque tiene como contrapartida una mayor carga computacional, lo que la hace más lenta que la simétrica.

Implementación práctica
La librería que elegimos es pycryptodome. Esta es compatible con múltiples algoritmos de cifrado, incluyendo AES, y permite controlar directamente aspectos como la clave, el vector de inicialización (IV), y los modos de operación.
Verificación de encriptación
Primero instalamos pycryptodome.
Desarrollamos nuevos scripts para el server y el cliente y los ejecutamos en las computadoras, capturamos el trafico usando wireshark.
Para TCP:
Por las dependencias con Ubuntu, ejecutamos en un ambiente virtual

![imagen](https://github.com/user-attachments/assets/64b46526-af22-4816-8ba0-e3a731448ee9)

Se analiza el contenido de los paquetes en wireshark
![imagen](https://github.com/user-attachments/assets/a329f406-e43f-43ed-a41e-a3b66eff6e5a)

De esta forma podemos ver que los paquetes se encuentran cifrados
Si comparamos las tramas podemos ver que son distintas con respecto a la forma sin encriptamiento.

De manera similar trabajamos con servidor_udp_aes_simple.py y cliente_udp_aes_simple.py

![imagen](https://github.com/user-attachments/assets/d1a310fa-bdf6-4320-8197-11645fb9a81a)

Al igual que antes, verificamos los datos mediante wireshark y se observa que la carga del paquete está cifrada.

![imagen](https://github.com/user-attachments/assets/fc43ce39-ea28-4402-9409-6e6404a71353)

Analizando el contenido del paquete podemos ver que se encuentra cifrado.

### Comunicación segura a larga distancia
**¿Cómo encriptar sin haber intercambiado claves previamente?**

La forma adecuada es usar encriptación asimétrica, como RSA. Este tipo de cifrado funciona con dos claves: una pública, que puede compartirse libremente, y una privada, que se mantiene en secreto.

**¿Cómo se implementaría esto en los scripts?**

El servidor genera un par de claves: una pública y una privada, una vez que el cliente se conecta por primera vez, el servidor le envía su clave pública.

El cliente usa esa clave pública para cifrar los mensajes que envía y el servidor, al recibirlos, los descifra usando su clave privada.

De este modo, aunque alguien intercepte los datos, no podrá leer el contenido sin la clave privada.
Además, si se quiere que la comunicación sea segura en ambos sentidos, también se puede hacer que el cliente tenga su propio par de claves y el servidor cifre sus respuestas con la clave pública del cliente.

## Conclusión
A lo largo de este trabajo práctico, se logró desarrollar e implementar exitosamente scripts de comunicación utilizando los protocolos TCP y UDP, incorporando funcionalidades clave como logging, medición de latencia y jitter, y análisis de tráfico mediante Wireshark. A partir de estas implementaciones, se pudo observar y comparar el comportamiento de ambos protocolos en un entorno controlado.
Los resultados mostraron que, si bien TCP y UDP tienen diferencias estructurales significativas —como la fiabilidad y el control de flujo en TCP frente a la ligereza de UDP—, el rendimiento observado fue similar en términos de latencia promedio y jitter. Esto sugiere una red local estable y sin congestión, donde las ventajas teóricas de UDP en velocidad no se manifestaron de forma clara.
Además, se incorporó encriptación simétrica (AES) a las comunicaciones, demostrando que es posible proteger los datos transmitidos incluso en protocolos que no garantizan seguridad nativa. Se discutió también la utilidad de la encriptación asimétrica para escenarios donde las claves no pueden compartirse previamente, planteando una solución viable para comunicaciones seguras a larga distancia.
Este trabajo permitió integrar conceptos clave de redes de computadoras, análisis de tráfico, y seguridad de la información, brindando una base sólida para el desarrollo de aplicaciones seguras y eficientes en entornos reales.


