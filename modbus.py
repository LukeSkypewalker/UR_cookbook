import threading

from pymodbus.client.sync import ModbusTcpClient
import math
import time


class URModbus():
    REG_DIG_OUT = 1
    REG_SET_PIN = 2
    REG_CLR_PIN = 3

    def __init__(self, host="10.0.0.2", port=502):
        self.client = ModbusTcpClient(host=host, port=port)
        tries = 10
        while not self.client.connect():
            tries -= 1
            if tries <= 0:
                raise RuntimeError('Cant connect to Robot')

        # every n seconds read some register in parallel thread
        self.keep_alive(5)

    def keep_alive(self, timeout):
        threading.Thread(target=self.read_with_pause, args=(timeout,)).start()

    def read_with_pause(self, timeout):
        try:
            while 1:
                self.get_digital_out(1)
                time.sleep(timeout)
        except Exception as e:
            print(e)
            self.read_with_pause(timeout)

    def get_digital_out(self, pin):
        mask = self.bitmask(pin)
        result = self.client.read_holding_registers(self.REG_DIG_OUT, 1)
        return result.registers[0] & mask
        # print(result)

    def set_digital_out(self, pin, val):
        mask = self.bitmask(pin)

        if val in (True, 1):
            adr = self.REG_SET_PIN
        else:
            adr = self.REG_CLR_PIN

        result = self.client.write_register(adr, mask)
        time.sleep(0.03)

    def bitmask(self, val):
        return int(2 ** val)
