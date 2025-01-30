from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Let's offer these menu options. You can add as many as you like.
menu_options = ("M", "A", "P")

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.

pressed = []

hub.system.set_stop_button(None)


stored_index = hub.system.storage(0, read=1)  # Read 1 byte from storage
menu_index = int.from_bytes(stored_index, 'little')
if menu_index < 0 or menu_index >= len(menu_options):
    menu_index = 0

while True:

    hub.display.char(menu_options[menu_index])

    # Wait for any button.
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    
    # Wait for the button to be released.
    while hub.buttons.pressed():
        wait(10)

    # Now check which button was pressed.
    if Button.CENTER in pressed:
        # Center button, so the menu is done!
        break
    elif Button.LEFT in pressed:
        # Left button, so decrement menu menu_index.
        menu_index = (menu_index - 1) % len(menu_options)
    elif Button.RIGHT in pressed:
        # Right button, so increment menu menu_index.
        menu_index = (menu_index + 1) % len(menu_options)

# Now we want to use the Center button as the stop button again.
hub.system.set_stop_button(Button.CENTER)

# Based on the selection, choose a program.
selected = menu_options[menu_index]
menu_index=menu_index+1
hub.system.storage(0, write=menu_index.to_bytes(1, 'little'))
if selected == "A":
    import apt_second_version
elif selected == "P":
    import dance_wo_blk_new
elif selected == "M":
    import Moana_Robot_Dance_New_Use_this

