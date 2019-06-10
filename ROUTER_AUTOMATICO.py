# Codigo desarrollado por Francisco Jose Lara.
# NODO-ROUTER 

#Librerias
import serial, time,sys
from digi.xbee.devices import XBeeDevice,RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress, XBee16BitAddress
from digi.xbee.packets.common import TransmitPacket
from digi.xbee.packets.raw import TX64Packet
from digi.xbee.util import utils
import struct

#Inicio XBee Device
device = XBeeDevice("/dev/serial0", 9600)
device.open()
print("-- Dispositivo  abierto --")

while 1:
    #Leer
    mens=None
    print("\nEsperando peticion de datos...\n")
    while mens==None:
        # Recivo de coordinador
        mens = device.read_data()                
        #print(".")
        time.sleep(0.5)
    # Decodifico mensaje
    com =mens.data.decode("utf8")                
    print ("Peticion decodificada: ",com,"\n")
    if com=='Fin':
        break

    #Recogida de datos de Shield Arduino
    arduino=serial.Serial('/dev/ttyACM0',9600)
    x=0
    while x==0:
            while arduino.inWaiting()>0:
                texto = arduino.readline()
                texto = texto.decode("utf8")
                texto = texto[:-2]
                print("\nDatos del sensor: ",texto,"\n")
                # Con 21 para "TEMP-xx:SND-xx:LUZ-xx"
                if len(texto)==21:
                    x=1
    arduino.close()

    # Datos recogidos
    time.sleep(1)
    data="Recogidos"
    data=data.encode("utf8")
    coord=RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040C53D49"))
    device.send_data(coord,data)

    #Leer
    mens=None
    print("\nEsperando mi turno...\n")
    while mens==None:
        # Recivo de coordinador
        mens = device.read_data_from(coord)       
        time.sleep(0.5)

    print("\nEnviando datos solicitados\n")
    data=texto.encode("utf8")
    # Envio a coordinador
    device.send_data(coord,data)
    print("Datos enviados con exito!\n")

print("Cerrando dispositivo de comunicacion...\n")
#Cierro conexion
device.close()
print("Fin de la comunicacion.\n")


