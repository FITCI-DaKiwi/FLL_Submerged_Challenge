from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# Let's offer these menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.

pressed = []
#while True:
#col = hub.colorSensor.color()
 # if col == Color.SENSOR_RED:
  #   import test
  #  elif col == Color.SENSOR_BLUE:
   #  import test2


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
if selected == "1":
    import State_Run_1_Octo_Shipping_lane_complete_12_05
elif selected == "2":
    import State_Run_2_James_collect_all_test_12_05_2024
elif selected == "3":
    import State_Run3_Taotao
elif selected == "4":
    import State_Run4_Taotao
elif selected == "5":
    import State_Run_5_vessel
elif selected == "6":
    import State_Run_6_1214_Whale_Octopie
elif selected == "7":
    import Habitat_Run_LisaFinal_run1_option
elif selected == "8":
    import Run_8_Mission_15_and_Delivering_the_Shark_6
elif selected == "9":
    import Run_9_whale_dot_py_taste_good


