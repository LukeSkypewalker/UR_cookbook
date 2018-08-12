import socket
import threading
import queue
from asyncio import sleep

import numpy as np
from numpy import linalg as linal
import networkx as nx
import urx
import modbus


def dist(A,B):
    vector = np.subtract(A[:3], B[:3])
    dist = linal.norm(vector)
    return dist


def add_edge(e1, e2):
    G.add_edge(e1, e2, weight=dist(e1, e2))


def find_closest_graph_point():
    current_point = rob.getl()
    closest_point = None
    closest_dist = 1000
    for node_point in G.nodes:
        dist_to_node = dist(current_point, node_point)
        if dist_to_node < closest_dist:
            closest_dist = dist_to_node
            closest_point = node_point
    return closest_point


def takе_money_from_pocket(pocket):
    path = nx.dijkstra_path(G, find_closest_graph_point(), pocket)
    print('pocket', path)
    rob.set_digital_out(1,False)
    rob.movels(path, acc=0.3, vel=0.1, radius=0.02)
    rob.set_digital_out(1,True)


def put_money_to_doors_packer():
    path = nx.dijkstra_path(G, find_closest_graph_point(), bottom_right)
    print('doors',path)
    threading.Thread(target=io_helper_thread, args=(bottom_mid, 6, True)).start()
    rob.movels(path, acc=0.3, vel=0.1, radius=0.02)


def io_helper_thread(io_point, io_port, io_val):
    epsilon = 0.005
    urmodbus.set_digital_out(io_port, not io_val)
    while True:
        if dist(rob.getl(), io_point) < epsilon:
            urmodbus.set_digital_out(io_port, io_val)
            return


def sense_force():
    F = rob.get_tcp_force()
    force = linal.norm(F)
    return force


def force_sensing():
    while True:
        force = sense_force()
        if force > 100:
            print(force)
            s.send(("stop\n").encode())


top_left = (0.1385712124925622, 0.011636543397915838, 0.04154186729581166, 1.6418626722172847, 0.09084535686200002, 0.09638235412602147)
top_right = (-0.08335407357610965, 0.002380275817666963, 0.04098004351565569, 1.5785973273478597, 0.0619146060894506, 0.04607632817790494)
middle_left = (0.13224846396039025, 0.12662553455733527, 0.04246070617888544, 1.6690120889031714, 0.03927775501125644, 0.04311094155117962)
middle_right = (-0.06833056456278366, 0.11545660067221411, 0.06772123781724937, 1.5331826245776523, 0.07362412262225689, 0.10506065060232621)
bottom_left = (0.14703163805242933, 0.12105297090236018, -0.028435767924547634, 1.593193283603764, 0.07557609939939768, 0.08203643035759282)
bottom_mid = (0.045732415260817116, 0.12377154691217895, -0.05642223856397642, 1.6562918746337372, 0.0881824773362143, 0.054139008724028104)
bottom_right = (-0.05682267667082395, 0.11817956508611568, -0.05438052803286208, 1.647961907492653, 0.05799813952987592, -0.015553741975745548)
side_top = (0.10513635590522341, 0.010425492915599043, 0.061232147357939415, 1.2747539121053997, -1.152338086670774, -1.1404847833127558)
side_bottom_mid = (0.09034984206608578, 0.002978369660784703, -0.06242151328692695, 1.2794475247155692, -1.1572609875282505, -1.140752256157648)
side_front_bottom_transition = (0.14832936517922996, 0.1324069539329083, -0.008314803132204078, 1.5152549302098637, -0.38448962259284947, -0.3941700894480176)
side_bottom_corner = (0.0727507484453784, 0.15678392808978373, -0.034084718592373664, 1.2952482154542435, -1.1371045191059936, -1.1378825796039966)

G = nx.Graph()

add_edge(side_bottom_mid, side_top)
add_edge(side_top, top_left)
add_edge(top_left, top_right)
add_edge(top_left, middle_left)
add_edge(top_left, middle_right)
add_edge(top_right, middle_left)
add_edge(top_right, middle_right)
add_edge(middle_left, bottom_left)
add_edge(middle_left, bottom_mid)
add_edge(middle_left, bottom_right)
add_edge(middle_right, bottom_left)
add_edge(middle_right, bottom_mid)
add_edge(middle_right, bottom_right)
add_edge(bottom_left, bottom_mid)
add_edge(bottom_mid, bottom_right)
add_edge(bottom_left, bottom_right)
add_edge(side_front_bottom_transition, side_bottom_mid)
add_edge(side_front_bottom_transition, bottom_left)
add_edge(side_front_bottom_transition, side_bottom_corner)
add_edge(side_bottom_mid, side_bottom_corner)



host = "10.0.0.2"
rob = urx.Robot(host, use_rt=True)
urmodbus = modbus.URModbus(host)


# Dashboard
PORT = 29999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, PORT))


tasks_queue = queue.Queue()
tasks_queue.put(lambda: takе_money_from_pocket(side_bottom_mid),)
tasks_queue.put(lambda: put_money_to_doors_packer())
print(tasks_queue)
print(tasks_queue.qsize())

threading.Thread(target=force_sensing).start()

while tasks_queue.not_empty:
    try:
        task = tasks_queue.get()
        task()
    except urx.RobotException as ex:
        print(ex)
        sleep(3)
        tasks_queue.put(task)
        print (tasks_queue)
