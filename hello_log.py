import socket
import threading
from time import sleep

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
log_port = 50000  # The same port as used by the server


def log_test(client):
    while True:
        try:
            data = client.recv(4096)
            print(data.decode())
        except socket.error:
            print("connection is lost")
            client.close()
            return


def server(soc):
    while True:
        client, addr = soc.accept()
        print('Got connection from', addr)
        client.settimeout(10)
        log_test_thread = threading.Thread(target=log_test, args=(client,))
        log_test_thread.setDaemon(True)
        log_test_thread.start()


log_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log_server.bind(('10.0.0.4', log_port))
log_server.listen(5)
print('Server started!')
print('Waiting for clients...')

threading.Thread(target=server, args=(log_server,)).start()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


client.send("socket_open(\"10.0.0.4\", 50000, \"socket_log\")\n".encode())




while True:
    client.send(("socket_send_string(\"hello_log\", \"socket_log\"\n").encode())
    sleep(1)
