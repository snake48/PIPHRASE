import threading
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def waiter():
    done = False
    while not done:
        if GPIO.input(21) == 0 or GPIO.input(16)==0:
            print 'pressed'
            done = True

def waiter2():
    print 'bob'
    


GPIO.cleanup()


