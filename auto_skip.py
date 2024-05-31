from PIL import ImageGrab
import time
import keyboard
import vgamepad as vg
import json
import pathlib

gamepad = vg.VX360Gamepad()

def check_colors_in_screenshot(colors_to_check, x_percentage, y_percentage, width, height):
    screen_width, screen_height = ImageGrab.grab().size

    x = int(screen_width * x_percentage)
    y = int(screen_height * y_percentage)
    bbox = (x, y, x + width, y + height)

    screenshot = ImageGrab.grab(bbox)

    pixels = list(screenshot.getdata())

    for color in colors_to_check:
        if color in pixels:
            return True

    return False

colors_to_check = [(57, 181, 74), (43, 235, 0)]

x_percentage = 0.53
y_percentage = 0.16
width = 15
height = 15

delay = 0.03

def default_press():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
    time.sleep(delay)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
    time.sleep(delay)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()

def party_press():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()
    time.sleep(delay)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    time.sleep(delay)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    time.sleep(delay)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    gamepad.update()

while True:
    pixel_pos = check_colors_in_screenshot(colors_to_check, x_percentage, y_percentage, width, height)

    if keyboard.is_pressed('ctrl+q'):
        quit()

    if pixel_pos:
        with open(f'{pathlib.Path(__file__).parent.resolve()}\\config.json', 'r') as json_file:
            config = json.load(json_file)

        if config["PizzaParty"] == "True":
            party_press()
        else:
            default_press()

        print("Color found")
        time.sleep(15)
    else:
        print("Color not found")