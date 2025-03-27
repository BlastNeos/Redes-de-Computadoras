# Configuración y Análisis de tráfico IPv4/IPv6
  
**-Federico I Soria**

**-Fernando Zarate**  

**Ping Slayers**

**Facultad de Ciencias Exactas, Fisicas y Naturales**  
**Redes de Computadoras**

**Profesores** (para publicaciones de alumnos)  --> AGREGAR

**Marzo 2024**  

---

## Resumen
Este trabajo se enfoca en el estudio de los principios fundamentales que rigen la comunicación entre dispositivos dentro de una red de computadoras. Se analizan los modelos de interconexión, con especial énfasis en las capas de enlace de datos, red y transporte, y su rol en la entrega eficiente de información. Asimismo, se examina el funcionamiento de los protocolos de comunicación, resaltando la encapsulación y desencapsulación de datos como procesos clave para garantizar la interoperabilidad entre diferentes sistemas de red.

Palabras clave: interconexión de redes, protocolos de comunicación

## Introducción

<div style="text-align: justify;">
El desarrollo de redes de conmutación y transmisión de paquetes surgió como respuesta a la necesidad de ampliar el acceso a recursos más allá de los sistemas aislados, lo que impulsó la interconexión de múltiples redes para posibilitar la comunicación entre estaciones ubicadas en distintos entornos. Este proceso, conocido como internetworking, se basa en la conexión de redes individuales a través de dispositivos intermedios, como puentes y enrutadores, que permiten que estas redes funcionen de manera integrada como si fueran una única unidad para los usuarios.

En este contexto, se diferencian las redes individuales y sus respectivas subredes, donde los sistemas finales (ES) están conectados para la comunicación y los sistemas intermedios facilitan el intercambio de datos entre redes distintas. Existen dos tipos principales de dispositivos intermedios: los puentes, que operan en la capa 2 del modelo OSI y permiten la conexión entre redes LAN similares, y los enrutadores, que trabajan en la capa 3 y son capaces de interconectar redes con características heterogéneas. Para lograr una interconexión eficiente, se deben cumplir ciertos requisitos clave, como el establecimiento de enlaces, el encaminamiento de datos, la gestión de tráfico y la capacidad de adaptarse a las diferencias entre las redes conectadas.

Desde una perspectiva arquitectónica, las redes pueden estar diseñadas para operar de forma orientada a conexión o no orientada a conexión. En el primer caso, se establecen circuitos virtuales con retransmisión y control de ruta, mientras que en el segundo, cada unidad de datos se encamina de manera independiente. Un ejemplo de este último enfoque es el Protocolo de Internet (IP), el cual permite la interconexión entre distintas redes sin necesidad de un canal de comunicación preestablecido.

El Protocolo de Internet (IP) es un elemento central dentro del conjunto de protocolos TCP/IP, siendo IPv4 la versión más utilizada en la actualidad, pese a los esfuerzos por migrar hacia IPv6. IPv4 define los servicios disponibles, el formato del protocolo y sus mecanismos de operación. Entre sus funciones principales se incluyen la transmisión y recepción de datos mediante primitivas como Send (envío) y Deliver (entrega), las cuales utilizan parámetros como direcciones de origen y destino, identificadores únicos y opciones de configuración.

El datagrama IPv4 está compuesto por varios campos esenciales, como versión, longitud de cabecera, tipo de servicio, identificador, tiempo de vida (TTL), protocolo y suma de comprobación, entre otros. Su correcta interpretación es clave para el proceso de enrutamiento y la entrega eficiente de datos a través de la red. Las direcciones IP en IPv4 tienen una longitud de 32 bits y se agrupan en tres clases principales (A, B y C), lo que permite su asignación flexible según las necesidades de la red. Para mejorar la gestión de direcciones, se introdujo el concepto de subredes, que permite dividir una red en segmentos más pequeños con direcciones de red específicas.

Otro protocolo clave en la interconexión de redes es el Protocolo de Mensajes de Control de Internet (ICMP), el cual se emplea para proporcionar información sobre errores y problemas en la comunicación. ICMP permite el envío de mensajes de error, redirección, eco y respuesta de tiempo, facilitando la identificación y resolución de fallos en la red.

