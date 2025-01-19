from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
prime_hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)
motor_2 = Motor(Port.B, Direction.COUNTERCLOCKWISE)
front = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(motor_2, motor, 80, 110)

# Code credit: https://github.com/MonongahelaCryptidCooperative/FLL-2023-old/blob/main/mcc_icons_music.py
def Moana_Song():
    x0 = ["D4/8", "C4/8", "D4/6", "R/12", "F4/4", "F4/4"]
    x1 = ["D4/8", "C4/8", "D4/6", "R/12", "G4/4", "G4/4"]
    x2 = ["F4/8", "F4/8", "F4/4", "A4/4", "A4/4"]
    x3 = ["F4/8", "D4/8", "F4/4", "A4/4", "A4/4"]
    x4 = ["G4/8", "A4/8", "A#4/2", "F4/2", "C#4/2", "R/4"]
    x5 = ["F4/8", "G4/8", "A4/4" "R/6"]
    x6 = ["F4/4", "F4/4", "C5/2", "G4/2", "R/4"]
    x7 = ["C4/4", "C5/4", "D5/4", "A4/2", "G4/2"]
    x8 = ["C4/4", "C4/4", "C5/4", "C5/1"]

    test = x0 + x0 + x1 + x1 + x2 + x3 + x4 + x5 + x5 + x5 + x6 + x7 +x8
    return test

# Code written by Angela X. 
# Music was aranged by D. Cheston
# The letter is the pitch. The first number is the octave.
# The second number is how long the note is held.
# Ex:"B4/8" 
# B4: The pitch B in the 4th octave. In scientific pitch notation, (and on the
# piano and other istruments) this is just below middle C (C4).
#/8: Indicates that the note should be played as an eighth note, 
# meaning it lasts for one-eighth the duration of a whole note.  
def get_pirates_of_the_caribbean_notes():
    x0 = ["A4/8", "C4/8"]
    x1 = ["D4/4", "D4/4", "D4/8", "E4/8", "F4/4", "F4/4", "F4/8", "G4/8", "E4/4", "E4/4", "D4/8", "C4/8", "C4/8", "D4/8", "R/4"]
    x2 = ["A4/8", "C4/8", "D4/4", "D4/4", "D4/8", "E4/8", "F4/4", "F4/4", "F4/8", "G4/8", "E4/4", "E4/4", "D4/8", "C4/8", "D4/2"]
    x3 = ["A4/8", "C4/8", "D4/4", "D4/4", "D4/8", "F4/8", "G4/4", "G4/4", "G4/8", "A4/8", "Bb4/4", "Bb4/4", "A4/8", "G4/8", "A4/8", "D4/8", "R/4"]
    x4 = ["D4/8", "E4/8", "F4/4", "F4/4", "G4/4", "A4/2"]
    x5 = ["D4/8", "F4/8", "E4/4", "E4/4", "F4/8", "D4/8", "E4/2", "R/4"]

    # Combining the segments into a test list
    test = x0 + x1 + x2 + x3 + x4 + x5 
    return test

    
async def subtask():
    print('DaKiwi')
    await drive_base.straight(250 / 3)
    await drive_base.straight(-80 / 3)
    await drive_base.turn(370 / 3)
    await drive_base.straight(70 / 3)
    await front.run_angle(1000, -250)
    await drive_base.straight(-70 / 3)
    await drive_base.straight(150 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await front.run_angle(1000, 250)
    await drive_base.curve(-90 / 3, 188 / 3, Stop.NONE)
    await drive_base.straight(300 / 3, Stop.NONE)
    await drive_base.straight(-30 / 3, Stop.NONE)
    await drive_base.straight(30 / 3, Stop.NONE)
    await front.run_angle(1000, -250)
    await drive_base.straight(-30 / 3, Stop.NONE)
    await drive_base.straight(30 / 3)
    await drive_base.straight(-30 / 3)
    await drive_base.straight(30 / 3)
    await front.run_angle(1000, 250)
    await drive_base.turn(178 / 3)
    await drive_base.turn(-367 / 3)
    await drive_base.straight(250 / 3)
    await drive_base.straight(-80 / 3)
    await front.run_angle(1000, -250)
    await drive_base.turn(370 / 3)
    await front.run_angle(1000, 110)
    await front.run_angle(1000, -110)
    await front.run_angle(1000, 110)
    await front.run_angle(1000, -110)
    await front.run_angle(1000, 110)
    await front.run_angle(1000, -110)
    await drive_base.straight(70 / 3)
    await drive_base.straight(-70 / 3)
    await drive_base.straight(150 / 3, Stop.NONE)
    await front.run_angle(1000, 250)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)




async def subtask2():
    for count in range(1):
        await wait(1)
        await prime_hub.speaker.play_notes(Moana_Song())

async def main():
    drive_base.use_gyro(True)
    print('voltage is', prime_hub.battery.voltage())
    await multitask(subtask(), subtask2())


run_task(main())
