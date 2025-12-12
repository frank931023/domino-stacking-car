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

# GPIO.cleanup()

pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

print("Start running")
GPIO.output(IN1, False)
GPIO.output(IN2, True)
GPIO.output(IN3, True)
GPIO.output(IN4, False)
time.sleep(2)

# GPIO.output(IN5, True)
# GPIO.output(IN6, False)
# pwm.ChangeDutyCycle(50)
# time.sleep(2)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)
GPIO.output(IN5, False)
GPIO.output(IN6, False)

GPIO.cleanup()
print("Testing done")



