import threading

from pymodbus.client.sync import ModbusTcpClient
import math
import time
import urx


class URModbus():
    def __init__(self, host="10.0.0.2", port=502):
        self.client = ModbusTcpClient(host=host, port=port)
        tryes = 10
        result = self.client.connect()
        while (not self.client.connect()):
            tryes -=1
            if tryes<=0:
                raise RuntimeError('Cant connect to Robot')
        result  = self.client.read_holding_registers(1,1)

    def set_digital_out(self, output, val):
        mask = int(math.pow(2, output))

        if val in (True, 1):
            adr = 2
        else:
            adr = 3

        result = self.client.write_register(adr, mask)
        # result = self.client.write_register(adr, mask)
        # time.sleep(0.1)


def infinite_send_modbus(host):
    urmodbus = URModbus(host)
    val = 1
    while 1:
        val = val ^ 1
        start = time.time()
        urmodbus.set_digital_out(5, val)
        print("dur = {}".format(time.time()-start))
        time.sleep(20)


def do_traj(host):
    rob = urx.Robot(host, use_rt=False)
    p1 = [0.09683299700426644, 0.1407934174659861, 0.26595562107141757, -1.7168944823556898, -2.0791661473639866, -0.15474323652877797]
    p2 = [0.07936390024034601, 0.09915904856116421, 0.16050588819904205, -1.84860606414923, -2.0837108399869377, 0.30295420309772103]
    while 1:
        rob.movel(p1, acc=0.2, vel=0.2)
        rob.movel(p2, acc=0.2, vel=0.2)


if __name__ == '__main__':
    host = "10.0.0.2"

    threading.Thread(target=do_traj, args=(host,)).start()
    threading.Thread(target=infinite_send_modbus, args=(host,)).start()



