
---

# Configuración y Análisis de tráfico IPv4/IPv6
  
**Federico I Soria**
**Fernando Zarate**  
**Ping Slayers**

**Facultad de Ciencias Exactas, Fisicas y Naturales**  
**Redes de Computadoras**
**Profesores** (para publicaciones de alumnos)  
**Marzo 2024**  

---

## Resumen
Este trabajo se enfoca en el estudio de los principios fundamentales que rigen la comunicación entre dispositivos dentro de una red de computadoras. Se analizan los modelos de interconexión, con especial énfasis en las capas de enlace de datos, red y transporte, y su rol en la entrega eficiente de información. Asimismo, se examina el funcionamiento de los protocolos de comunicación, resaltando la encapsulación y desencapsulación de datos como procesos clave para garantizar la interoperabilidad entre diferentes sistemas de red.

Palabras clave: interconexión de redes, protocolos de comunicación, encapsulación, desencapsulación

## Introducción

# Marco teórico / Modelo / Metodología
El crecimiento de las redes de conmutación y difusión de paquetes surgió de la necesidad de ampliar el acceso a recursos más allá de sistemas individuales, lo que llevó a la interconexión de múltiples redes para facilitar la comunicación entre estaciones de diferentes redes. La interconexión entre redes, o internetworking, implica la conexión de redes individuales a través de puentes o dispositivos de enrutamiento, permitiendo que aparezcan como una red única para los usuarios. Se distinguen redes individuales y subredes constituyentes, con sistemas finales (ES) conectados a ellas y dispositivos intermedios (IS) que facilitan la comunicación entre diferentes redes. Se destacan dos tipos de IS: puentes, que operan en la capa 2 del modelo OSI y conectan redes LAN similares, y dispositivos de enrutamiento, que operan en la capa 3 y conectan redes potencialmente diferentes. Los requisitos para un sistema de interconexión entre redes incluyen proporcionar enlace, encaminamiento de datos, contabilidad, y adaptabilidad a las diferencias entre las redes interconectadas. Los enfoques de arquitectura pueden ser orientados a conexión o no orientados a conexión, con funciones clave como retransmisión y encaminamiento en el primero, y enrutamiento independiente por unidad de datos en el segundo, donde se destacan protocolos como el Protocolo de Internet (IP) para la interconexión.
El Protocolo Internet (IP) es un componente fundamental del conjunto de protocolos TCP/IP y es ampliamente utilizado para la interconexión de redes. Actualmente, la versión 4 de IP (IPv4) es el estándar predominante en las redes TCP/IP, a pesar de los esfuerzos para migrar hacia IPv6.

IPv4 define tanto los servicios que proporciona como el formato del protocolo y sus mecanismos asociados. Los servicios de IP incluyen primitivas como Send (envío) y Deliver (entrega), que se utilizan para solicitar la transmisión de datos y notificar la llegada de datos, respectivamente. Los parámetros asociados a estas primitivas incluyen direcciones de origen y destino, indicadores de tipo de servicio, identificadores únicos para los datos y opciones adicionales para extensiones futuras.
El formato del datagrama IPv4 incluye varios campos importantes, como versión, longitud de cabecera, tipo de servicio, longitud total, identificador, indicadores, tiempo de vida, protocolo, suma de comprobación, direcciones de origen y destino, opciones y datos. Estos campos son cruciales para el enrutamiento y la entrega de datos a través de la red.
Las direcciones IP, codificadas en formato de 32 bits, se utilizan para identificar los dispositivos en una red. Las direcciones se clasifican en tres clases principales (A, B y C), que permiten una asignación flexible de direcciones según el tamaño y la estructura de la red.
El concepto de subredes se introdujo para permitir una mayor flexibilidad en la asignación de direcciones IP dentro de una red. Esto involucra la subdivisión de una red en subredes más pequeñas, cada una con su propia dirección de red y un rango de direcciones para dispositivos individuales.
El Protocolo de Mensajes de Control de Internet (ICMP) es esencial para proporcionar información de retroalimentación sobre problemas de comunicación en la red. ICMP se utiliza para enviar mensajes de error, redireccionamiento, eco y tiempo de respuesta, entre otros, lo que facilita el diagnóstico y la resolución de problemas de red.
El protocolo de interconexión IP, utilizado en Internet, proporciona un servicio no orientado a conexión, lo que significa que los datos se transmiten como datagramas entre sistemas finales sin establecer previamente una conexión. Esto ofrece flexibilidad y robustez, ya que puede adaptarse a una variedad de redes y condiciones de red. En este esquema, cada dispositivo de enrutamiento determina la ruta de los datagramas hacia su destino, lo que puede incluir fragmentación y reensamblado de datos según las características de las redes intermedias. Aunque este servicio no garantiza la entrega de datos ni su orden, es altamente adaptable y puede funcionar en una variedad de entornos de red. El protocolo IP también incluye mecanismos para el encaminamiento, control de errores, control de flujo y limitación del tiempo de vida de los datagramas para garantizar un funcionamiento eficiente y fiable en Internet y otras redes.
	El Protocolo de Internet (IP) ha sido el pilar de Internet y la mayoría de las redes privadas durante mucho tiempo. Sin embargo, con el agotamiento de direcciones en IPv4, surgió la necesidad de una nueva versión, IPv6, para reemplazarla. IPv6 ofrece mejoras significativas, como un espacio de direcciones más amplio, mecanismos de opciones mejorados, autoconfiguración de direcciones y flexibilidad en el direccionamiento. A continuación, se describen la estructura y características principales de IPv6.
