import threading

import urx



# def force_control(force):
# if rob.get_tcp_force() > force:



rob = urx.Robot("10.0.0.2", use_rt=True)
# threading.Thread(target=force_control(), args=(200,)).start()


while True:
    rob.movel([0.012889971473679554, 0.22536417168498468, 0.033527201044447424, -2.9461864926833323, -0.5407140101351142, 0.2002910487153246],acc=0.3, vel=0.2)
    rob.movel([-0.02998879918968457, 0.33407504308090175, 0.5651256537814562, -1.551643173633851, -0.36952898586425414, 0.362464706550764],acc=0.3, vel=0.2)
