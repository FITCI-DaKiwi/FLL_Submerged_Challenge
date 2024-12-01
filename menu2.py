from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

# Menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

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
        wait(10)
    
    # Wait for the button to be released
    while hub.buttons.pressed():
        wait(10)

    # Check which button was pressed
    if Button.CENTER in pressed:
        # Center button confirms the selection and starts the program
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
            import Run_6_Sending_the_Samples
        elif selected == "7":
            import Run_7_Mission_15_and_Delivering_the_Shark_6
        elif selected == "8":
            import Run_8_whale_dot_py_taste_good
        elif selected == "9":
            import Run_9_11192024_Scuba_Diver
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
