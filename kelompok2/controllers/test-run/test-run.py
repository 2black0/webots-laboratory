from controller import Robot

kondisi = 1
counter = 0

robot = Robot()
timestep = int(robot.getBasicTimeStep())

#inisialisasi motor kanan & kiri
leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

#inisialisasi sensor 
sensorkiri = robot.getDevice('ds_left')
sensorkanan = robot.getDevice('ds_right')
sensordepan = robot.getDevice('ds_front')
irl2 = robot.getDevice('IRL2')
irl1 = robot.getDevice('IRL1')
ircl = robot.getDevice('IRCL')
ircr = robot.getDevice('IRCR')
irr1 = robot.getDevice('IRR1')
irr2 = robot.getDevice('IRR2')

#aktivasi sensor
irl2.enable(timestep)
irl1.enable(timestep)
ircl.enable(timestep)
ircr.enable(timestep)
irr1.enable(timestep)
irr2.enable(timestep)
sensorkiri.enable(timestep)
sensorkanan.enable(timestep)
sensordepan.enable(timestep)


def run_robot(robot):
    time_step = 16
    max_speed = 1000
    
#fungsi gerak robot    
def jalan_lurus():
    rightmotor.setVelocity(5)
    leftmotor.setVelocity(5)
def belok_kiri():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(0)
def belok_kanan():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(4)
def berhenti():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)

#fungsi jalur robot line follower
def run():
    if garis_kanan > 1500 and garis_kiri < 1500:
       belok_kiri()
    elif garis_kanan < 1500 and garis_kiri > 1500:
        belok_kanan()
    elif garis_total < 2700 :
        if sens_kanan < 400 and sens_kiri > 600:
            belok_kanan()  
        elif sens_kiri < 400 and sens_kanan > 600:
            belok_kiri() 
        elif sens_kiri < 400 and sens_kanan < 400:
            belok_kiri()  
    elif sensor_kanan < 1000 or sensor_kiri < 1000 :
        jalan_lurus()
    
    else :
        jalan_lurus()

#fungsi halangan palang
def palang():
   if sens_kanan < 400 and sens_kiri < 400 :
       if sensor_depan < 700 :
           berhenti()
       elif sensor_depan > 700 :
           jalan_lurus()
           
   elif sens_kanan > 400 or sens_kiri > 400:
       run()
 
    
while robot.step(timestep) != -1:  
    # rightmotor.setVelocity(10)
    # leftmotor.setVelocity(10)
    counter+=1
    
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    sensor_kiri = sensorkiri.getValue()
    sensor_kanan = sensorkanan.getValue()
    sensor_depan = sensordepan.getValue()
    
    sens_kanan = irr1_val + irr2_val
    sens_kiri = irl1_val + irl2_val
    sens_tengah = ircr_val + ircl_val
    garis_kanan = ircr_val + irr1_val + irr2_val
    garis_kiri = ircl_val + irl1_val + irl2_val
    garis_total = garis_kanan + garis_kiri
    
    
    
    print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} '.format(sens_kanan, sens_kiri, garis_kanan, garis_kiri, sens_tengah, garis_total ))
    # print('{:.2f} {:.2f} {:.2f} '.format(sensor_depan, sensor_kanan, sensor_kiri ))
    # print('{:.2f} '.format(counter))
    
    if kondisi == 1 :
        run()
    if kondisi == 2 :
        palang()  
    if kondisi == 3 :
        berhenti()  
    
    if counter > 5100 and counter < 5700 :
        kondisi = 2
    if counter > 5700 :
        kondisi = 3
