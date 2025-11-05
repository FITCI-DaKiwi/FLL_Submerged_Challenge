from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Menu options. You can add as many as you like.
menu_options = ("1", "2")

# Disable the stop button to use the center button for menu navigation.
hub.system.set_stop_button(None)

# Initialize the menu index
menu_index = 0  # Start at the first option

while True:
    hub.display.char(menu_options[menu_index])

    # Wait for any button to be pressed
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(2)
    
    # Wait for the button to be released
    while hub.buttons.pressed():
        wait(2)

    # Check which button was pressed
    if Button.CENTER in pressed:
        # Center button confirms the selection and starts the program
        selected = menu_options[menu_index]
        if selected == "1":
            import FITCI_Run1_Nov6
        elif selected == "2":
            import FITCI_Run2_Nov6
        # Return to menu after completing the selected program
        continue
    elif Button.LEFT in pressed:
        # Left button increments the menu index
        menu_index = (menu_index + 1) % len(menu_options)
    elif Button.RIGHT in pressed:
        # Right button decrements the menu index
        menu_index = (menu_index - 1) % len(menu_options)

# Restore the stop button functionality
hub.system.set_stop_button(Button.CENTER)