El protocolo IP es no orientado a conexión, lo que significa que **los datos se envían en forma de datagramas sin necesidad de establecer un canal de comunicación previo**. Esto ofrece flexibilidad y robustez, ya que cada enrutador determina dinámicamente la mejor ruta para los paquetes, permitiendo que la red se adapte a cambios en la topología o congestión del tráfico. Sin embargo, este método no garantiza la entrega de los datos ni su orden, ya que pueden llegar en secuencias diferentes dependiendo del camino tomado. Para optimizar su funcionamiento, IP incorpora mecanismos de encaminamiento, control de errores, gestión del flujo de tráfico y limitación del tiempo de vida de los paquetes (TTL).

Dado el creciente agotamiento de direcciones IPv4, se ha desarrollado IPv6, una versión mejorada del protocolo que expande significativamente el espacio de direcciones y proporciona nuevas funcionalidades. IPv6 utiliza direcciones de 128 bits, permitiendo una asignación más eficiente y simplificando la configuración de redes mediante mecanismos de autoconfiguración. El formato de los paquetes IPv6 incluye una cabecera principal y cabeceras de extensión opcionales, que pueden contener información adicional sobre seguridad, fragmentación, encaminamiento y control de flujo. A diferencia de IPv4, en IPv6 la fragmentación solo puede ser realizada por el nodo de origen, evitando que los enrutadores intermedios modifiquen los paquetes en tránsito.
Otra innovación importante en IPv6 es el uso de distintos tipos de direcciones, que incluyen unidifusión (unicast) para la comunicación uno a uno, monodifusión (anycast) para la entrega eficiente de paquetes a un grupo de nodos y multidifusión (multicast) para el envío de datos a múltiples destinatarios simultáneamente. Además, IPv6 introduce la etiqueta de flujo, un campo que permite identificar secuencias de paquetes con requisitos de tratamiento especial.
Por último, el protocolo IPv6 optimiza el encaminamiento mediante una cabecera específica, en la que se puede especificar una lista de nodos intermedios para definir una ruta preestablecida. Este enfoque mejora el control sobre el tráfico y permite una mejor adaptación a diversas condiciones de red.
</div>

## Desarrollo
### Parte 1 - Simulación de la red

Para el modelado de la red, se utilizó Cisco Packet Tracer, una herramienta de simulación que permite diseñar, configurar y probar infraestructuras de red sin necesidad de hardware físico. Se estableció una topología que refleja un entorno realista, interconectando distintos dispositivos de red y definiendo sus parámetros operativos. A lo largo del proceso, se configuraron switches, routers y terminales, asegurando que la comunicación entre los nodos fuera funcional y coherente con los objetivos planteados.

