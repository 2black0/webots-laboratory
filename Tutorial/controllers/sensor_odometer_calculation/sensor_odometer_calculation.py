"""odometer_calculation controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
#import math

def run_robot(robot):
    # get the time step of the current world.
    timestep = 64
    max_speed = 2 #6.28
    
    #motor definition
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #get device odometry left & right
    left_ps = robot.getDevice('left wheel sensor')
    left_ps.enable(timestep)
    
    right_ps = robot.getDevice('right wheel sensor')
    right_ps.enable(timestep)
        
    #ps variable    
    ps_value = [0, 0]
    """dist_value = [0, 0]
    
    wheel_radius = 0.0205 #20.5 mm
    distance_between_wheels = 0.052 #52mm
    
    wheel_cirum = 2 * 3.14 * wheel_radius
    encoder_unit = wheel_cirum / 6.28
    
    robot_pose = [0, 0, 0] #x, y, theta
    last_ps_value = [0, 0]"""
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        ps_value[0] = left_ps.getValue()
        ps_value[1] = right_ps.getValue()
        
        #print("----------------------------")
        print("position sensor values: {} {}".format(ps_value[0], ps_value[1]))
        
        left_motor.setVelocity(3)
        right_motor.setVelocity(2)
        
        """for ind in range(2):
            diff = ps_value[ind] - last_ps_value[ind]
            if diff < 0.001:
                diff = 0
                ps_value[ind] = last_ps_value[ind]
            dist_value[ind] = ps_value[ind] * encoder_unit
            
        v = (dist_value[0] + dist_value[1]) / 2.0
        w = (dist_value[0] - dist_value[1]) / distance_between_wheels
        
        dt = 1
        robot_pose[2] += (w * dt)
        
        vx = v + math.cos(robot_pose[2])
        vy = v + math.sin(robot_pose[2])
        
        robot_pose[0] = (vx * dt)
        robot_pose[1] = (vy * dt)
        
        print("robot pose: {}".format(robot_pose))"""
        
        #print("distance sensor values: {} {}".format(dist_value[0], dist_value[1]))
        
        """for ind in range(2):
            last_ps_value[ind] = ps_value[ind]"""

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)