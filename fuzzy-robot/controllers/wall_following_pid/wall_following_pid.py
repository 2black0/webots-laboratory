"""wall_following_pid_controller."""

from controller import Robot
import sys

def calculate_motor_velocity(signal_percentage):
    """Konversi sinyal persentase kecepatan ke kecepatan motor (rad/s)."""
    MAX_SPEED_RAD_PER_SEC = 6.28
    return (signal_percentage / 100.0) * MAX_SPEED_RAD_PER_SEC

def run_robot(robot):
    timestep = 64

    # Inisialisasi Sensor Ultrasonik
    sensor_wall_following = []
    sensor_names = ['ps0', 'ps1', 'ps2'] # Sensor depan dan samping kanan
    for name in sensor_names:
        sensor = robot.getDevice(name)
        sensor_wall_following.append(sensor)
        sensor.enable(timestep)

    # Inisialisasi Motor Roda
    roda = []
    roda_names = ['left wheel motor', 'right wheel motor']
    for name in roda_names:
        motor = robot.getDevice(name)
        roda.append(motor)
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)

    # Konstanta PID Kontrol
    SETPOINT_IDEAL = 100
    KP = 0.35
    KI = 0.00001
    KD = 0.002
    KECEPATAN_DASAR = 80

    # Variabel PID
    error = [0.0, 0.0, 0.0] # error[0] = saat ini, error[1] = integral, error[2] = sebelumnya
    integral_error = 0.0
    pid_control = 0.0

    print("Program Wall Following Manual (PID) E-puck Dimulai")
    print("Kontrol PID menggunakan rata-rata sensor ps1 & ps2 untuk ikuti dinding kanan")
    print("Tuning PID: Struktur Parameter Referensi, Integral Saturation, KP & KD diubah")
    print("Log sensor, kecepatan motor, error PID ditampilkan di terminal")
    print("Loop utama dimulai...")

    # Loop Utama Kontrol Robot
    while robot.step(timestep) != -1:
        normal_speed_percentage = KECEPATAN_DASAR
        fast_speed_percentage = 100

        # Baca Nilai Sensor
        nilai_sensor = [s.getValue() for s in sensor_wall_following]
        ps0, ps1, ps2 = nilai_sensor

        # Hitung Rata-rata Sensor ps1 dan ps2
        sensor_rata_rata = ps1

        # Hitung Error
        error[0] = SETPOINT_IDEAL - sensor_rata_rata

        # Kendali Proporsional (P)
        control_p = error[0] * KP

        # Kendali Integral (I) dengan Saturation
        error[1] += error[0]
        if error[1] > 150:
            error[1] = 150
        elif error[1] < -150:
            error[1] = -150
        control_i = error[1] * KI

        # Kendali Derivatif (D)
        control_d = (error[0] - error[2]) * KD
        error[2] = error[0]

        # Kontrol PID Total
        pid_control = control_p + control_i + control_d

        # Batasi Output PID
        max_pid_control_percentage = (fast_speed_percentage - normal_speed_percentage - 1)
        if pid_control >= max_pid_control_percentage:
            pid_control = max_pid_control_percentage
        elif pid_control <= -max_pid_control_percentage:
            pid_control = -max_pid_control_percentage

        # Kecepatan Motor dengan Koreksi PID
        kecepatan_kiri_percentage = normal_speed_percentage + pid_control
        kecepatan_kanan_percentage = normal_speed_percentage - pid_control

        # Batasi Kecepatan Motor
        kecepatan_kiri_percentage = max(min(kecepatan_kiri_percentage, 100), 0)
        kecepatan_kanan_percentage = max(min(kecepatan_kanan_percentage, 100), 0)

        # Set Kecepatan Motor (Persentase Velocity)
        roda[0].setVelocity(calculate_motor_velocity(kecepatan_kiri_percentage))
        roda[1].setVelocity(calculate_motor_velocity(kecepatan_kanan_percentage))

        # Logging
        log_string = "S: ps0:{:05.2f}, ps1:{:05.2f}, ps2:{:05.2f} | M: kiri:{:.2f}, kanan:{:.2f} | Err: {:05.2f}, P: {:05.2f}, I: {:05.2f}, D: {:05.2f}".format(
            ps0, ps1, ps2, kecepatan_kiri_percentage, kecepatan_kanan_percentage, error[0], control_p, control_i, control_d
        )
        print(log_string)

if __name__ == "__main__":
    robot_instance = Robot()
    run_robot(robot_instance)