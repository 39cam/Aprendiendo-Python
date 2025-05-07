import socket

# Se define la misma ip y puerto del servidor
HOST = '192.168.1.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se crea el socket
cliente.connect((HOST, PORT)) # Se realiza la conexión enviando los datos respectivos

cliente.sendall("Hola, servidor".encode()) # Se envía el mensaje codificado
respuesta = cliente.recv(1024) # Se recibe la respuesta con capacidad de 1KB
print(f"Respuesta del servidor: {respuesta.decode()}")

cliente.close()
