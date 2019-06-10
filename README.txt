# WSN_Mesh_ZigBee

## Introducción
El presente proyecto contiene el código, tanto del nodo coordinador de una red de topología en malla, como el de los nodos router de la red.
La finalidad de este proyecto es proponer una solución al problema de las redes de sensores inalámbricas, usando para ello el protocolo de comunicación Zigbee, buscando así la ventaja en cuanto a consumo de potencia con respecto a sus competidores más usados para este tipo de proyectos, e implementando dicha solución en forma de red mallada, lo que proporciona mayor tolerancia a fallos en la comunicación.
Hoy día, se suelen proponer este tipo de soluciones basadas en el concepto de IoT (en inglés, _Internet of Things_) o Internet de las cosas, para casos de aplicación práctica. Un ejemplo de ello podría ser el conocido como Smart Cities o Ciudades Inteligentes, o en concepto de apoyo en operaciones de rescate.
Este tipo de solución permite obtener información en casos en los que es necesaria la cercanía al fenómeno observado, la persistencia en el tiempo, o ambas.

## Área de desarrollo
El presente proyecto ha sido llevado a cabo como parte de un Trabajo de Fin de Estudios desarrollado por Francisco José Lara, y bajo la tutorización del departamento de Ingeniería de Sistemas y Automática, en la Escuela de Ingenierías Industriales de la Universidad de Málaga.

## Elementos constituyentes
Se trata de un proyecto desarrollado tanto con software como hardware libre, usando prácticamente en su totalidad en lenguaje Python, y dejando un pequeño espacio para el código Arduino.

**Hardware:** Para el desarrollo de cada uno de los módulos se propone el uso de:
* Raspberry Pi 3 Model B
* Raspberry Pi B Meet Arduino Shield DFR0327
* Módulo RF XBee Pro S2
* Sensores

**Software:** En la realización del proyecto se emplea el lenguaje de programación Python para el desarrollo del código de los nodos de la red, y el lenguaje Arduino para la recogida de datos de los sensores, así como MySQL, como gestor de bases de datos para el almacenamiento de dichos datos y el software XCTU de Digi International para la configuración de los módulos de radio frecuencia Zigbee. Todo ello a través del sistema operativo Raspbian, cargado sobre el hardware Raspberry Pi.
* IDE Python
* IDE Arduino
* PyMySQL
* XCTU Digi
* Raspbian OS

**Bibliografía**
* [GitHub - Python](https://github.com/digidotcom)	

* [IoT Internet de las Cosas](https://es.wikipedia.org/wiki/Internet_de_las_cosas)	

* [Smart Cities](https://books.google.es/books?hl=es&lr=lang_es&id=TdB3DwAAQBAJ&oi=fnd&pg=PA20&dq=iot+smart+cities&ots=fRARBbCaqX&sig=G3j6ifXYBNCnmsNmVhVUsBjDFFQ#v=onepage&q&f=false)	

* [DFRobot](https://wiki.dfrobot.com/Arduino_Shield_for_Raspberry_Pi_2B_and_3B_SKU_DFR0327)	

* [Arduino](https://aprendiendoarduino.wordpress.com/2016/11/16/zigbeexbee/)	
