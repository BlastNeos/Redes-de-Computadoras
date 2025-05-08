# Ruteo externo dinámico (Border Gateway Protocol (BGP)) y sistemas autónomos (Autonomous Systems (AS))


## Parte I - Integración de conceptos, actividades online e investigación

### 1) Investigar y elaborar reportes sobre los siguientes conceptos e información sobre AS:

a) Un Autonomous System (AS) es un conjunto de redes IP y routers bajo un mismo control administrativo que comparten una política de enrutamiento común. Estos sistemas suelen pertenecer a proveedores de servicios de Internet, grandes empresas, universidades u organizaciones gubernamentales, y son la unidad básica sobre la que se asienta el enrutamiento global en Internet.
Una forma simplificada es pensarlo como la oficina de correos de una ciudad. El correo va de una oficina de correos a otra hasta que llega a la ciudad correcta, y la oficina de correos de esa ciudad entregará el correo en esa ciudad. Del mismo modo, los paquetes de datos recorren Internet saltando de AS a AS hasta que llegan al AS que contiene su dirección de Protocolo de Internet (IP) de destino. Los enrutadores dentro de ese AS envían el paquete a la dirección IP.

b) A cada AS se le asigna un número oficial, o número de sistema autónomo (ASN), de forma similar a como cada empresa tiene una licencia comercial con un número oficial único. Pero, a diferencia de las empresas, las partes externas suelen referirse a los AS solo por su número, los cuales son números únicos de 16 bits entre 1 y 65534, o de 32 bits entre 131072 y 4294967294.
Para evitar la proliferación innecesaria de entradas en la tabla de enrutamiento global, solo se debe asignar un nuevo ASN cuando realmente se requiera una política de enrutamiento distinta. Compartir un mismo ASN entre redes no gestionadas de forma conjunta implica una mayor coordinación entre los administradores de red y, en ocasiones, puede conllevar la necesidad de rediseñar en parte la infraestructura.
LACNIC asignará Números de Sistema Autónomo a aquellas organizaciones que cumplan los siguientes requisitos:
Estar multihomed con dos o más Sistemas Autónomos al momento de la solicitud, o bien prever alcanzar dicha situación en un plazo máximo de dos semanas desde la presentación de la petición.
Presentar una documentación detallada de su política de enrutamiento, única y diferente de la del ASN al que esté conectada.

c) Algunos ejemplos de ASN de empresas o universidades son:

AS27790 – Universidad Nacional de Córdoba (Registro LACNIC, tipo Educación)

AS15169 – Google LLC (Registro ARIN, tipo Hosting)

AS13335 – Cloudflare, Inc. (Registro ARIN, tipo Hosting)

d) Se analizó el ASN de la conexión actual de la PC y se muestra a continuación la información recopilada:

Se presenta un resumen de la conexión usando ipinfo.io como herramienta para facilitar esta información. A continuación, las características principales de la red:

![image](https://github.com/user-attachments/assets/2730a096-24cf-48ce-b172-cc2b125cf732)

A continuación se agregan las características de la red, donde se detallan a que pais pertenece,se muestra que gestiona más de 27.000 dominios alojados y posee aproximadamente 8,4 millones de direcciones IPv4 y soporte completo para IPv6, con un rango de 3,26 × 10³² direcciones. 

![image](https://github.com/user-attachments/assets/9c0f082d-61a9-49e6-8068-4ffbf93c57a2)

### 2) Investigar y elaborar reportes sobre los siguientes conceptos e información sobre BGP:

a) El Border Gateway Protocol (BGP) es el protocolo de enrutamiento principal que permite la interconexión y el intercambio de información de rutas entre diferentes Sistemas Autónomos (AS) en Internet. Está diseñado como un protocolo de vector de ruta y toma decisiones de enrutamiento basadas en atributos como el número de AS atravesados, la preferencia de ruta y políticas definidas por los administradores de red. Esto proporciona un control granular sobre cómo se enruta el tráfico entre distintas redes, garantizando estabilidad y eficiencia.

b) El funcionamiento de BGP se basa en una serie de procedimientos y el intercambio de mensajes específicos para establecer y mantener las rutas entre routers BGP.
Procedimientos funcionales:
Adquisición de vecino: Los routers BGP establecen una conexión TCP (generalmente en el puerto 179) para formar una relación de vecino. Esta conexión es esencial para el intercambio de información de enrutamiento.


