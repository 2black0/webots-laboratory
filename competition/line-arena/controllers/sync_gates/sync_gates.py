from controller import Robot, Motor, DistanceSensor, PositionSensor, InertialUnit

robot = Robot()
timestep = 16

left1_gate = robot.getDevice('l1')
left2_gate = robot.getDevice('l2')
right1_gate = robot.getDevice('r1')
right2_gate = robot.getDevice('r2')

left1_gate.setPosition(float('inf'))
left2_gate.setPosition(float('inf'))
right1_gate.setPosition(float('inf'))
right2_gate.setPosition(float('inf'))

counter = 0

while robot.step(timestep) != -1:
    if counter == 1:
        left1_gate.setPosition(1.5)
        left2_gate.setPosition(0)
        right1_gate.setPosition(1.5)
        right2_gate.setPosition(0)
    elif counter == 188:
        left1_gate.setPosition(1.5)
        left2_gate.setPosition(1.5)
        right1_gate.setPosition(1.5)
        right2_gate.setPosition(1.5)
    elif counter == 625:
        left1_gate.setPosition(0)
        left2_gate.setPosition(1.5)
        right1_gate.setPosition(0)
        right2_gate.setPosition(1.5)
    elif counter == 813:
        left1_gate.setPosition(0)
        left2_gate.setPosition(0)
        right1_gate.setPosition(0)
        right2_gate.setPosition(0)
    elif counter == 1250:
        counter = 0
    
    counter+=1