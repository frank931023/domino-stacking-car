import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# left motor pins
IN1 = 17
IN2 = 18

# right motor pins
IN3 = 22
IN4 = 23

# domino servo pins
IN5 = 2
IN6 = 3
ENA = 4

# IR sensor pin
# IR = 8

GPIO.setup([IN1, IN2, IN3, IN4, IN5, IN6, ENA], GPIO.OUT)
# GPIO.setup(IR, GPIO.IN)

pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

domino_active = False

def forward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def backward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def turnLeft():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def turnRight():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    
def dominoRun():
    global domino_active
    domino_active = True
    GPIO.output(IN5, True)
    GPIO.output(IN6, False)
    pwm.ChangeDutyCycle(50)
        
def dominoStop():
    global domino_active
    domino_active = False
    GPIO.output(IN5, False)
    GPIO.output(IN6, False)
    pwm.ChangeDutyCycle(0)

# def obstacleDetected():
#     return GPIO.input(IR) == 0

def cleanup():
    stop()
    GPIO.cleanup()