Detección de vecino alcanzable: Una vez establecida la conexión, los routers envían periódicamente mensajes de mantenimiento para asegurarse de que el vecino sigue activo y la sesión BGP está operativa.


Detección de red alcanzable: Los routers intercambian información sobre las rutas disponibles, permitiendo a cada uno construir una tabla de enrutamiento que refleje las rutas más eficientes y actuales hacia diferentes destinos.


Tipos de mensajes BGP: BGP utiliza cuatro tipos principales de mensajes para llevar a cabo sus funciones:
OPEN: Este mensaje inicia la sesión BGP entre dos routers. Incluye información como la versión de BGP, el número de AS del emisor, el identificador del router y parámetros opcionales.

UPDATE: Utilizado para anunciar nuevas rutas o retirar rutas previamente anunciadas. Este mensaje contiene información sobre los prefijos de red y los atributos asociados que ayudan a determinar la mejor ruta.

KEEPALIVE: Enviado periódicamente para mantener activa la sesión BGP. Si un router no recibe un mensaje KEEPALIVE o UPDATE dentro de un tiempo determinado (conocido como "Hold Time"), considera que la sesión ha fallado.

NOTIFICATION: Se utiliza para informar sobre errores o condiciones que requieren la terminación de la sesión BGP. Este mensaje incluye un código de error y, opcionalmente, datos adicionales que describen la naturaleza del problema.

c)
El BGP externo, también conocido como eBGP, es utilizado para el intercambio de información de enrutamiento entre diferentes sistemas autónomos (AS). Esta conexión se da entre los routers de los distintos AS (fuera del AS) y garantiza un camino libre de loops. Por otra parte el BGP interno se utiliza para intercambiar información sobre rutas dentro del AS, las conexiones se realizan entre los diferentes routers de la red que conforma el AS.

**Análisis del ejemplo**

