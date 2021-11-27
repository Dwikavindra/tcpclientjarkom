import socket
import threading

nickname = input("Choose a nickname: ")
HOST = '34.101.88.159'
PORT = 3389
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.AF_INET itu tcpnya
client.connect((HOST,PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'ready':
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("The server closed")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()