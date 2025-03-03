"""motor_rotation controller."""

from controller import Robot, Keyboard

def run_controller():
    # Membuat instance robot.
    robot = Robot()

    # Mendapatkan time step dari dunia simulasi.
    timestep = int(robot.getBasicTimeStep())

    # Mendapatkan instance device motor.
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

    # Menginisialisasi perangkat keyboard
    keyboard = robot.getKeyboard()
    keyboard.enable(timestep)

    print("Program kendali motor e-puck dengan keyboard dimulai.")
    print("Gunakan tombol WASD untuk bergerak:")
    print("W: Maju, S: Mundur, A: Kiri, D: Kanan")
    print("Tombol R: Maju Terus (aktifkan/nonaktifkan)")
    print("Tombol S (sendiri, bukan WASD): Berhenti")
    print("Log akan ditampilkan di terminal ini.")

    # Variabel status untuk maju terus dan debouncing R
    maju_terus_aktif = False
    r_key_pressed_last_step = False # Status tombol R di langkah sebelumnya

    # Loop utama:
    while robot.step(timestep) != -1:
        left_speed = 0
        right_speed = 0
        r_key_currently_pressed = False # Reset status tombol R saat ini

        key = keyboard.getKey()

        # Kendali WASD dan fungsi lainnya
        if key == ord('W') or key == ord('w'):
            left_speed = 5
            right_speed = 5
            maju_terus_aktif = False
            print("Tombol W ditekan: Maju (WASD)")
        elif key == ord('S') or key == ord('s'):
            left_speed = -5
            right_speed = -5
            maju_terus_aktif = False
            print("Tombol S ditekan: Mundur (WASD)")
        elif key == ord('A') or key == ord('a'):
            left_speed = -3
            right_speed = 3
            maju_terus_aktif = False
            print("Tombol A ditekan: Belok Kiri")
        elif key == ord('D') or key == ord('d'):
            left_speed = 3
            right_speed = -3
            maju_terus_aktif = False
            print("Tombol D ditekan: Belok Kanan")
        elif key == ord('R') or key == ord('r'):
            r_key_currently_pressed = True # Set status tombol R saat ini ditekan
        elif key == ord('S') or key == ord('s'): # Tombol 'S' atau 's' untuk STOP (standalone)
            left_speed = 0
            right_speed = 0
            maju_terus_aktif = False
            print("Tombol S ditekan: BERHENTI (Tombol S Sendiri)")
        elif key != -1:
            print(f"Tombol dengan kode {key} ditekan (tidak terdefinisi).")
            maju_terus_aktif = False

        # Debouncing dan logika Maju Terus untuk tombol R
        if r_key_currently_pressed and not r_key_pressed_last_step:
            maju_terus_aktif = not maju_terus_aktif
            if maju_terus_aktif:
                print("Tombol R ditekan: Maju Terus DI AKTIFKAN")
            else:
                print("Tombol R ditekan: Maju Terus DI NONAKTIFKAN")

        r_key_pressed_last_step = r_key_currently_pressed # Update status tombol R untuk langkah berikutnya

        # Logika maju terus (tetap sama)
        if maju_terus_aktif:
            left_speed = 5
            right_speed = 5

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

    # Kode cleanup exit
    print("Program selesai.")

if __name__ == "__main__":
    run_controller()