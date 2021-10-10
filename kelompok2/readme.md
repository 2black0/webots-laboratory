# Arena

![Arena](https://github.com/2black0/webots-laboratory/blob/6821642d7449c7fbabcc026cab05f311bd9c2706/competition/line-arena/img/full-arena.png)

# List Component of Robot
## Sensor

![Inertial Unit ](https://github.com/2black0/webots-laboratory/blob/6821642d7449c7fbabcc026cab05f311bd9c2706/competition/line-arena/img/inertial-unit.png)

1. Inertial Unit 

```
"inertial unit"
```

![Distance Sensor](https://github.com/2black0/webots-laboratory/blob/e5155ba50e504a4b3106b1218210571894c044d8/competition/line-arena/img/sensor.png)

2. Line Sensor

```
"IRL2"
"IRL1"
"IRCL"
"IRCR"
"IRR1"
"IRR2"
```

3. Distance Sensor

```
"ds_right"
"ds_left"
"ds_front"
"ds_right_maze"
```
4. Wheel position

```
"ps_1"
"ps_2"
```

![Camera](https://github.com/2black0/webots-laboratory/blob/6821642d7449c7fbabcc026cab05f311bd9c2706/competition/line-arena/img/camera.png)

5. Camera

```
"CAM"
```

## Actuator

![Wheel](https://github.com/2black0/webots-laboratory/blob/6821642d7449c7fbabcc026cab05f311bd9c2706/competition/line-arena/img/wheel-motor.png)

1. Wheel
```
"motor_1"
"motor_2"
```

![Arm](https://github.com/2black0/webots-laboratory/blob/9bf2197f52fc51027ad82c0f9bfa49ccd7cbddb7/competition/line-arena/img/arm.png)

2. Arm

```
"r_motor"
"l_motor"
"base_motor"
"arm1_motor"
"arm2_motor"
```
# Rule
1. Robot start from starting point
2. Robot have to following the line
3. Robot have to following the wall when no line
4. Robot pick the box with the arm and bring the box
5. Robot finish and stop in finishing point