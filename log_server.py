import socket
import threading
from time import sleep

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
log_port = 50000  # The same port as used by the server


def log_test(client):
    while True:
        try:
            data = client.recv(4096).decode("utf-8")
            print(data)
        except socket.error:
            print("connection is lost")
            client.close()
            return


log_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log_server.bind(('10.0.0.4', log_port))
log_server.listen(5)
print('Server started!')
print('Waiting for clients...')

client, addr = log_server.accept()  # Establish connection with client.
print('Got connection from', addr)
log_test_thread = threading.Thread(target=log_test, args=(client,))
log_test_thread.setDaemon(True)
log_test_thread.start()

while True:
    print("sleep")
    sleep(10)
