# Ruteo dinámico OSPF en ambiente virtual

OSPF (Open Shortest Path First) es un protocolo de enrutamiento interno (IGP, Interior Gateway Protocol) que utiliza el algoritmo de estado de enlace (link-state) para determinar las rutas más eficientes dentro de una red autónoma (AS). OSPF es un protocolo dinámico, lo que significa que actualiza las rutas automáticamente en respuesta a cambios en la topología de la red.
Clases de redes IP
Las direcciones IPv4 originalmente se dividían en cinco clases (A, B, C, D y E), de las cuales las más utilizadas son:
Clase A: 0.0.0.0 a 127.255.255.255 (máscara por defecto: 255.0.0.0). Grandes redes con muchos hosts.

Clase B: 128.0.0.0 a 191.255.255.255 (máscara: 255.255.0.0). Redes medianas.

Clase C: 192.0.0.0 a 223.255.255.255 (máscara: 255.255.255.0). Redes pequeñas.

Clase D: 224.0.0.0 a 239.255.255.255. Para multicast.

Clase E: 240.0.0.0 a 255.255.255.255. Reservada para uso futuro

##Teoría de grafos aplicada a redes y OSPF

La teoría de grafos es fundamental para comprender el funcionamiento de protocolos de enrutamiento como OSPF. En este contexto:
Cada router se representa como un nodo (vértice) del grafo.

Cada enlace de red (por ejemplo, una conexión entre routers) se representa como una arista (edge).


A cada arista se le asigna un peso, que puede representar el costo del enlace, el retardo, el ancho de banda, etc.


OSPF construye un grafo dirigido y ponderado de la red, conocido como Link-State Database (LSDB), y aplica el algoritmo de Dijkstra para calcular el árbol de rutas más cortas desde sí mismo hacia todos los otros nodos. Este árbol se usa para llenar la tabla de enrutamiento.

