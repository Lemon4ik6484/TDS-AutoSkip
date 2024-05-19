from PIL import ImageGrab
import time
import keyboard
import vgamepad as vg

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

while True:
    pixel_pos = check_colors_in_screenshot(colors_to_check, x_percentage, y_percentage, width, height)

    if keyboard.is_pressed('ctrl+q'):
        quit()

    if pixel_pos:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        gamepad.update()
        time.sleep(0.03)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        gamepad.update()
        time.sleep(0.03)
        gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)
        gamepad.update()
        time.sleep(0.03)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        time.sleep(0.03)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        gamepad.update()
        time.sleep(0.03)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        gamepad.update()
        print("Color found")
        time.sleep(15)
    else:
        print("Color not found")