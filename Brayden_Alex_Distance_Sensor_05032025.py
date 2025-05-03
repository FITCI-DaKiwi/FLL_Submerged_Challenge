from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase,
from pybricks.tools import wait, StopWatch

hub = PrimeHub( )
left = Motor(Port.A, Direction. COUNTERCLOCKWISE)
Right = Motor(Port.B, Direction. CLOCKWISE)
wheel_diameter = 81.6
axle_distance = 116
drive_base = DriveBase(left_motor = left, right_motor = Right, wheel_diameter = wheel_diameter, axle_track = axle_distance)

# The main program starts here.

# drive_base.straight(650)
# drive_base.turn(-90)

# while True:
#     drive_base.drive(200,0)
#     distance_sensor = UltrasonicSensor(Port.D)
#     if distance_sensor.distance() < 41:
#         drive_base.brake
#         print("Obstacle detected! Stopping")
#         break
while True:
    drive_base.drive(400,0)
    distance_sensor = UltrasonicSensor(Port.D)
    if distance_sensor.distance() < 200:
        drive_base.brake
        print("Obstacle detected! Stopping")
        break

drive_base.turn(90)

while True:
    drive_base.drive(400,0)
    distance_sensor = UltrasonicSensor(Port.D)
    if distance_sensor.distance() < 65:
        drive_base.brake
        print("Obstacle detected! Stopping")
        break