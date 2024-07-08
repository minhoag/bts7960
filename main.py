import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time

# Pin Definitions
RPWM = 18  # Forward PWM
LPWM = 19  # Backward PWM
R_EN = 20  # Forward Enable
L_EN = 21  # Backward Enable

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)

# Initialize PWM
pwm_forward = GPIO.PWM(RPWM, 1000)  # Set frequency to 1kHz
pwm_backward = GPIO.PWM(LPWM, 1000)  # Set frequency to 1kHz

try:
    GPIO.output(R_EN, GPIO.HIGH)
    GPIO.output(L_EN, GPIO.LOW)
    while True:
        pwm_forward.start(100)
except KeyboardInterrupt:
    pass

pwm_forward.stop()
GPIO.cleanup()