![image](https://github.com/user-attachments/assets/121b80ca-32bd-4431-8dac-10b259ae99b6)

En este contexto, es importante diferenciar entre un simulador y un emulador. Un simulador genera una representación matemática y lógica de una red, permitiendo evaluar distintos escenarios sin requerir hardware específico. Su uso es ideal para el análisis teórico y la validación de configuraciones. En cambio, un emulador reproduce el comportamiento real de una red al utilizar dispositivos y software auténticos o virtualizados, lo que permite realizar pruebas más cercanas a un entorno de producción. Aunque los emuladores ofrecen una mayor fidelidad en la representación de la red, requieren más recursos y pueden ser más complejos de implementar.

Además, se realizaron pruebas de conectividad para verificar el correcto funcionamiento de la red, utilizando comandos como ping y arp -a para analizar la resolución de direcciones y la transmisión de paquetes entre dispositivos. Gracias a las herramientas de simulación y monitoreo de Packet Tracer, fue posible observar el flujo de datos y diagnosticar posibles errores en la configuración.

<img src="https://github.com/user-attachments/assets/ae531119-fca4-42ff-9e7e-82be9afc25e8" width="450" align="center" />

Esto confirma la estabilidad y confiabilidad de la conectividad entre los hosts y proporciona una comprensión integral del estado de la red en términos de comunicación y accesibilidad.
Se evaluó la conectividad entre todos los host enviando 3 (tres) paquetes ICMPv6, utilizando el comando ping para IPv6 de la siguiente manera para cada dispositivo:

<img src="https://github.com/user-attachments/assets/57bc52c1-9b3c-4584-a677-2fe068b38c2e" width="600" align="center" />

A continuación se inició tráfico ICMP (Internet Control Message Protocol)  entre h1 con destino a h2 con un ping desde h1 a la dirección IPv4 de h2  donde se observaron las siguientes comunicaciones:

<img src="https://github.com/user-attachments/assets/7579922b-5a4d-43a5-abbb-d893b1ffd80c" width="600" align="center" />


El protocolo ARP (Address Resolution Protocol) se utiliza para mapear direcciones IP a direcciones MAC. Cuando un dispositivo necesita conocer la dirección MAC correspondiente a una dirección IP específica (por ejemplo, para comunicarse con otro dispositivo en la red), envía una solicitud ARP en forma de difusión a todos los dispositivos de la red local. Esta solicitud incluye la dirección IP del dispositivo al que intenta acceder. En el siguiente ejemplo, se muestra cómo h1 envía una solicitud ARP a la dirección IP del router.

<img src="https://github.com/user-attachments/assets/e551be2c-2961-4a77-9123-8acc44f21fd7" width="600" align="center" />

Cuando el dispositivo que posee la dirección IP solicitada recibe la solicitud, responde enviando su dirección MAC directamente al dispositivo que hizo la solicitud.
Una vez que el dispositivo que realizó la solicitud recibe la respuesta ARP, guarda tanto la dirección IP como la dirección MAC en su caché ARP. Esto le permite evitar futuras solicitudes ARP para la misma dirección IP durante un período de tiempo determinado, ya que puede usar la información almacenada en su caché para comunicarse directamente con el dispositivo de destino. A continuación, se puede ver el caché ARP de h1 con la dirección IP y MAC del router.

<img  src="https://github.com/user-attachments/assets/43e4e585-1135-4f80-aa51-f32fb73aa9fc" width="600" align="center" />

En la tabla ARP de h1 se puede identificar la dirección MAC del router, mientras que en la tabla ARP de h3 no se encuentra ninguna dirección, ya que no se han enviado paquetes hacia ese dispositivo ni ha recibido paquetes.

<img src="https://github.com/user-attachments/assets/587d48c3-8b9a-4857-940d-cd317e4d88d1" width="600" align="center" />

Por otro lado, la tabla ARP de h2 contiene la dirección IP y la MAC de la interfaz GigabitEthernet 0/0/1 del router.

<img src="https://github.com/user-attachments/assets/e7bacdaf-6e9d-46d1-8a27-113e0c19661c" width="600" align="center" />

En la tabla ARP del router se encuentran las direcciones IP y MAC de h1, h2, GigabitEthernet 0/0/0 y GigabitEthernet 0/0/1, así como el tiempo de vida de cada entrada y la interfaz a la que pertenecen. 

<img src="https://github.com/user-attachments/assets/f5034ef6-d854-49c1-880d-faaf5a1c4a8a" width="600" align="center" />

En los datagramas se observan las direcciones IP de origen y destino, las cuales son utilizadas para encaminar los paquetes correctamente a través de la red.
El enrutador determina la comunicación entre dos hosts examinando la dirección IP de destino del paquete y utilizando su tabla de enrutamiento para determinar la mejor ruta hacia ese destino. Luego, reenvía el paquete a través de la interfaz de red adecuada hacia el siguiente salto en la ruta hacia el destino final.

<img src="https://github.com/user-attachments/assets/b8ae719a-04d6-4078-9890-0f9cf9898321" width="600" align="center" />

El switch es un dispositivo utilizado para conectar múltiples dispositivos dentro de una misma red local (LAN). A diferencia de otros dispositivos como los routers, el switch no necesita direcciones IP, ya que su función principal es dirigir los paquetes de datos basándose en las direcciones MAC de los dispositivos conectados.

Uno de los principales beneficios de utilizar un switch es su capacidad para conectar diversos dispositivos de red, como computadoras, impresoras y servidores, dentro de la misma red local. Además, un switch divide la red en segmentos más pequeños, lo cual contribuye a reducir la congestión y mejorar el rendimiento de la red, limitando el tráfico transmitido a través de cada uno de sus puertos.

Otra ventaja importante es el envío selectivo de los paquetes de datos. El switch identifica la dirección MAC de destino de cada paquete y lo envía solo al puerto de salida correspondiente, lo que optimiza la eficiencia en la transmisión de datos dentro de la red. Además, el switch aprende las direcciones MAC de los dispositivos conectados a sus puertos y construye una tabla de direcciones MAC para determinar la ruta más adecuada para los paquetes entrantes.

A diferencia de los hubs, los switches son capaces de detectar y evitar colisiones de datos, ya que pueden transmitir información simultáneamente a través de diferentes puertos. Esto asegura una mayor fiabilidad en la transmisión de datos dentro de la red.

En cuanto al marco teórico, las direcciones de broadcast en IPv4 son direcciones especiales que permiten enviar un paquete de datos a todos los dispositivos de una red. Estas direcciones se representan con una dirección IP en la que todos los bits correspondientes al host están configurados en 1. En la red Ethernet, la dirección de broadcast se utiliza con la dirección MAC FFFF.FFFF.FFFF.

Por otro lado, las direcciones de multicast en IPv4 son utilizadas para enviar un paquete de datos a un grupo específico de dispositivos dentro de una red. Las direcciones multicast se encuentran en el rango reservado de direcciones IP de clase D, que va desde 224.0.0.0 hasta 239.255.255.255. Los dispositivos que deseen recibir los paquetes multicast deben unirse al grupo multicast correspondiente, lo que permite una distribución más eficiente de los datos dentro de la red.

Se inició tráfico ICMPv3 (IPv6) entre h1 y h3 y analizamos el mismo sobre las dos redes.

<img src="https://github.com/user-attachments/assets/ab525262-d5e5-49d6-ac92-0c4a529ec4a5" width="600" align="center" />

Se identificaron comunicaciones NDP, algunos mensajes de este tipo que suceden son los de solicitud de vecinos y de anuncio de vecinos como los que se ven a continuación:

<img src="https://github.com/user-attachments/assets/04493401-668c-4eb8-83c9-975835f0ade3" width="600" align="center" />

A continuación se puede observar como el router reconoció a los vecinos y mapeo las direcciones MAC de la capa de linkeo:

<img src="https://github.com/user-attachments/assets/c93ddcde-4ab6-4cf8-bf6a-3b2e0ce858e4" width="600" align="center" />

El protocolo NDP (Neighbor Discovery Protocol) en IPv6 cumple un rol equivalente al ARP (Address Resolution Protocol) en IPv4. Su propósito principal es ayudar a los dispositivos a resolver direcciones y descubrir información relevante dentro de la red local. A través de mensajes de solicitud y respuesta, NDP permite a los dispositivos IPv6 identificar las direcciones MAC de los dispositivos vecinos cuando se conoce su dirección IP. Este proceso se lleva a cabo mediante los mensajes de Neighbor Solicitation (NS) y Neighbor Advertisement (NA).

Además, NDP facilita el descubrimiento de dispositivos en la misma red local. Para ello, utiliza los mensajes de Router Solicitation (RS) y Router Advertisement (RA), que permiten a los dispositivos identificar los routers disponibles y obtener la información necesaria sobre la configuración de la red. En paralelo, también se emplean los mensajes NS y NA para descubrir otros dispositivos IPv6 vecinos.

Otro aspecto importante de NDP es su capacidad para permitir la autoconfiguración de direcciones IPv6. Esto elimina la necesidad de servidores DHCP, ya que los dispositivos pueden auto asignarse direcciones IPv6 únicas. A través de los mensajes de NS y NA, los dispositivos pueden verificar si la dirección IPv6 que intentan configurar está duplicada en la red, asegurando así una asignación correcta.

NDP también juega un papel clave en el descubrimiento de prefijos. Informa a los dispositivos sobre los prefijos utilizados en la red, facilitando la autoconfiguración de direcciones IPv6 y asegurando que la conectividad se mantenga sin problemas.

En cuanto a la función de broadcast, que en IPv4 permite enviar paquetes a todos los dispositivos de una red, IPv6 la reemplaza con multicast. En lugar de inundar la red con paquetes, IPv6 envía los paquetes solo a un grupo específico de dispositivos interesados en recibirlos. Esto ayuda a reducir el tráfico de red y mejora la eficiencia de las comunicaciones.

Por último, las direcciones en IPv6 se dividen en tres tipos: link-local, unique-local y global. Las direcciones link-local, que comienzan con el prefijo FE80::/10, se utilizan para la comunicación dentro de la misma red local y no son enrutables fuera de ella. Son esenciales para la comunicación entre dispositivos en una misma subred. Las direcciones unique-local, con el prefijo FC00::/7, son únicas dentro de una red privada, similar a las direcciones privadas en IPv4, y se usan en redes corporativas o privadas. Finalmente, las direcciones globales, que comienzan con el prefijo 2000::/3, son públicas y se utilizan para la comunicación en Internet, siendo enrutable a nivel global.

### Parte 2 - Implementación de la red
Se utilizó un switch Cisco Catalyst 2960, un equipo de Capa 2 pensado para ofrecer conectividad estable en redes empresariales. Cuenta con 24 o 48 puertos Fast Ethernet, además de puertos Gigabit Ethernet para enlaces ascendentes, lo que permite una mejor escalabilidad de la red.

El equipo soporta funciones de seguridad, como control de acceso mediante 802.1X y listas de control de acceso (ACLs), lo que ayuda a gestionar el tráfico de manera segura. Además, algunos modelos incluyen Power over Ethernet (PoE), facilitando la alimentación de dispositivos sin necesidad de cables adicionales.

<img src="https://github.com/user-attachments/assets/6992a619-b824-4410-a0e6-6d8757a020b9" width="900" align="center" />

b) Para acceder a la configuración del switch Cisco Catalyst 2960, se ingresó al modo privilegiado a través de la consola. Primero, se solicitó la verificación de acceso, donde se introdujo la contraseña de usuario. Luego, mediante el comando enable, se accedió al modo privilegiado, lo que permitió ejecutar configuraciones avanzadas en el dispositivo.

