from controller import Robot

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
    rightmotor.setVelocity(1)
    leftmotor.setVelocity(1)
    
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    
    print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(irl2_val, irl1_val, ircl_val, ircr_val, irr1_val, irr2_val))