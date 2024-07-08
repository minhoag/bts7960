import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

R_EN = 21
L_EN = 22
RPWM = 23
LPWM = 24
# Set all of our PINS to output
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)


# Enable "Left" and "Right" movement on the HBRidge
GPIO.output(R_EN, True)
rpwm= GPIO.PWM(RPWM, 1000)

print("Running...")

try:
    while True:
        rpwm.start(1000)  # duty cycle of 100%
except KeyboardInterrupt:
    print("Key Interrupted")
    pass

rpwm.stop()
GPIO.cleanup()