Posteriormente, con "configure terminal", se ingresó al modo de configuración global, lo que permitió realizar ajustes en la seguridad del dispositivo donde se estableció una contraseña de acceso y posteriormente se utilizó exit para salir del modo de configuración y volver al modo privilegiado.

![image](https://github.com/user-attachments/assets/e2ccb18e-7549-4583-90d1-a511e1953dce)

c) Siguiendo con el desarrollo de las actividades se estableció una conexión entre el switch y varios dispositivos a los fines de verificar la conectividad, esto se realizo mediante el comando "ping" como se muestra a continuación:

<img src="https://github.com/user-attachments/assets/04587d97-6af1-4d62-a78c-c822f7591975" width="450" align="center" />

<img src="https://github.com/user-attachments/assets/7925c656-333f-4756-90cb-dae15cb4e48d" width="450" align="center" />

d) Realizamos las sigueintes actividades para configurar un puerto del switch en modo mirroring y utilizar una tercera computadora para supervisar el trafico entre otras 2:
  1. Acceder al switch mediante un software de emulación de terminal, como PuTTY.

  2. Ingresamos al modo de configuración global ejecutando el comando enable.

  3. Entramos en el modo de configuración de interfaz con el comando configure terminal.

  4. Definimos el puerto de monitoreo (destino) con el comando monitor session 1 destination interface [número-de-puerto].

  5. Especificamos los puertos origen (los que serán supervisados) utilizando monitor session 1 source interface [número-de-puerto].

  6. Establecemos el tipo de tráfico a capturar con monitor session 1 filter [tipo-de-tráfico].

  7. Conectamos la tercera computadora al puerto de monitoreo del switch.

Luego de esto monitoreamos el trafico entre las 2 maquinas usando el software de analisis de red Wireshark. 

![f1](https://github.com/user-attachments/assets/12547fea-4cb5-486a-af85-5789b0d1243b)

En donde podemos observar comunicaciones ARP y las direcciones IP.

![f2](https://github.com/user-attachments/assets/77058afd-2f85-4efc-9c3f-2ab4c3266e91)
![f3](https://github.com/user-attachments/assets/75d578ec-a25c-4cc4-94ce-84128f3cc15e)
![f4](https://github.com/user-attachments/assets/50904990-93f5-482a-a925-45675a5328b3)

