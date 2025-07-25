import socket
import threading

HOST = '127.0.0.1'
PORT = 27459

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala,mensagem):
    for msn in salas[sala]:
        if isinstance(msn, str):
            msn = msn.encode()
        msn.send(mensagem.encode())
        
def enviarMensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024).decode()
        mensagem = f"{nome}: {mensagem}\n"
        broadcast(sala, mensagem)
        
while True:
    client, address = server.accept()
    client.send(b"Nome")
    nome = client.recv(1024).decode()
    sala = client.recv(1024).decode()    
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f" --> Salas ativas: {salas}.\n  -> {nome} entrou na sala {sala}. INFO: {address}\n")
    broadcast(sala, f"{nome} entrou na sala {sala}.\n")
    tread = threading.Thread(target=enviarMensagem, args=(nome, sala, client))
    tread.start()
    

