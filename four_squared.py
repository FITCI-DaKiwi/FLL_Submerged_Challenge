from pybricks.hub import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, wheel_diameter, axle_distance
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left = motor(Port.A, Direction, COUNTERCLOCKWISE)
Right = Motor(Port.B, Direction. CLOCKWISE)
wheel_diameter = 81.6
axle_distance = 116
drive_base = DriveBase(left_motor = left, right_motor = Right. wheel_diameter = wheel_diameter, axle_track = axle_distance):
# The main program starts here.

drive_base.straight(355)
drive_base.turn(-90)
drive_base.straight(310)
drive_base.turn(-90)
drive_base.straight(355)
drive_base.turn(-90)
drive_base.straight(310)
drive_base.turn(-90)

