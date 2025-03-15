from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase,
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left = Motor(Port.A, Direction. COUNTERCLOCKWISE)
Right = Motor(Port.B, Direction. CLOCKWISE)
wheel_diameter = 81.6
axle_distance = 116
drive_base = DriveBase(left_motor = left, right_motor = Right, wheel_diameter = wheel_diameter, 
axle_track = axle_distance)

# The main program starts here.

while True:
    # Sets up the code for when we need to stop the robot before it hits the wall
    drive_base.drive(200,0)
    # sets up the drive speed of the robot
    pass
    # makes the robot drive forever unless it is stopped by the program
    distance_sensor = UltrasonicSensor(Port.C)
    # Classifies the distance sensor and which port it comes from
    if distance_sensor.distance() < 50:
        # If the distance sensor is less that 5 centimeters away from an object
        drive_base.brake()
        # Stops the robots motion by actively slowwing it down
        print("Obstacle detected! Stopping")
        # Shows that the obstacle has been detected
        break
        # Stops the loop
# while distance_sensor.distance() > 50:
#     drive_base.straight(20)
# drive_base.straight(355)
# drive_base.turn(-90)
# drive_base.straight(310)
# drive_base.turn(-90)
# drive_base.straight(355)
# drive_base.turn(-90)
# drive_base.straight(310)
# drive_base.turn(-90)