IPv6 utiliza direcciones de 128 bits, proporcionando un espacio de direcciones enormemente ampliado en comparación con IPv4. Además, ofrece una mejorada cabecera de opciones y autoconfiguración de direcciones, permitiendo la asignación dinámica de direcciones.
La estructura de un paquete IPv6 consta de una cabecera principal IPv6 y cabeceras de extensión opcionales. Las cabeceras de extensión pueden incluir opciones salto a salto, encaminamiento, fragmentación, autenticación, encapsulamiento de seguridad y opciones para el destino. Estas cabeceras proporcionan funcionalidades adicionales y mejoras en el procesamiento de paquetes.
Las direcciones IPv6 son de 128 bits y se asignan a interfaces individuales en los nodos. Se pueden utilizar tres tipos de direcciones: unidifusión (unicast), monodifusión (anycast) y multidifusión (multicast). IPv6 también introduce la etiqueta de flujo, que identifica secuencias de paquetes con requisitos de tratamiento especial.
La fragmentación en IPv6 solo puede ser realizada por el nodo origen, no por los dispositivos de encaminamiento intermedios. La cabecera de fragmentación contiene información sobre la posición del fragmento en el paquete original y el identificador único del paquete.
La cabecera de encaminamiento permite especificar una lista de nodos intermedios en la ruta del paquete. Cada cabecera de encaminamiento comienza con un bloque de 32 bits seguido de datos específicos al tipo de encaminamiento.

## Desarrollo



## Resultados


## Discusión y conclusiones

## Referencias

3) Investigar y explicar las diferencias entre un simulador y un emulador, en el contexto de redes.



4) Evaluar conectividad entre todos los host enviando 3 (tres) paquetes ICMPv4, utilizando el comando
ping para IPv4.
5) Evaluar conectividad entre todos los host enviando 3 (tres) paquetes ICMPv6, utilizando el comando
ping6 para IPv6.

6) Iniciar trá

co ICMP en el Cliente 1 con destino Cliente 2. Analizar trá

co sobre las dos redes, capturar

screenshots y responder las siguientes preguntas:
a) ¿Cuáles son las comunicaciones ARP que observan? Explicar y ejempli

car con capturas cómo

funciona la traducción de direcciones lógicas a direcciones físicas.
b) ¿Cuáles son las direcciones IP en los datagramas? Indicar con un ejemplo.
c) ¿Cómo determina el enrutador la comunicación entre un host y otro?
d) ¿Para qué usamos el switch? ¿Por qué el switch no tiene asignadas direcciones IP en sus interfaces?
e) ¿Qué datos contiene la tabla ARP de h1?
f) ¿Qué datos contiene la tabla ARP de h3?
g) ¿Qué datos contiene la tabla ARP del router?
h) ¿Qué son las direcciónes de broadcast en IPv4? ¿Cuál es su utilidad?
i) ¿Qué son las direcciónes de multicast en IPv4? ¿Cuál es su utilidad?
7) Iniciar trá

co ICMPv3 (IPv6) entre h1 y h3. Analizar el trá

co sobre las dos redes, capturar screenshots y

responder las siguientes preguntas:
a) ¿Cuáles son las comunicaciones NDP que suceden? Identi

que los distintos tipos de mensajes

NDP haciendo foco en las direcciones IP de origen y destino de cada uno.
b) ¿NDP reemplaza a ARP?
c) Describir las funciones de NDP
d) ¿Cómo se reemplaza la función de broadcast en IPv6?
e) ¿Cuál es la diferencia entre las direcciones link-local, unique-local y global? ¿En qué caso usaría
cada una? Ejempli
car.