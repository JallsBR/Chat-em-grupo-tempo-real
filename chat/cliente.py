import socket
import threading
from tkinter import*
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 27459
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        login = Tk()
        login.withdraw()
        
        self.janela_carregada = False
        self.ativo = True
        
        self.nome = simpledialog.askstring(b"Nome", "Digite seu nome:", parent=login)
        self.sala = simpledialog.askstring(b"Sala", "Digite o nome da sala:", parent=login)
        thread = threading.Thread(target=self.conecta)
        thread.start()
        self.janela()

    def janela(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title(f"Chat - {self.nome} - {self.sala}")
        
        self.caixa_texto = Text(self.root)        
        self.caixa_texto.place(relx=0.05, rely=0.01, width=700, height=600)
        
        self.envia_mensagem = Entry(self.root)
        self.envia_mensagem.place(relx=0.05, rely=0.8, width=600, height=20)
        
        self.btn_enviar = Button(self.root, text="Enviar", command=self.enviarMensagem)
        self.btn_enviar.place(relx=0.8, rely=0.8, width=100, height=20)
        self.root.protocol("WM_DELETE_WINDOW", self.fechar)



        
        self.root.mainloop()
        
    def fechar(self):
        self.root.destroy()
        self.client.close()
        
    def conecta(self):
        while True:
            recebido = self.client.recv(1024)
            if recebido == b"Nome":
                self.client.send(self.nome.encode())
                self.client.send(self.sala.encode())
            else:
                try:
                    self.caixa_texto.insert('end', recebido.decode())
                except:
                    pass
    def enviarMensagem(self): 
        mensagem = self.envia_mensagem.get()
        self.client.send(mensagem.encode())        
        
        
chat = Chat()        
        