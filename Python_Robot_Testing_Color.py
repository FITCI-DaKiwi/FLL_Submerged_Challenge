from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
sensor = ColorSensor(Port.D)


print(sensor.hsv())


hues = {
    Color.RED: 350,
    Color.BLUE: 210
}                                                                                                                                                                                                                                                                                               
saturation = 30

values = {
    None: 0,
    Color.WHITE: 60,
}

#sensor.color_map(hues, saturation, values)

while True:
    print(sensor.color())
    #print(color_sensor.color())
    wait(1000)