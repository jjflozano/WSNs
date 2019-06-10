# Codigo desarrollado por Francisco Jose Lara.
# NODO-COORDINADOR

# Librerias
import serial, time,sys,datetime
from xbee import XBee,ZigBee
from digi.xbee.models.address import XBee64BitAddress, XBee16BitAddress
from digi.xbee.devices import ZigBeeDevice,XBeeDevice,RemoteXBeeDevice,RemoteZigBeeDevice
from digi.xbee.serial import XBeeSerialPort
from digi.xbee.packets.raw import TX64Packet, TX16Packet,RX64Packet, RX16Packet
from digi.xbee.models.message import XBeeMessage
import pymysql
remoto = {}

#Inicio XBee Device
device = XBeeDevice("/dev/serial0", 9600)
device.open()

#MAC de mi dispositivo
print("MAC de mi dispositivo: ")
print (device.get_64bit_addr(),"\n")

#Buscar redes
xnet = device.get_network() 
print ("Red encontrada:")
print (xnet)
xnet.start_discovery_process()
while xnet.is_discovery_running():
    time.sleep(0.5)
    
#Busca dispositivos de esa red
devices = xnet.get_devices() 
print ("Dispositivos en esa red: 0,1,2...")
print (devices, "\n")
# Vision de todos los nodos de la red
for i in range(len(devices)):         
    remoto[i]=xnet.add_remote(devices[i])
    x64addr=remoto[i].get_64bit_addr()
    ID=remoto[i].get_node_id()
    print(i," -> ",x64addr," ",ID,"\n")
    
x=0
while x<2:
    # Peticion a sensores
    data='Sensores'
    data=data.encode("utf8")
    print ("Enviando peticion...")
    # Envio en modo broadcast
    device.send_data_broadcast(data,0)  
    print ("Peticion enviada")
    time.sleep(1)
    j=0
    for j in range(i+1):
        # Datos recogidos desde los sensores
        print ("Esperando a dispositivo ",j,"...")
        mens=None
        while mens==None:
            mens = device.read_data_from(remoto[j])
        data =mens.data.decode("utf8")
        time.sleep(0.5)
        print("\nDatos ",data)
        
        # Asignacion de turno
        print("Recolectando esos datos...")
        data='Tu turno'
        data=data.encode("utf8")
        device.send_data(remoto[j],data)
        
        #Leer
        mens=None
        while mens==None:
            # Recivo de router
            mens = device.read_data_from(remoto[j])  
        time.sleep(1)
        
        # Inicio Base de Datos
        db = pymysql.connect(host="localhost", # host, usually localhost
                     user="patrick",           # username
                     passwd="patrick",         # password
                     db="mydb")                # data base
        cur = db.cursor()
        
        tim= mens.timestamp
        fecha=datetime.datetime.fromtimestamp(tim).strftime('%Y-%m-%d %H:%M:%S')
        print("Fecha y hora de recepcion: ",fecha)
        
        rem=mens.remote_device
        print ("Lo ha enviado: ", rem)

        data =mens.data.decode("utf8")
        dataDetach = data.split(':')
        k=0
        for k in range(len(dataDetach)):
            print("Datos decodificados: \n",dataDetach[k],"\n")
            query="INSERT INTO Tabla (Emisor,Tiempo,Dato) VALUES ('%s','%s','%s')" % (rem,fecha,dataDetach[k])
            '''print (query)'''
            print ("\nSubido a la base de datos con exito\n")
            # Vuelco en base de datos
            cur.execute(query)
            db.commit()
    stop='N'
    stop=input("Parar ejecucion...( s )? ")
    if stop=='s':
        x=5
    time.sleep(5)
    
data='Fin'
data=data.encode("utf8")
print ("Enviando señal de finalizacion...")
# Envio en modo broadcast
device.send_data_broadcast(data,0)  
print ("Fin del programa")

#Cierro conexion
device.close()

