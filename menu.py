from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# Let's offer these menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6", "7", "8")

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.

pressed = []
hub.system.set_stop_button(None)
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
        menu_index = (menu_index + 1) % len(menu_options)
    elif Button.RIGHT in pressed:
        # Right button, so increment menu menu_index.
        menu_index = (menu_index - 1) % len(menu_options)

# Now we want to use the Center button as the stop button again.
hub.system.set_stop_button(Button.CENTER)

# Based on the selection, choose a program.
selected = menu_options[menu_index]
if selected == "1":
    import Run_1_collection
elif selected == "2":
    import Run_2_Second_run_Sonar_green_circle
elif selected == "3":
    import mission1_Taotao
elif selected == "4":
    import Kraken
elif selected == "5":
    import run_5
elif selected == "6":
    import run_6
elif selected == "7":
    import run_7
elif selected == "8":
    import Run_8_whale_dot_py_taste_good
