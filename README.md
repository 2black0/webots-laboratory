# 🤖 Webots Robot Control Tutorial

Welcome to the **Webots Robot Control Tutorial** repository!
This project is a curated collection of robot control examples and sensor interfacing using the [Webots simulator](https://cyberbotics.com/). It covers fundamental techniques such as Bang-Bang, PID, Fuzzy Logic controllers, as well as sensor-based feedback systems. Designed for students, educators, and robotics enthusiasts.

---

## 📂 Project Structure

```
.
├── LICENSE
├── README.md
└── Tutorial
    ├── controllers/                  # Python-based Webots controllers
    │   ├── bangbang_controller_wall_following/       # Bang-bang control example
    │   ├── fuzzy_logic_controller_wall_following/    # Fuzzy logic wall following
    │   ├── pid_controller_wall_following/            # PID-based wall following
    │   ├── motor_teleoperation/                      # Manual motor control
    │   ├── sensor_accelerometer_gyroscope/           # IMU sensor reading
    │   ├── sensor_odometer_calculation/              # Odometer calculation example
    │   ├── sensor_proximity/                         # Single proximity sensor
    │   └── sensor_ultrasonic/                        # Multiple ultrasonic (proximity) sensors
    ├── requirements.txt               # Python dependencies (if any)
    └── worlds/
        └── arena.wbt                 # Simulation world for all tutorials
```

---

## 🚀 Getting Started

### 🛠️ Requirements

* [Webots Simulator](https://cyberbotics.com/) (version 2023+ recommended)
* Python 3.x (with Webots Python controller bindings)
* \[Optional] `pip install numpy scikit-fuzzy` (for fuzzy logic controller)

### ▶️ Running a Simulation

1. Open Webots and load the `arena.wbt` world from the `Tutorial/worlds/` directory.
2. Choose the desired controller from `Tutorial/controllers/` by:

   * Right-clicking on the robot
   * Selecting "Controller"
   * Choosing the appropriate controller script
3. Run the simulation and observe the behavior.

---

## 📘 Controllers Description

| Controller Directory                     | Description                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------- |
| `bangbang_controller_wall_following/`    | Implements simple bang-bang wall-following based on threshold distance.   |
| `pid_controller_wall_following/`         | PID control for smoother wall-following with continuous feedback.         |
| `fuzzy_logic_controller_wall_following/` | Uses fuzzy logic rules to navigate by maintaining distance from the wall. |
| `motor_teleoperation/`                   | Enables manual control of robot motors using predefined commands.         |
| `sensor_accelerometer_gyroscope/`        | Reads IMU values (acceleration and rotation) from the e-puck robot.       |
| `sensor_odometer_calculation/`           | Demonstrates basic odometry calculation using wheel encoders.             |
| `sensor_proximity/`                      | Prints readings from a single proximity sensor (`ps0`).                   |
| `sensor_ultrasonic/`                     | Reads and displays values from all 8 e-puck proximity sensors.            |

---

## 🎯 Learning Goals

By exploring this repository, learners will be able to:

* Understand and compare different robot control techniques.
* Interface various onboard sensors in Webots.
* Implement reactive and feedback-based control.
* Simulate realistic robotics scenarios and evaluate algorithms.

---

## 📦 Requirements

Install Python libraries only if you're running advanced control logic (e.g. fuzzy):

```bash
pip install numpy scikit-fuzzy
```

For default use, Webots comes with all necessary Python controller bindings.

---

## 🧑‍💻 Author

Developed by [2black0](https://github.com/2black0)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

---

> ✨ Contributions and feedback are welcome! Feel free to open issues or submit pull requests.