import urx


def movejls(self, pose_list, acc=0.01, vel=0.01, radius=0.01, wait=True, threshold=None):
    header = "def myProg():\n"
    end = "end\n"
    prog = header
    for idx, item in enumerate(pose_list):
        if idx == (len(pose_list) - 1):
            radius = 0
        pose = item[0]
        type_of_pose = item[1]
        if type_of_pose:
            prefix = 'p'
        else:
            prefix = ''

        prog += self._format_move("movel", pose, acc, vel, radius, prefix) + "\n"
    prog += end
    print(prog)
    self.send_program(prog)
    if wait:
        self._wait_for_move(target=pose_list[-1][0], threshold=threshold)
        return self.getl()


host = "10.0.0.2"
rob = urx.Robot(host, use_rt=True)

a = [1.206207036972046, -2.4435513655291956, -1.5308025519000452, -0.5937169233905237, 1.610512137413025, -0.0019915739642542007]
p1 = [0.2676576791667157, 0.34573049516866106, -0.03242200013357144, -2.9478270655963588, 0.6217635106620352, 0.019860802073762816]
b = [0.7452199459075928, -2.4435394446002405, -1.53143817583193, -0.5937045256244105, 1.6100807189941406, -0.0020392576800745132]
c = [0.25382813811302185, -2.44346791902651, -1.531306568776266, -0.5937169233905237, 1.6100926399230957, -0.002003494893209279]

poses = [(a,0), (p1,1), (b,0), (c,0)]

#rob.movej(a,1,1)
#rob.movej(b,1,1)
#rob.movej(c,1,1)
#rob.movexs("movel",)

movejls(rob, poses, 1, 1)

