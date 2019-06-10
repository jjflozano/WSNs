# WSN_Mesh_ZigBee

## Introducci�n
El presente proyecto contiene el c�digo, tanto del nodo coordinador de una red de topolog�a en malla, como el de los nodos router de la red.
La finalidad de este proyecto es proponer una soluci�n al problema de las redes de sensores inal�mbricas, usando para ello el protocolo de comunicaci�n Zigbee, buscando as� la ventaja en cuanto a consumo de potencia con respecto a sus competidores m�s usados para este tipo de proyectos, e implementando dicha soluci�n en forma de red mallada, lo que proporciona mayor tolerancia a fallos en la comunicaci�n.
Hoy d�a, se suelen proponer este tipo de soluciones basadas en el concepto de IoT (en ingl�s, _Internet of Things_) o Internet de las cosas, para casos de aplicaci�n pr�ctica. Un ejemplo de ello podr�a ser el conocido como Smart Cities o Ciudades Inteligentes, o en concepto de apoyo en operaciones de rescate.
Este tipo de soluci�n permite obtener informaci�n en casos en los que es necesaria la cercan�a al fen�meno observado, la persistencia en el tiempo, o ambas.

## �rea de desarrollo
El presente proyecto ha sido llevado a cabo como parte de un Trabajo de Fin de Estudios desarrollado por Francisco Jos� Lara, y bajo la tutorizaci�n del departamento de Ingenier�a de Sistemas y Autom�tica, en la Escuela de Ingenier�as Industriales de la Universidad de M�laga.

## Elementos constituyentes
Se trata de un proyecto desarrollado tanto con software como hardware libre, usando pr�cticamente en su totalidad en lenguaje Python, y dejando un peque�o espacio para el c�digo Arduino.

**Hardware:** Para el desarrollo de cada uno de los m�dulos se propone el uso de:
* Raspberry Pi 3 Model B
* Raspberry Pi B Meet Arduino Shield DFR0327
* M�dulo RF XBee Pro S2
* Sensores

**Software:** En la realizaci�n del proyecto se emplea el lenguaje de programaci�n Python para el desarrollo del c�digo de los nodos de la red, y el lenguaje Arduino para la recogida de datos de los sensores, as� como MySQL, como gestor de bases de datos para el almacenamiento de dichos datos y el software XCTU de Digi International para la configuraci�n de los m�dulos de radio frecuencia Zigbee. Todo ello a trav�s del sistema operativo Raspbian, cargado sobre el hardware Raspberry Pi.
* IDE Python
* IDE Arduino
* PyMySQL
* XCTU Digi
* Raspbian OS

**Bibliograf�a**
* [GitHub - Python](https://github.com/digidotcom)	

* [IoT Internet de las Cosas](https://es.wikipedia.org/wiki/Internet_de_las_cosas)	

* [Smart Cities](https://books.google.es/books?hl=es&lr=lang_es&id=TdB3DwAAQBAJ&oi=fnd&pg=PA20&dq=iot+smart+cities&ots=fRARBbCaqX&sig=G3j6ifXYBNCnmsNmVhVUsBjDFFQ#v=onepage&q&f=false)	

* [DFRobot](https://wiki.dfrobot.com/Arduino_Shield_for_Raspberry_Pi_2B_and_3B_SKU_DFR0327)	

* [Arduino](https://aprendiendoarduino.wordpress.com/2016/11/16/zigbeexbee/)	
