import socket

# Andrés Camilo Ocampo Castillo - 20222578098

# Dirección IP del servidor (la que voy a definir en el servidor)
HOST = '192.168.1.1' # La ip debe concordar con la del cliente hasta el apartado de red, es decir en este caso los 3 primeros valores, cambia el valor final

PORT = 5000 # Selección de un puerto aleatorio

# Creando el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Af_inet: dirección ipv4, sock_stream: protocolo tcp
servidor.bind((HOST, PORT)) # La función bind nos permite asignar tanto un host (la ip q se asignó al server) como un puerto
servidor.listen(1) # Solo recibiendo una señal

print("Esperando conexión...")
conn, addr = servidor.accept() # En el momento en que reciba conexión asigna conn a la conexión respectiva y la ip del cliente
print(f"Conectado por: {addr}")

while True:
    datos = conn.recv(1024) # El parametro es la cantidad de bytes q se están recibiendo (en este caso 1KB), recv es la función para recibir
    if not datos: # En dado caso de que no haya un mensaje recibido entonces se cierra el flujo
        break
    print(f"Mensaje recibido: {datos.decode()}") # Se imprime en pantalla el mensaje que envió el cliente decodificando con .decode()
    conn.sendall("Mensaje recibido".encode()) # Se envía el mensaje codificado al cliente para confirmar la conexión

conn.close() # Se cierra la conexión

# Andrés Camilo Ocampo Castillo - 20222578098