import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# left motor pins
IN1 = 17
IN2 = 18
EN_LEFT = 5

# right motor pins
IN3 = 22
IN4 = 23
EN_RIGHT = 6

# domino servo pins
IN5 = 2
IN6 = 3
ENA = 4

# IR sensor pin
# IR = 8

GPIO.setup([IN1, IN2, IN3, IN4, IN5, IN6, ENA, EN_LEFT, EN_RIGHT], GPIO.OUT)
# GPIO.setup(IR, GPIO.IN)

pwm_domino = GPIO.PWM(ENA, 1000)
pwm_domino.start(0)
pwm_left_motor = GPIO.PWM(EN_LEFT, 1000)
pwm_left_motor.start(0)
pwm_right_motor = GPIO.PWM(EN_RIGHT, 1000)
pwm_right_motor.start(0)

chassis_speed = 40
domino_active = False

def backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwm_left_motor.ChangeDutyCycle(chassis_speed)
    pwm_right_motor.ChangeDutyCycle(chassis_speed)

def forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwm_left_motor.ChangeDutyCycle(chassis_speed)
    pwm_right_motor.ChangeDutyCycle(chassis_speed)

def turnRight():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwm_left_motor.ChangeDutyCycle(chassis_speed)
    pwm_right_motor.ChangeDutyCycle(chassis_speed)

def turnLeft():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwm_left_motor.ChangeDutyCycle(chassis_speed)
    pwm_right_motor.ChangeDutyCycle(chassis_speed)

def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    pwm_left_motor.ChangeDutyCycle(0)
    pwm_right_motor.ChangeDutyCycle(0)
    
def dominoRun():
    global domino_active
    domino_active = True
    GPIO.output(IN5, True)
    GPIO.output(IN6, False)
    pwm_domino.ChangeDutyCycle(50)
        
def dominoStop():
    global domino_active
    domino_active = False
    GPIO.output(IN5, False)
    GPIO.output(IN6, False)
    pwm_domino.ChangeDutyCycle(0)

# def obstacleDetected():
#     return GPIO.input(IR) == 0

def cleanup():
    stop()
    GPIO.cleanup()

    
