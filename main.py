import RPi.GPIO as GPIO
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

# Function to move motor forward
def move_forward(speed):
    print(f"Moving forward with speed: {speed}")
    GPIO.output(R_EN, GPIO.HIGH)
    GPIO.output(L_EN, GPIO.LOW)
    pwm_forward.start(speed)
    pwm_backward.stop()

# Function to move motor backward
def move_backward(speed):
    print(f"Moving backward with speed: {speed}")
    GPIO.output(R_EN, GPIO.LOW)
    GPIO.output(L_EN, GPIO.HIGH)
    pwm_forward.stop()
    pwm_backward.start(speed)

# Function to stop motor
def stop_motor():
    print("Stopping motor")
    GPIO.output(R_EN, GPIO.LOW)
    GPIO.output(L_EN, GPIO.LOW)
    pwm_forward.stop()
    pwm_backward.stop()

try:
    while True:
        command = input("Enter command (f: forward, b: backward, s: stop, q: quit): ").lower()
        if command == 'f':
            speed = int(input("Enter speed (0-100): "))
            move_forward(speed)
        elif command == 'b':
            speed = int(input("Enter speed (0-100): "))
            move_backward(speed)
        elif command == 's':
            stop_motor()
        elif command == 'q':
            break
        else:
            print("Invalid command")
finally:
    stop_motor()
    GPIO.cleanup()
