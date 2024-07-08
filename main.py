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
GPIO.setup(L_EN, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)


# Enable "Left" and "Right" movement on the HBRidge
GPIO.output(R_EN, True)
GPIO.output(L_EN, True)

rpwm= GPIO.PWM(RPWM, 100)
lpwm= GPIO.PWM(LPWM, 100)

rpwm.ChangeDutyCycle(0)
rpwm.start(0)

while 1:

  for x in range(100):
    print("Speeding up " + str(x))
    rpwm.ChangeDutyCycle(x)
    time.sleep(0.25)

  time.sleep(5)

  for x in range(100):
    print("Slowing down " + str(x))
    rpwm.ChangeDutyCycle(100-x)
    time.sleep(0.25)