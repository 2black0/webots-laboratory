from controller import Robot

tembok = 2
garis_kanan = 1
garis_kiri = 1

def run_robot(robot):

    time_step = 16
    max_speed = 1000
    
def maju():
    rightmotor.setVelocity(6)
    leftmotor.setVelocity(6)
def hadap_kiri():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(0)
def hadap_kanan():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(4)
def diam():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)
# def misal():
    # if ir_kanan > 1500 and ir_kiri < 1500:
       # hadap_kiri()
    # elif garis < 2900:
        # maju()
    # elif ir_kanan < 1500 and ir_kiri > 1500:
        # hadap_kanan() 
    # elif line_kiri < 600:
        # diam()
        # hadap_kiri()
def fix():
    if ir_kanan > 1500 and ir_kiri < 1500:
       hadap_kiri()
    elif ir_kanan < 1500 and ir_kiri > 1500:
        hadap_kanan()
    elif ir_kanan < 600 and line_kanan < 400:
        hadap_kanan()  
    elif garis > 2900 :
         if line_kanan < 1200 :
            hadap_kiri()
    elif (ir_kanan > 1500 and garis_tengah > 400) or (ir_kiri > 1500 and garis_tengah > 400) :
        maju()
    elif ping_depan > 300:
        maju()
    elif ping_depan < 300:
        maju()
    else :
        maju()
# def pas():
    # if(garis > 3700 and ping_kanan < 1000) or (garis > 3700 and ping_kiri < 1000):
       # maju()
# def palang():
     # if line_kanan < 600 and line_kiri > 700:
            # hadap_kanan() 
     # elif line_kanan < 600 and line_kanan > 350 and garis_tengah > 700:
        # maju()
     # elif ping_depan < 300:
        # diam()
     # elif line_kanan < 350 and line_kiri < 350:
        # diam()
        
robot = Robot()
timestep = int(robot.getBasicTimeStep())

leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

pingkiri = robot.getDevice('ds_left')
pingkanan = robot.getDevice('ds_right')
pingdepan = robot.getDevice('ds_front')
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
pingkiri.enable(timestep)
pingkanan.enable(timestep)
pingdepan.enable(timestep)

while robot.step(timestep) != -1:  
    # rightmotor.setVelocity(10)
    # leftmotor.setVelocity(10)
    
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    ping_kiri = pingkiri.getValue()
    ping_kanan = pingkanan.getValue()
    ping_depan = pingdepan.getValue()
    
    line_kanan = irr1_val + irr2_val
    line_kiri = irl1_val + irl2_val
    ir_kanan = ircr_val + irr1_val + irr2_val
    ir_kiri = ircl_val + irl1_val + irl2_val
    garis_tengah = ircr_val + ircl_val
    garis = ir_kanan + ir_kiri
    
    
    
    print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} '.format(line_kanan, line_kiri, ir_kanan, ir_kiri, garis_tengah, garis))
    
    if tembok == 2:
        fix()
        

    # if tembok == 2:
       # misal()
       # pas()
    # if garis < 3000 and ping_kiri < 1000:
       # tembok = 3
    # elif tembok == 3:
       # fix()
       # if ping_kanan < 900:
         # tembok = 4
    # elif tembok == 4:
        # palang()
