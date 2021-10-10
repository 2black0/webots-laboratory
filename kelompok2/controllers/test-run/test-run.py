from controller import Robot

def maju():
    rightmotor.setVelocity(8)
    leftmotor.setVelocity(8)    
def hadap_kiri():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(-4)
def hadap_kanan():
    rightmotor.setVelocity(6)
    leftmotor.setVelocity(-6)
def diam():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)

robot = Robot()
timestep = int(robot.getBasicTimeStep())

leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

irl2 = robot.getDevice('IRL2')
irl1 = robot.getDevice('IRL1')
ircl = robot.getDevice('IRCL')
ircr = robot.getDevice('IRCR')
irr1 = robot.getDevice('IRR1')
irr2 = robot.getDevice('IRR2')

irl2.enable(timestep)
irl1.enable(timestep)
ircl.enable(timestep)
ircr.enable(timestep)
irr1.enable(timestep)
irr2.enable(timestep)

while robot.step(timestep) != -1:  
    rightmotor.setVelocity(15)
    leftmotor.setVelocity(15)

    
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    
    ir_kiri = ircl_val + irl1_val + irl2_val
    ir_kanan = ircr_val + irr1_val + irr2_val
    
    print('{:.2f} {:.2f}'.format(ir_kiri, ir_kanan))
    if ir_kiri < 1900 and ir_kanan > 2000:
        maju()
    else :
        maju()