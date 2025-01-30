from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

# Set up all devices.
prime_hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)
motor_2 = Motor(Port.B, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(motor_2, motor, 80, 110)

# Code credit: https://github.com/MonongahelaCryptidCooperative/FLL-2023-old/blob/main/mcc_icons_music.py
def get_star_wars_notes():
    x0 = ["D4/12", "D4/12", "D4/12"]
    x1 = ["G4/2", "D5/2"]
    x2 = ["C5/12", "B4/12", "A4/12", "G5/2",  "D5/4"]
    x3 = ["C5/12", "B4/12", "C5/12", "A4/2",  "D4/6", "D4/12"]
    x4 = ["E4/4.", "E4/8", "C5/8", "B4/8",  "A4/8", "G4/8"]
    x5 = ["G4/12", "A4/12", "B4/12", "A4/6", "E4/12", "F#4/4", "D4/6", "D4/12"]
    x6 = ["D5/4", "A4/2", "D4/6", "D4/12"]
    x7 = ["G4/12", "A4/12", "B4/12", "A4/6", "E4/12", "F#4/4", "D5/6", "D5/12"]
    x8 = ["G5/6", "F5/12", "Eb5/6", "D5/12", "C5/6", "Bb4/12", "A4/6", "G4/12"]
    x9 = ["D5/2."]
    x10 = ["G5/12", "F5/12", "Eb5/12", "Bb5/2", "A5/4", "G5/8", "R/8", "G4/12", "G4/12", "G4/12", "G4/4"]
    test = x0 + x1 + x2 + x2 + x3 + x1 + x2 + x2 + x3 + x4 + x5 + x4 + x6 + x4 + x7 + x8 + x9 + x0 + x1 + x2 + x2 + x3 + x1 + x2 + x10
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
def get_APT_notes():
    x0 = ["F4/4", "F4/8", "F4/4", "E4/8", "E4/8", "E4/8", "B4/4", "B4/4", "C4/4","D4/4"]
    x1 = ["E4/4", "E4/8", "E4/4", "D4/8", "D4/8", "D4/8", "D4/4", "C4/4", "E4/2"]
    x2 = ["E4/8", "E4/8", "E4/8", "E4/8", "E4/8", "D4/8", "C4/4", "G4/4", "C4/4", "B3/4", "C4/4"]
    x3 = ["G3/4", "G3/8", "G3/4", "G3/8", "A3/4", "G3/4", "G3/8", "G3/4", "G3/8", "A3/4", 
    "G3/4", "G3/8", "G3/4", "G3/8", "A3/4", "G3/4", "R/8", "G3/8", "A3/8", "G3/8", "A3/4"]
    
    test = x0 + x1 + x0 + x2 + x3 + x3
    return test


    
async def subtask():
    await drive_base.straight(250 / 3)
    await drive_base.straight(-80 / 3)
    await drive_base.turn(370 / 3)
    await drive_base.straight(70 / 3)
    await drive_base.straight(-70 / 3)
    await drive_base.straight(150 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 188 / 3, Stop.NONE)
    await drive_base.straight(300 / 3, Stop.NONE)
    await drive_base.straight(-30 / 3, Stop.NONE)
    await drive_base.straight(30 / 3, Stop.NONE)
    await drive_base.straight(-30 / 3, Stop.NONE)
    await drive_base.straight(30 / 3)
    await drive_base.straight(-30 / 3)
    await drive_base.straight(30 / 3)
    await drive_base.turn(178 / 3)
    await drive_base.turn(-367 / 3)
    await drive_base.straight(250 / 3)
    await drive_base.straight(-80 / 3)
    await drive_base.turn(370 / 3)
    await drive_base.straight(70 / 3)
    await drive_base.straight(-70 / 3)
    await drive_base.straight(150 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await drive_base.curve(-90 / 3, 360 / 3, Stop.NONE)
    await drive_base.curve(90 / 3, 185 / 3, Stop.NONE)
    await drive_base.turn(-360)
    await drive_base.turn(470)
    await drive_base.turn(360)
    await drive_base.turn(-360)
    await drive_base.turn(360)


async def subtask2():
    for count in range(1):
        await wait(1)
        await prime_hub.speaker.play_notes(get_APT_notes())

async def main():
    drive_base.use_gyro(True)
    await multitask(subtask(), subtask2())


run_task(main())
