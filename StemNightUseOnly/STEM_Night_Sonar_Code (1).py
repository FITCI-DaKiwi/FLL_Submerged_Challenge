from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
front = Motor(Port.E, Direction.COUNTERCLOCKWISE)
top = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(left, right, 81, 99)

drive_base.use_gyro(True)
drive_base.straight(235)
drive_base.settings(turn_rate=80)
drive_base.turn(90)
drive_base.straight(185)
top.run_angle(500,750)
top.run_angle(1000,-1900)
top.run_angle(500,500)
drive_base.straight(-150)