#socket.sendfile() disponible desde Python 3.3
import socket
import binascii 
import os 
import logging

SERVER_ADDR = '' #MARP Direccion para el servidor local.
SERVER_PORT = 9800 #MARP Puerto 9800 por defecto
BUFFER_SIZE = 64 * 1024 # MARP 64 KB para buffer de transferencia de archivos

server_socket = socket.socket()
server_socket.bind((SERVER_ADDR, SERVER_PORT))
server_socket.listen(10) #MARP 1 conexion activa y 9 en cola
server_socket.listen(100) #MARP 1 conexion activa y 9 en cola

listening=True #MARP variables globales = 1
listener=True
listen=True

try:
    while True: #MARP En un bucle infinito esperar la conexion para saber si esxiste solicutd de conexion y archivo a enviar.
        print("\nEsperando conexion remota...\n")
        conn, addr = server_socket.accept()
        print('Conexion establecida ', addr) #MARP Se efctua la conexion local.

        if (listening==binascii.unhexlify("01")):#MARP Probar si existe un archivo dentro del buffer.
            logging.basicConfig(
            level = logging.DEBUG, 
            format = '%(message)s'
            )
            logging.info('Comenzando grabacion')
            os.system('arecord -d 10 -f U8 -r 8000 201444696_server.wav')

            logging.info('Grabacion finalizada, inicia reproduccion')
            os.system('aplay 201444696_server.wav')

        elif (listener==binascii.unhexlify("03")):

            print('Enviando archivo de audio desde el servidor...')
            with open('201444696_server.wav', 'rb') as f: #MARPSe abre el archivo de audio.wav a enviar en BINARIO
            conn.sendfile(f, 0)
            f.close()
            conn.close()
            print("\n\nArchivo enviado a: ", addr)

        elif (listen==binascii.unhexlify("02")): #MARP Cerrar la conexion establecida en el servidor
            print("Efectuar desconexion")
            server_socket.close()
        
        else:
            pass
"""
finally:
    print("Cerrando el servidor...")
    server_socket.close()
"""





