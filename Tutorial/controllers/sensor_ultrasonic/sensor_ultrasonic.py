"""pembacaan_sensor_ultrasonic controller."""

from controller import Robot

def run_robot(robot):
    timestep = 64

    # Define sensor ultrasonik
    sensor_ultrasonic = []
    sensor_name = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7'] # Daftar nama sensor e-puck
    for i in range(8): # e-puck memiliki 8 sensor ultrasonik (proximity sensors)
        sensor = robot.getDevice(sensor_name[i])
        sensor_ultrasonic.append(sensor) # Tambahkan objek sensor ke list
        sensor.enable(timestep) # Enable sensor langsung (tanpa indeks)

    print("Program pembacaan sensor ultrasonik e-puck dimulai.")
    print("Nilai sensor akan ditampilkan dalam format banyak baris di terminal setiap langkah.")

    # Loop utama:
    while robot.step(timestep) != -1:
        sensor_values = []
        for i in range(8):
            sensor_values.append(sensor_ultrasonic[i].getValue())

        # Membuat string log banyak baris yang ringkas
        log_string_debug = ""
        for i in range(8):
            log_string_debug += f"ps{i}: {sensor_values[i]:.2f}  "
        print(log_string_debug) # Cetak log banyak baris

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)