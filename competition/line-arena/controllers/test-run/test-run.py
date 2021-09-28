from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

while robot.step(timestep) != -1:  
    rightmotor.setVelocity(6.28)
    leftmotor.setVelocity(6.28)