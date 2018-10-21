# Dashboard examples
# CB-series: https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/dashboard-server-port-29999-15690/
# E-series:  https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/dashboard-server-e-series-port-29999-42728/
import socket

HOST = "10.0.0.2"
PORT = 29999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cmd = "unlock protective stop\n"
# cmd = "stop\n"
# cmd = "play\n"
# cmd = "pause\n"

s.send(cmd.encode())
