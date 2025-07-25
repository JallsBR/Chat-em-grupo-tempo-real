# Chat em grupo (realtime)

Exercício prático Pythonando para a criação de um chat em grupo em tempo real utilizando sockets e interface gráfica simples com Tkinter.

Tecnologias utilizadas

    Python 3

    Sockets (módulo socket) para comunicação em tempo real

    Tkinter para interface gráfica local

- Objetivos do projeto

01. Praticar uso de sockets TCP em Python
02. Criar uma interface gráfica básica para interação entre os usuários
03. Permitir vários clientes conectados simultaneamente a um servidor local
04. Exercitar conceitos de concorrência (threads) para gerenciar múltiplas conexões sem travar a interface

- Como executar localmente

1️⃣ Clone este repositório:

git clone https://github.com/JallsBR/Chat-em-grupo-tempo-real.git


2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
-  Windows
venv\Scripts\activate
-  Linux/Mac
source venv/bin/activate

3️⃣ Execute o servidor:

python servidor.py

4️⃣ Em outro terminal ou máquina, execute o cliente:

python cliente.py

OBS: Você pode abrir múltiplas instâncias do cliente.py para simular vários usuários no chat.