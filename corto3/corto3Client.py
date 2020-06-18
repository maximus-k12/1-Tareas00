import socket
import binascii
import os 
import logging

SERVER_IP   = ''
SERVER_PORT = 9800
BUFFER_SIZE = 64
BUFFER_SIZE = 64 * 1024 #MARP Usar un ancho de buffer de 64 bits.
 
# MARP Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# MARP Conectar al puerto donde el servidor se encuentra a la escucha
server_address = (SERVER_IP, SERVER_PORT) #MARP Buscar direccion del puerto y el servidor.
print('Conectando a {} en el puerto {}'.format(*server_address)) #MARP Mostrar donde se esta efectuando la conexion.
sock.connect(server_address)
try:
    # MARP Enviar  un texto codificado EN BINARIO
    message = b'Archivo de audio'
    print('\n\nEnviando el audio  {!s}'.format(message)) #MARP Mostrar que se esta enviando un archivo
    sock.sendall(message) #Enviar utilizando "socket.sendall" 
    print("\n\n")
    # MARP Esperamos la respuesta del ping servidor
    bytesRecibidos = 0
    bytesEsperados = len(message)
    # MARP TCP envia por bloques de BUFFER_SIZE bytes
    while bytesRecibidos < bytesEsperados: 
        data = sock.recv(BUFFER_SIZE)
        bytesRecibidos += len(data)
        print('Recibido: {!s}'.format(data))
finally: 
    print('\n\nConexion finalizada con el servidor')
    sock.close()