![image](https://github.com/user-attachments/assets/7ccada02-0855-4767-8177-1fea029bb27d)

Un AS se considera de tránsito cuando permite el tránsito de datos a través de él para llegar a otros AS. Según la definición anterior, podemos concluir que AS2 es un AS de tránsito ya que permite el intercambio de AS1 y AS3.

d) Para analizar el entorno de mi AS se utilizó la herramienta de bgpview.io donde se recolectó la siguiente información:
![image](https://github.com/user-attachments/assets/663902d4-1cd7-478f-9bff-8651b5095fb3)

![image](https://github.com/user-attachments/assets/9411a2c0-9324-4241-950f-75ca5f5ef0fa)

e) Asimismo de analizó una red distinta, específicamente el 4G de la red móvil y a continuación se muestran las conexiones sobre una nueva ASN.

![image](https://github.com/user-attachments/assets/aa5dbe15-97bb-4341-a171-bd97bd88829c)

![image](https://github.com/user-attachments/assets/63ebc5a2-045f-4d9a-a775-0ef5dae42ee2)


f) Se investigó sobre un problema de enrutamiento que tuvo un impacto importante, el cual fue el que ocurrio en 2021. 

Más especificamente el 4 de octubre de 2021, Facebook y sus servicios asociados—Instagram, WhatsApp, Messenger y Oculus—experimentaron una interrupción global de seis horas debido a un error de configuración en BGP.

**Causas**
Durante una tarea rutinaria de mantenimiento, los ingenieros de Facebook ejecutaron un comando destinado a evaluar la capacidad de la red troncal global. Sin embargo, este comando accidentalmente desconectó todos los centros de datos de Facebook. Como resultado, los servidores DNS (Domain Name System) de la empresa, que estaban diseñados para retirarse del enrutamiento BGP si no podían conectarse a los centros de datos, se volvieron inaccesibles desde Internet. Esto impidió que los usuarios resolvieran los nombres de dominio de Facebook y accedieran a sus servicios.

**Consecuencias**
-Interrupción de servicios: Los usuarios no pudieron acceder a Facebook y sus plataformas asociadas, lo que afectó tanto a la comunicación personal como a las operaciones comerciales que dependen de estas plataformas.

-Impacto en otras plataformas: La caída de Facebook provocó un aumento significativo del tráfico en otras aplicaciones de mensajería y redes sociales como Twitter, Telegram y Signal, algunas de las cuales experimentaron ralentizaciones debido al incremento inesperado de usuarios.

-Problemas internos en Facebook: La interrupción también afectó a las herramientas internas de comunicación y autenticación de Facebook, dificultando la capacidad de los empleados para diagnosticar y resolver el problema de manera remota.

-Repercusiones económicas: Durante las horas de inactividad, las acciones de Facebook cayeron aproximadamente un 5%, y se estimó que el patrimonio neto del CEO, Mark Zuckerberg, disminuyó en más de 6 mil millones de dólares.

Este incidente destacó la fragilidad de la infraestructura de Internet y la importancia de una gestión cuidadosa de los protocolos de enrutamiento como BGP. También subrayó la necesidad de implementar medidas de seguridad adicionales, como la validación de rutas mediante RPKI (Resource Public Key Infrastructure), para prevenir errores de configuración que puedan tener consecuencias de gran alcance.


## Parte II - Simulaciones y análisis
Se implementó la siguiente red en packet tracer: 

![image](https://github.com/user-attachments/assets/8b71f643-405f-4423-a2b0-1d0094bfb7bc)

1) Configuración BGP en en router:
	show running-config | section router bgp
	 
	Se aplicó ese comando sobre Router0, De esta salida podemos observar:
●	router bgp 100: El router está configurado para usar BGP con AS100.
●	no synchronization: Sincronización deshabilitada.
●	neighbor 10.0.0.2 remote-as 200: Relación de vecindad con un router de dirección 10.0.0.2 en AS200 (Sesión BGP entre dos AS).
●	network 192.168.1.0: Indica que la red 192.168.1.0/24 se comparte a través de BGP para que otros routers la aprendan.

Los vecinos BGP (Router0) se visualizan mediante "show ip bgp summary"

![image](https://github.com/user-attachments/assets/1f8e5ee6-5388-46b7-8256-20d966e50fe0)

Se analizó la información y se muestra a continuación las conclusiones:

●  Identificador BGP: 192.168.1.1 y AS100.

●  Versión de la tabla BGP: 3 y versión de tabla de ruteo: 6 (Son las veces que estas tablas se han actualizado).

●  2 rutas BGP activas y 2 caminos activos, sin eliminaciones recientes.

●  Un vecino en la AS200 con dirección 10.0.0.2

○  V: versión de BGP.

○  Mensajes recibidos desde el vecino: 27.

○  Mensajes enviados: 26.

○  Versión de la tabla BGP: 3.

○  No hay mensajes pendientes.

○  Tiempo activo.

Para ver  la tabla BGP se utilizó “show ip bgp”

![image](https://github.com/user-attachments/assets/cd415430-6ef1-47b6-ab30-ebb441683bd9)

La primera dirección está directamente conectada mientras que la segunda dirección, tiene 200 i en path, lo que significa que esa ruta fue aprendida a través del AS200.

2) Posteriormente se comprobó la conectividad entre los hosts de cada AS
● PC0 a PC2

![image](https://github.com/user-attachments/assets/dea0bd17-e325-45fb-8a2e-2e1b6b8aa723)

● PC0 a PC3

![image](https://github.com/user-attachments/assets/e4a7751b-d04b-43c6-868c-316c9ce8e42b)

● PC1 a PC2

![image](https://github.com/user-attachments/assets/7d0e956d-98ee-4513-b8cf-010df9252919)

3) Asismismo se simuló tráfico en la red mientras se habilitaban o deshabilitaban algunos de los routers, y se analizó el tráfico visualizado.
   
● Tracert desde PC0 a PC3 sin apagar nada.

![image](https://github.com/user-attachments/assets/ceee2ba5-29fe-4d9d-8dc8-f0c4b1b80b52)

● Tracert desde PC0 a PC3 apagando Router0

![image](https://github.com/user-attachments/assets/74ee5e9a-e7bb-4431-bff4-b0816d004bc4)

4) Se agregó la configuración IPv6 pero tener en cuenta que IPv6 NO es compatible con packet tracer, por lo que solo asignamos la direcciones.
5) A continuación se muestra el diseño de la red en una tabla de las siguientes características:

![image](https://github.com/user-attachments/assets/a5da598f-efd8-47dc-ac73-746deaffca88)

![image](https://github.com/user-attachments/assets/42babf86-a66b-4418-a331-3edb365e3e64)


6) Se añadió un router en el sistema autónomo AS100, un switch conectado a dicho router, y un quinto host (h4) conectado a este switch.

![image](https://github.com/user-attachments/assets/f3b57927-c94e-4ce5-83a9-45638b9272b0)

Se agregó el router extra, con un switch y una pc con la siguiente configuración:

![image](https://github.com/user-attachments/assets/56288dce-e539-4e31-a7bd-a0307604c444)

7) A continuación se muestran las rutas estaticas configuradas
   
● Configuración OSPF en Router0:

![image](https://github.com/user-attachments/assets/391cf988-bf0e-4383-a01f-ebe017f39af4)

● Configuración OSPF en Router1:

![image](https://github.com/user-attachments/assets/61d66eda-ff8f-484f-9e70-a1fd16e0a50e)

● Configuración OSPF en Router2:

![image](https://github.com/user-attachments/assets/368c9dd6-baba-4ab4-8d81-7de67cb7b247)

8) Se redistribuye OSPF en BGP, el analisis y la configuración se muestra a continuación:

![image](https://github.com/user-attachments/assets/d4d4148f-ee3a-4198-9b14-a390c9605205)

![image](https://github.com/user-attachments/assets/174531aa-9aa9-41cf-bedb-476771b0cc73)

● Configuración BGP de Router1:

![image](https://github.com/user-attachments/assets/5646b12f-8d85-4b53-8bcd-d09a8b125b6f)

Tabla de ruteo de Router0:

![image](https://github.com/user-attachments/assets/b4f215b3-2adc-4225-839a-5a46e10ca767)

Tabla de ruteo de Router1:

![image](https://github.com/user-attachments/assets/e4d834d8-17cb-47b0-b21a-baaa54d6b265)

Tabla de ruteo de Router2:

![image](https://github.com/user-attachments/assets/10f8696d-c2a7-4667-8dc0-4b17881de1a6)

Se puede observar en las tablas de ruteo que cada uno conoce cómo llegar a un dispositivo dentro de una red a través de otra, es decir, esta tabla indica el camino para redirigir el paquete de datos y a través de qué redes para que este pueda llegar a destino. Por ejemplo en Router2 se observa que la red 192.168.1 es alcanzable a través del dispositivo conectado a 10.10.10.1, mientras que la red 192.168.3.0 está conectada directamente a el.

9) Se comprueba la conectividad entre los hosts de ambos sistemas autónomos con h4:

PC4 ping hacia PC0 y PC1:

![image](https://github.com/user-attachments/assets/b0026033-4808-43a2-8858-83647c16228e)

PC4 ping hacia PC2 y PC3:

![image](https://github.com/user-attachments/assets/d9da80f1-ddcf-4827-8a2d-2db1a5986db7)



