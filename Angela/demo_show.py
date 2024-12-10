from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
right = Motor(Port.A, Direction.CLOCKWISE)
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
front = Motor(Port.E, Direction.CLOCKWISE)
back = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(left, right, 81.6, 110)

# Initialize variables.
heading = 0

# The main program starts here.
drive_base.use_gyro(True)
heading = prime_hub.imu.heading()
print('Initial heading is: ', heading)
drive_base.settings(straight_speed=60)
drive_base.straight(-64)
drive_base.settings(straight_speed=500)
heading = prime_hub.imu.heading()
print('Before the U-turn, the heading is: ', heading)
front.run_angle(100, -65)
drive_base.curve(93.5, 180)
heading = prime_hub.imu.heading()
print('After the U-turn, the heading is: ', heading)
drive_base.straight(310)
heading = prime_hub.imu.heading()
print('Before the U-turn, the heading is: ', heading)
drive_base.curve(-100.45, heading)
heading = prime_hub.imu.heading()
print('After the U-turn, the heading is: ', heading)
