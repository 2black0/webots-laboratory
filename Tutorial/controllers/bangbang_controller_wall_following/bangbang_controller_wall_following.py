from controller import Robot

def calculate_motor(signal):
    return (signal/100)*6.28

def run_robot(robot):
    timestep = 64
    
    #define sensor
    sensor = []
    sensor_name =['ps0', 'ps1', 'ps2']
    for i in range(3):
        sensor.append(robot.getDevice(sensor_name[i]))
        sensor[i].enable(timestep)
    
    #define motor
    wheel = []
    wheel_name =['left wheel motor', 'right wheel motor']
    for i in range(2):
        wheel.append(robot.getDevice(wheel_name[i]))
        wheel[i].setPosition(float('inf'))
        wheel[i].setVelocity(0.0)
    
    set_point = 80
    fast_speed = 100

    while robot.step(timestep) != -1:
        sensor0_val = sensor[0].getValue()
        sensor1_val = sensor[1].getValue()
        sensor2_val = sensor[2].getValue()

        max_speed = calculate_motor(fast_speed)
        
        #cek depan
        if sensor0_val > 80:
            left = -max_speed
            right = max_speed
        else:
            #cek dinding kanan
            if sensor2_val > 80:
                left = max_speed
                right = max_speed
            else:                
                #koreksi jalan
                left = max_speed
                right = max_speed/8

            #patahan
            if sensor1_val > 80:
                left = max_speed/8
                right = max_speed
                
        wheel[0].setVelocity(left)
        wheel[1].setVelocity(right)
        
        log_string = "S: ps0:{:06.2f}, ps1:{:06.2f}, ps2:{:06.2f} | M: kiri:{:.2f}, kanan:{:.2f}".format(
            sensor0_val, sensor1_val, sensor2_val, left, right
        )
        print(log_string)
        
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)