![image](https://github.com/user-attachments/assets/12d71f1f-9bb6-457b-91ef-95ea38f61598)

Elaboramos la siguiente tabla de direccionamiento

![image](https://github.com/user-attachments/assets/09f4d7ab-ce9c-48fa-9919-d86f95ae53c2)

3)Se configuró cada router para que utilice el protocolo de comunicación OSPF de la siguiente forma:

*Configuracion router 0 para protocolo OSPF*

![image](https://github.com/user-attachments/assets/b1d42a90-9094-406b-b459-f6e11fe2f8f9)

*Configuración router1 para protocolo OSPF*

![image](https://github.com/user-attachments/assets/394f660d-9046-4fa0-b244-ab34928daea7)

Ahora se procedió a probar la conectividad entre las computadoras, se muestra a continuación la prueba de conectividad entre PC0 con PC1 y PC2 mediante un ping.

![image](https://github.com/user-attachments/assets/85aa91d5-586f-4285-b490-66f277f7cf78)

Ahora se prueba la conectividad con las pc que están en las otras redes 

*Conectividad entre PC0 con PC3 y PC4 de las otras redes*

![image](https://github.com/user-attachments/assets/761111ae-d508-4ab7-a94d-9cd1be8a0611)

*Conectividad entre PC1 con PC3 y PC4*

![image](https://github.com/user-attachments/assets/7c6590d0-f930-4a53-858a-19f824066e4c)

*Conectividad entre PC2 con PC3 y PC4*

![image](https://github.com/user-attachments/assets/b733a382-1ae3-4e2c-88a0-c9536cb7679b)

*Conectividad entre PC4 con PC3*

Ahora se verifica que las tablas de enrutamiento contienen rutas OSPF mediante el comando show ip route OSPF en cada router:

![image](https://github.com/user-attachments/assets/c2b9a300-b1c2-4c48-a9af-75baee329eb2)

![image](https://github.com/user-attachments/assets/d1823014-1531-4058-b533-e61066069bf6)

![image](https://github.com/user-attachments/assets/57c58267-02b6-4a71-98ec-9c1b963c9d33)

![image](https://github.com/user-attachments/assets/1c5cfa18-c209-4e68-8a18-b42ccb589af0)

![image](https://github.com/user-attachments/assets/3a48f6c8-ac4c-4900-9d84-33805ba932b8)

Se analizaron los mensajes de OSPF para comprender su funcionamiento y su impacto en la red.

Tipos de mensajes OSPF
Hello: descubrir y mantener vecinos
Database Description: describir la base de datos de LSAs
Link-State Request: solicitar información específica
Link-State Update: enviar información de enrutamiento 
Link-State Acknowledgment:	confirmar recepción de LSAs

Se realizó un analisis paso a paso del proceso OSPF donde se descubren vecinos (Hello) mediante el comando show ip ospf neighbor

![image](https://github.com/user-attachments/assets/da67002f-4308-4bf1-9f1d-51078a86a71c)

Se activa el modo simulación para filtrar por OSPF y al seleccionar cada paquete se puede visualizar el contenido del mensaje.

![image](https://github.com/user-attachments/assets/4c870f3f-2891-48c3-83b6-5a7dfa1ebb6e)

![image](https://github.com/user-attachments/assets/8c61c557-5192-47fb-85ea-b99becea54b8)

5) Se configuran los routers para notificar las redes conectadas directamente al router y leer las bases de datos de estado de enlace (LSDB) en cada uno de los routers.

 ![image](https://github.com/user-attachments/assets/cc3b1d4e-145b-4ed3-8a9e-59ad08c11a06)

![image](https://github.com/user-attachments/assets/2d43959f-cf40-4279-9477-7f73eadfd499)

![image](https://github.com/user-attachments/assets/dd961bfa-a19c-474a-81c4-614857706a2a)

![image](https://github.com/user-attachments/assets/e5113e07-b503-4619-9cdd-f9a2de64ce64)

![image](https://github.com/user-attachments/assets/8261ac2e-a262-4277-b43b-40f6edfc05b2)

![image](https://github.com/user-attachments/assets/979a51d7-8a62-4623-9748-cd70c8f86aac)

Mediante el comando show ipi ospf database se muestran las bases de datos de estado de enlace 

![image](https://github.com/user-attachments/assets/68c1d1e4-9f4a-46e5-b335-681887c1c3da)

![image](https://github.com/user-attachments/assets/f663f785-5d3e-47c7-b148-5b11e0fb2cb0)

![image](https://github.com/user-attachments/assets/61eac3a8-ee4e-478a-95a1-fc99ebea80c4)

![image](https://github.com/user-attachments/assets/978ca1d4-e43d-4e2a-a4db-0fe201f2b051)

![image](https://github.com/user-attachments/assets/226bfa21-35b3-42db-b2ba-61132dbad577)

6) Se definen las áreas de OSPF de la siguiente manera: R0 y R2 están en el área A, el resto de los routers estarán en el área B.
Asi quedan las entradas LSDB:  

![image](https://github.com/user-attachments/assets/366beb3f-677f-40a2-982a-ac1726e3e8a8)

![image](https://github.com/user-attachments/assets/e9966dca-6d03-4bbe-b23b-89295a9385ff)

![image](https://github.com/user-attachments/assets/7854ba5c-735e-4d43-b85e-b77fa14e3edb)

![image](https://github.com/user-attachments/assets/1400681a-93ae-4c8a-ac92-d0d7593028f9)

![image](https://github.com/user-attachments/assets/f398b499-fed4-4c7b-ade4-5cac0efd9166)

7) En el router R0 se consulta la información acerca de los vecinos R1 y R3 de OSPF mientras que en el router R0 se consulta la información sobre las operaciones del protocolo de enrutamiento.

![image](https://github.com/user-attachments/assets/4adfd573-f440-48c8-886e-62a063bb1350)

8) Posteriormente se configuró el costo de OSPF, el objetivo es observar cómo afecta el funcionamiento del protocolo.
b) Realizar pruebas entre los clientes de los diferentes routers utilizando traceroute antes y después de la modificación para verificar el funcionamiento.

Para esto se mide primero la ruta que toma un paquete desde la PC0 mediante el comando tracert o traceroute desde un router
Desde PC0 a PC3

![image](https://github.com/user-attachments/assets/00b8f235-9413-4cb8-b9b8-de135b832d18)

Se puede ver que el camino que recorre es de R0->R1, luego R1->R3. Se aumenta el costo de R0->R1, sabiendo que como es una conexion serial el costo predeterminado es 64, lo cual implica que se lleva a más del doble.

![image](https://github.com/user-attachments/assets/78a04787-864c-4b6c-8db7-d9e58bdf7b45)

Ahora se verifica si esto afecto el camino que recorre un paquete desde PC0.

![image](https://github.com/user-attachments/assets/fc1118d1-99cd-4469-a07f-7ae63eaff89d)

Se observa que ya no sigue el camino R0->R1 sino que hace R0->R2->R1 por el aumento del costo entre R0-R1.

9) Se configura una dirección de loopback en R1 para simular un enlace a un proveedor de servicios de Internet (ISP).

![image](https://github.com/user-attachments/assets/4e4b7649-12cc-4b85-b167-854300670150)

 b) Del mismo modo se configura una ruta estática predeterminada en el router R1 y se incluye la ruta estática predeterminada en las actualizaciones de OSPF enviadas desde el router R1

![image](https://github.com/user-attachments/assets/dc23e436-62e3-4ddc-8364-59248a738308)

10) Se se cae una interfaz del router R1 (R1 - R2, R1 - R0, R1 - S1) sucede lo que se muestra a continuación

Análisis por interfaz
 Si se cae R1 – R2

Si R2 no tiene otra conexión hacia el backbone o hacia otras redes, pierde conectividad externa.

OSPF actualiza su LSDB (Link State Database) y notifica a los demás routers.

Las rutas que usaban esa interfaz se recalcularán usando Dijkstra.

Si se cae R1 – R0

Lo mismo: R0 pierde conexión directa con R1.

Si tiene otra vía (por ejemplo, R0 → R2 → R1), se mantiene el tráfico, solo cambia la ruta.

Si no hay otra ruta, R0 pierde conexión con redes que estaban accesibles solo por R1 (por ejemplo, al ISP).

 Si se cae R1 – Switch S1

Las PCs o dispositivos conectados a S1 pierden acceso completo a la red, porque ya no pueden comunicarse con el router.

No afecta la topología OSPF, pero sí impacta a los usuarios finales.

11) El RIB es una tabla de enrutamiento lógica que contiene todas las rutas conocidas (de OSPF, RIP, estáticas, etc.) mientras que el FIB es una tabla de reenvío real utilizada por el router que contiene solo las rutas activas seleccionadas por el RIB.
Para poder visualizar la tabla RIB ejecutamos show ip route. Esto muestra todas	las rutas que el router aprendió, sus orígenes (O = OSPF, C = conectada, S = estática, etc.) y métricas.

![image](https://github.com/user-attachments/assets/c323c211-1649-4083-8fdb-f7600e7b83b5)
