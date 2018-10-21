import networkx as nx
import matplotlib.pyplot as plt
import urx
import numpy as np


acc = 1
vel = 0.1
rad = 0.01


def point_dist(A, B):
    vector = np.subtract(A[:3], B[:3])
    return np.linalg.norm(vector)


def pose_dist(A, B):
    # TODO math test
    vector = np.subtract(A, B)
    return np.linalg.norm(vector)


def add_edge(p1, p2, is_linear=True, acc=acc, vel=vel, radius=rad, io_port=None, io_val=None):
    G.add_edge(p1, p2, dist=point_dist(G.nodes[p1]['pose'], G.nodes[p2]['pose']),
               is_linear=is_linear, acc=acc, vel=vel, radius=radius, io_port=io_port, io_val=io_val)


def find_closest_graph_point():
    current_pose = rob.getl()
    closest_node = None
    closest_dist = 1000
    for node in G.nodes:
        print(node)
        dist_to_node = point_dist(current_pose, G.nodes[node]['pose'])
        print(dist_to_node)
        if dist_to_node < closest_dist:
            closest_dist = dist_to_node
            closest_node = node
        print(closest_node)
    return closest_node


def movexxx(node_id_list, wait=True, threshold=None):
    header = "def myProg():\n"
    end = "end\n"
    prog = header

    for idx, node_id in enumerate(node_id_list):

        if idx == 0:
            # skip first point, we will omit it from the path,
            # but now it is needed to find the edge
            continue

        prev_node_id = node_id_list[idx - 1]
        node = G.nodes[node_id]
        edge = G.edges[prev_node_id, node_id]

        command = 'movel' if edge['is_linear'] else 'movej'

        if 'joints' in node:
            prefix = ''
            pose = node['joints']
        else:
            prefix = 'p'
            pose = node['pose']

        if idx == (len(node_id_list) - 1):
            radius = 0
        else:
            radius = edge['radius']

        prog += rob._format_move(command, pose, edge['acc'], edge['vel'], radius, prefix) + "\n"

        if edge['io_port']:
            prog += 'set_digital_out(' + str(edge['io_port']) +',' + str(edge['io_val']) + ")\n"

    prog += end
    print('\n' + prog)
    #rob.send_program(prog)
    #if wait:
    #    rob._wait_for_move(target=node['pose'], threshold=threshold)
    #    return rob.getl()


rob = urx.Robot("10.0.0.2", use_rt=True)
rob.set_tcp((0, 0, 0.067, 1.57, 0, 0))


a = [-0.1066, 0.3251, 0.0857, -0.4662, 3.0152, -0.0539]
aj = [2.5172, -1.9524, -2.4193, -1.9736, -0.9298, -0.0446]
b = [-0.0858, 0.4113, 0.0863, -0.3439, 3.0724, -0.0046]
bj = [2.1936, -2.1627, -2.0025, -2.1274, -1.1707, -0.0446]
c = [-0.0393, 0.3693, 0.0877, -0.2868, 3.0768, -0.0079]
cj = [2.1509, -2.0364, -2.2728, -1.9852, -1.1761, -0.0446]
d = [-0.0412, 0.3401, 0.0842, -0.3749, 3.0392, -0.0768]
dj = [2.2094, -1.9588, -2.4040, -1.9853, -1.1761, -0.0446]
e = [0.0406, 0.4311, 0.0904, -0.1652, 3.1090, 0.0639]
ej = [2.0638, -2.1977, -1.9524, -2.0904, -1.1849, -0.0447]
f = [0.0117, 0.4215, 0.0891, -0.0886, 3.1018, 0.0292]
fj = [2.0062, -2.1657, -2.0063, -2.0922, -1.1929, -0.0447]
g = [0.0244, 0.4023, 0.0856, 0.0162, 3.0876, -0.0307]
gj = [1.9379, -2.1184, -2.0929, -2.0932, -1.1926, -0.0447]
h = [0.0136, 0.3503, 0.0885, -0.2811, 3.0754, -0.0283]
hj = [1.9447, -1.9870, -2.3525, -1.9673, -1.3783, -0.0446]
i = [0.0278, 0.4281, 0.0873, -0.0960, 3.0832, -0.0633]
ij = [1.8477, -2.1762, -1.9218, -2.2289, -1.3549, -0.0447]
j = [0.1037, 0.4544, 0.0897, 0.1936, 3.0805, -0.0910]
jj = [1.6603, -2.2691, -1.6944, -2.3762, -1.3544, -0.0447]
k = [0.0738, 0.4144, 0.0916, 0.0665, 3.0905, -0.0359]
kj = [1.7436, -2.1452, -1.9770, -2.1836, -1.3543, -0.0447]
l = [0.1140, 0.3629, 0.0864, 0.1334, 3.0833, -0.1147]
lj = [1.6236, -2.0489, -2.1619, -2.1451, -1.4295, -0.0447]
m = [0.0623, 0.3329, 0.0848, -0.1228, 3.0771, -0.1096]
mj = [1.7898, -1.9540, -2.3796, -2.0239, -1.4295, -0.0447]

G = nx.DiGraph()

G.add_node('a', pose=a, joints=aj)
G.add_node('b', pose=b)
G.add_node('c', pose=c)
G.add_node('d', pose=d)
G.add_node('e', pose=e, joints=ej)
G.add_node('f', pose=f)
G.add_node('g', pose=g)
G.add_node('h', pose=h, joints=hj)
G.add_node('i', pose=i, joints=ij)
G.add_node('j', pose=j, joints=jj)
G.add_node('k', pose=k, joints=kj)
G.add_node('l', pose=l, joints=lj)
G.add_node('m', pose=m, joints=mj)

add_edge('a', 'b', is_linear=True, acc=acc, vel=vel, radius=rad, io_port=5, io_val=True)
add_edge('a', 'c')
add_edge('a', 'd')
add_edge('b', 'a')
add_edge('b', 'e', vel=0.05)
add_edge('b', 'c')
add_edge('c', 'd')
add_edge('c', 'f')
add_edge('c', 'g')
add_edge('c', 'h')
add_edge('d', 'a')
add_edge('e', 'b')
add_edge('e', 'i', io_port=5, io_val=False)
add_edge('f', 'e')
add_edge('g', 'f')
add_edge('g', 'l')
add_edge('h', 'd')
add_edge('i', 'e')
add_edge('i', 'g')
add_edge('i', 'j')
add_edge('i', 'k')
add_edge('j', 'i')
add_edge('j', 'l')
add_edge('k', 'l')
add_edge('l', 'h')
add_edge('l', 'g')
add_edge('l', 'k')
add_edge('l', 'j')
add_edge('m', 'l')


path = nx.dijkstra_path(G, 'a', 'j')

print('path', path)
movexxx(path)

nx.draw(G, with_labels=True)
plt.show()
