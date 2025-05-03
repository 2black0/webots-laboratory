"""odometer_calculation controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Accelerometer, Gyro

def run_robot(robot):
    # get the time step of the current world.
    timestep = 64
    max_speed = 6.28
    
    #motor declaration
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #acc declaration
    acc = robot.getDevice('accelerometer')
    acc.enable(timestep)
    
    #gyro declaration
    gyro = robot.getDevice('gyro')
    gyro.enable(timestep)    
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        acc_value = acc.getValues()
        gyro_value = gyro.getValues()

        round_acc_value = [f"{num:.2f}" for num in acc_value]
        round_gyro_value = [f"{num:.2f}" for num in gyro_value]

        #print("----------------------------")
        print("IMU sensor values: {} {}".format(round_acc_value, round_gyro_value))
        
        #left_motor.setVelocity(max_speed)
        #right_motor.setVelocity(max_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)