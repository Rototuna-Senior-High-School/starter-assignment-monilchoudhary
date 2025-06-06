import board
import digitalio


blue_led = digitalio.DigitalInOut(board.GP1)
blue_led.direction = digitalio.Direction.OUTPUT

red_led = digitalio.DigitalInOut(board.GP0)
red_led.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP15)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

while True:
    if button1.value is False:
        blue_led.value = False
        red_led.value = True

    elif button1.value is True:
        blue_led.value = True
        red_led.value = False
