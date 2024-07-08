import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

R_EN = 21
L_EN = 22
RPWM = 23
LPWM = 24

GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)

# Initialize PWM
pwm_forward = GPIO.PWM(RPWM, 1000)  # Set frequency to 1kHz
pwm_backward = GPIO.PWM(LPWM, 1000)  # Set frequency to 1kHz

GPIO.output(R_EN, GPIO.HIGH)
GPIO.output(L_EN, GPIO.LOW)

pwm_forward.start(100)
pwm_backward.stop()