import socket
HOST = '127.0.0.1'
PORT = 27459

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)  # Recebe a mensagem "Sala"
if mensagem == b"Nome":
    print("Servidor solicitou o nome do usuário e da sala.")
    client.send(b"Oswaldo")
    client.send(b"Python")
    