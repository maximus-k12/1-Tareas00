"""*****************************************Envio de un archivo de audio desde un servidor *******************************************"""
import socket
import binascii 
import os 
import logging

listening=0 #MARP variables globales, inicializada en 0 para que el cliente comience a hacer el conteo.
speaking=0 #MARP inicializada en 0 para que el cliente comience a hacer el conteo.
talking=0 #MARP Para finalizar la conexion con el cliente si ya se envio el audio .wav


SERVER_ADDR = '' #MARP Direccion para el servidor local.
SERVER_PORT = 9800 #MARP Puerto 9800 por defecto
BUFFER_SIZE = 64 * 1024 # MARP 64 KB para buffer de transferencia de archivos

server_socket = socket.socket()
server_socket.bind((SERVER_ADDR, SERVER_PORT))
server_socket.listen(10) #MARP 1 conexion activa y 9 en cola
server_socket.listen(100) #MARP 1 conexion activa y 9 en cola


try:
    while True: #MARP En un bucle infinito esperar la conexion para saber si esxiste solicutd de conexion y archivo a enviar.
        print("\nEsperando conexion remota...\n")
        conn, addr = server_socket.accept()
        print('Conexion establecida ', addr) #MARP Se efctua la conexion local.

        if (listening==binascii.unhexlify("01")):#MARP Probar si existe un archivo dentro del buffer.
            logging.basicConfig(
            level = logging.DEBUG,  
            format = '%(message)s' #MARP Que el formato sea un mensaje a enviar
            )
            logging.info('Comenzando grabacion') #MARP Mostrar informacion de inicion como comenzando grabacion.
            os.system('arecord -d 10 -f U8 -r 8000 201444696_server.wav')  #MARP Formato y tamaño del archivo .wav 

            logging.info('Grabacion finalizada, inicia reproduccion') #MARP Mostrar que termino la grabacion del archivo.
            os.system('aplay 201444696_server.wav') #MARP Mostrar el audio que fue grabado.

        if (speaking==binascii.unhexlify("03")): # MARP Empezar a enviar el archivo de audio si el audio existe.

            print('Enviando archivo de audio desde el servidor...') #Mostrar el envio del archivo de audio.
            with open('201444696_server.wav', 'rb') as f: #MARPSe abre el archivo de audio.wav a enviar en BINARIO
                conn.sendfile(f, 0)                      #MARP ENviar el archivo en el bufer.            
                f.close()
            conn.close()                              #MARP Terminarl el envio del audio.
            print("\n\nArchivo enviado a: ", addr) #Mostrar el aarchivo enviado de audio.

        if (talking==binascii.unhexlify("02")): #MARP Cerrar la conexion establecida en el servidor
            print("Efectuar desconexion")
            server_socket.close()               #MARP Terminar la conexion del servidor con el cliente
"""
finally:
    print("Cerrando el servidor...")
    server_socket.close()
"""





