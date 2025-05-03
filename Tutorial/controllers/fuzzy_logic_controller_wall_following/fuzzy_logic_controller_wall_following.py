"""wall_following_fuzzy_controller."""

from controller import Robot
import sys
import skfuzzy as fuzz
from skfuzzy import control

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

    # Konstanta Fuzzy Control
    SETPOINT_IDEAL = 100
    KECEPATAN_DASAR = 80
    FAST_SPEED_PERCENTAGE = 100

    # Fuzzy Logic Controller Setup
    # 1. Fuzzy Input (Error Jarak)
    error_jarak = control.Antecedent(universe=[-200, 200], label='ErrorJarak') # Range error yang mungkin
    error_jarak['NB'] = fuzz.trimf(error_jarak.universe, [-200, -200, -50]) # Negative Big
    error_jarak['NS'] = fuzz.trimf(error_jarak.universe, [-50, -25, 0])    # Negative Small
    error_jarak['ZE'] = fuzz.trimf(error_jarak.universe, [-25, 0, 25])     # Zero
    error_jarak['PS'] = fuzz.trimf(error_jarak.universe, [0, 25, 50])      # Positive Small
    error_jarak['PB'] = fuzz.trimf(error_jarak.universe, [50, 200, 200])   # Positive Big

    # 2. Fuzzy Output (Koreksi Kecepatan)
    koreksi_kecepatan = control.Consequent(universe=[-100, 100], label='KoreksiKecepatan') # Range koreksi kecepatan
    koreksi_kecepatan['RL'] = fuzz.trimf(koreksi_kecepatan.universe, [-100, -100, -50]) # Right Large (Belok Kanan Tajam)
    koreksi_kecepatan['RS'] = fuzz.trimf(koreksi_kecepatan.universe, [-50, -25, 0])     # Right Small (Belok Kanan Sedikit)
    koreksi_kecepatan['ZE'] = fuzz.trimf(koreksi_kecepatan.universe, [-25, 0, 25])      # Zero (Tidak Ada Koreksi)
    koreksi_kecepatan['LS'] = fuzz.trimf(koreksi_kecepatan.universe, [0, 25, 50])      # Left Small (Belok Kiri Sedikit)
    koreksi_kecepatan['LL'] = fuzz.trimf(koreksi_kecepatan.universe, [50, 100, 100])    # Left Large (Belok Kiri Tajam)

    # 3. Fuzzy Rules
    rules = [
        control.Rule(error_jarak['NB'], koreksi_kecepatan['RL']), # Error Negatif Besar -> Belok Kanan Tajam (RL) - DIBALIK!
        control.Rule(error_jarak['NS'], koreksi_kecepatan['RS']), # Error Negatif Kecil -> Belok Kanan Sedikit (RS) - DIBALIK!
        control.Rule(error_jarak['ZE'], koreksi_kecepatan['ZE']), # Error Zero -> Tidak Ada Koreksi (ZE)
        control.Rule(error_jarak['PS'], koreksi_kecepatan['LS']), # Error Positif Kecil -> Belok Kiri Sedikit (LS)
        control.Rule(error_jarak['PB'], koreksi_kecepatan['LL'])  # Error Positif Besar -> Belok Kiri Tajam (LL)
    ]

    # 4. Control System Creation and Simulation
    wall_following_ctrl = control.ControlSystem(rules=rules)
    wall_following_sim = control.ControlSystemSimulation(wall_following_ctrl)

    print("Program Wall Following Manual (Fuzzy Logic) E-puck Dimulai")
    print("Kontrol Fuzzy menggunakan sensor ps1 untuk ikuti dinding kanan")
    print("Tuning Fuzzy: Membership function dan Rules mungkin perlu disesuaikan")
    print("Log sensor, kecepatan motor, output fuzzy ditampilkan di terminal")
    print("Loop utama dimulai...")

    # Loop Utama Kontrol Robot
    while robot.step(timestep) != -1:
        normal_speed_percentage = KECEPATAN_DASAR

        # Baca Nilai Sensor
        nilai_sensor = [s.getValue() for s in sensor_wall_following]
        ps0, ps1, ps2 = nilai_sensor

        # Hitung Rata-rata Sensor ps1 dan ps2 (Fokus ke ps1 saja untuk fuzzy ini)
        sensor_rata_rata = ps1

        # Hitung Error
        error_value = SETPOINT_IDEAL - sensor_rata_rata

        # Fuzzy Control Calculation
        wall_following_sim.input['ErrorJarak'] = error_value
        wall_following_sim.compute()
        pid_control = wall_following_sim.output['KoreksiKecepatan'] # Output fuzzy sebagai koreksi kecepatan

        # Batasi Output Fuzzy (opsional, bisa disesuaikan)
        max_pid_control_percentage = (FAST_SPEED_PERCENTAGE - normal_speed_percentage - 1)
        if pid_control >= max_pid_control_percentage:
            pid_control = max_pid_control_percentage
        elif pid_control <= -max_pid_control_percentage:
            pid_control = -max_pid_control_percentage

        # Kecepatan Motor dengan Koreksi Fuzzy
        kecepatan_kiri_percentage = normal_speed_percentage + pid_control
        kecepatan_kanan_percentage = normal_speed_percentage - pid_control

        # Batasi Kecepatan Motor
        kecepatan_kiri_percentage = max(min(kecepatan_kiri_percentage, 100), 0)
        kecepatan_kanan_percentage = max(min(kecepatan_kanan_percentage, 100), 0)

        # Set Kecepatan Motor (Persentase Velocity)
        roda[0].setVelocity(calculate_motor_velocity(kecepatan_kiri_percentage))
        roda[1].setVelocity(calculate_motor_velocity(kecepatan_kanan_percentage))

        # Logging
        log_string = "S: ps0:{:05.2f}, ps1:{:05.2f}, ps2:{:05.2f} | M: kiri:{:.2f}, kanan:{:.2f} | Err: {:05.2f}, FuzzyOut: {:05.2f}".format(
            ps0, ps1, ps2, kecepatan_kiri_percentage, kecepatan_kanan_percentage, error_value, pid_control
        )
        print(log_string)

if __name__ == "__main__":
    robot_instance = Robot()
    run_robot(robot_instance)