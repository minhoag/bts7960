import RPi.GPIO as GPIO
import time

# Pin Definitions
RPWM = 12  # Forward PWM
LPWM = 24  # Backward PWM
R_EN = 21  # Forward Enable
L_EN = 22  # Backward Enable

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)

# PWM Setup
pwm_r = GPIO.PWM(RPWM, 1000)
pwm_l = GPIO.PWM(LPWM, 1000)
pwm_r.start(0)
pwm_l.start(0)

def motor_forward(speed):
    GPIO.output(R_EN, GPIO.HIGH)
    GPIO.output(L_EN, GPIO.LOW)
    pwm_r.ChangeDutyCycle(speed)
    pwm_l.ChangeDutyCycle(0)

def motor_backward(speed):
    GPIO.output(R_EN, GPIO.LOW)
    GPIO.output(L_EN, GPIO.HIGH)
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(R_EN, GPIO.LOW)
    GPIO.output(L_EN, GPIO.LOW)
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

print('Running..')

try:
    while True:
        motor_forward(50)  # Run motor forward at 50% speed
        time.sleep(5)
        motor_stop()
        time.sleep(2)
        motor_backward(50)  # Run motor backward at 50% speed
        time.sleep(5)
        motor_stop()
        time.sleep(2)
except KeyboardInterrupt:
    pass
