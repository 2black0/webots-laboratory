"""wall_following_manual_controller_smooth_corrected_setpoint_tuned."""

from controller import Robot

def run_robot(robot):
    timestep = 64

    # Inisialisasi Sensor Ultrasonik
    sensor_wall_following = []
    sensor_name = ['ps0', 'ps1', 'ps2']
    for name in sensor_name:
        sensor = robot.getDevice(name)
        sensor_wall_following.append(sensor)
        sensor.enable(timestep)

    # Inisialisasi Motor Roda
    roda = []
    nama_roda = ['left wheel motor', 'right wheel motor']
    for name in nama_roda:
        motor = robot.getDevice(name)
        roda.append(motor)
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)

    # Konstanta Kontrol Wall Following yang Dihaluskan
    SETPOINT_JAUH = 50        # Jarak dinding 'jauh' (nilai sensor) - DITURUNKAN
    SETPOINT_SEDANG = 60      # Jarak dinding 'sedang' - DITURUNKAN
    SETPOINT_DEKAT = 150
    SETPOINT_SANGAT_DEKAT = 200

    KECEPATAN_MAJU_PENUH = 3.0
    KECEPATAN_MAJU_SEDANG = 2.5
    KECEPATAN_MAJU_LAMBAT = 2.0
    KECEPATAN_BELOK_SEDANG = 1.5
    KECEPATAN_BELOK_TAJAM = 2.0


    print("Program Wall Following Manual (On-Off Halus) E-puck Dimulai")
    print("Menggunakan sensor ps0, ps1, ps2 untuk ikuti dinding kanan")
    print("Kontrol On-Off yang Dihaluskan dengan Tingkat Kecepatan")
    print("Log sensor & kecepatan motor (satu baris) ditampilkan di terminal")
    print("Loop utama dimulai...")

    # Loop Utama Kontrol Robot
    while robot.step(timestep) != -1:
        # Baca Nilai Sensor
        nilai_sensor = [s.getValue() for s in sensor_wall_following]
        ps0, ps1, ps2 = nilai_sensor

        kecepatan_kiri = KECEPATAN_MAJU_PENUH
        kecepatan_kanan = KECEPATAN_MAJU_PENUH

        # Logika Kontrol On-Off Wall Following yang Dihaluskan
        if ps0 > SETPOINT_SANGAT_DEKAT:
            # Sensor depan mendeteksi dinding sangat dekat, putar menjauh
            kecepatan_kiri = -KECEPATAN_BELOK_SEDANG
            kecepatan_kanan = KECEPATAN_BELOK_SEDANG
        elif ps2 < SETPOINT_JAUH:
            # Sensor samping kanan jauh dari dinding, belok kiri tajam
            kecepatan_kanan = KECEPATAN_MAJU_PENUH
            kecepatan_kiri = KECEPATAN_MAJU_LAMBAT
        elif ps2 < SETPOINT_SEDANG:
            # Sensor samping kanan agak jauh dari dinding, belok kiri sedang
            kecepatan_kanan = KECEPATAN_MAJU_SEDANG
            kecepatan_kiri = KECEPATAN_MAJU_LAMBAT
        elif ps2 > SETPOINT_DEKAT:
            # Sensor samping kanan terlalu dekat dengan dinding, belok kanan sedang (DIKOREKSI)
            kecepatan_kiri = KECEPATAN_MAJU_LAMBAT
            kecepatan_kanan = KECEPATAN_MAJU_SEDANG
        elif ps2 > SETPOINT_SANGAT_DEKAT:
            # Sensor samping kanan sangat dekat dengan dinding, belok kanan tajam (DIKOREKSI)
            kecepatan_kiri = KECEPATAN_MAJU_LAMBAT
            kecepatan_kanan = KECEPATAN_MAJU_PENUH
        else:
            # Jarak ideal, maju lurus
            kecepatan_kiri = KECEPATAN_MAJU_PENUH
            kecepatan_kanan = KECEPATAN_MAJU_PENUH

        # Set Kecepatan Motor
        roda[0].setVelocity(kecepatan_kiri)
        roda[1].setVelocity(kecepatan_kanan)

        # Logging Satu Baris (Sensor & Motor)
        log_string = "S: ps0:{:06.2f}, ps1:{:06.2f}, ps2:{:06.2f} | M: kiri:{:.2f}, kanan:{:.2f}".format(
            ps0, ps1, ps2, kecepatan_kiri, kecepatan_kanan
        )
        print(log_string)

if __name__ == "__main__":
    robot_instance = Robot()
    run_robot(robot_instance)