import unicornhat as uh #import the necessary modules
import time, random,signal
import catchphrases_uni as cp # the file with our animations
import RPi.GPIO as GPIO
from fuzzywuzzy import fuzz

def halfthing(num,colour): #turns on half the LEDS to indicate who pressed button first
        uh.clear()
        for x in range (num,num+4):
                for y in range(0,8):
                        uh.set_pixel(x,y,colour[0],colour[1],colour[2])
        uh.show()

def  pressed(num): # Function to be run when buttons pressed
        global running
        running = False # stops animaton from playing
        halfthing(num,(255,0,0))
        get_answer(3) # call with goes set to 3
    
def b21pressed(channel): # Run when button on GPIO 21 pressed
        pressed(0)

def b16pressed(channel): # Run when button on GPIO 16 pressed
        pressed(4)

def get_answer(goes): # Asks the player for their answer 
    answer = raw_input('Name that catchphrase? ')
    match = fuzz.ratio(answer, picked) # compare answer to catchphrase title
    if  match >=85:
        print 'Correct!'
    elif match >= 60 and match < 85: # if it nearly matches
        goes=goes-1
        if goes==0:
            print('run out of goes')
        else:
            print 'Close.. Try again (' +( str(goes) + ' guesses remaining)')
            get_answer(goes)
    else:
        print "That's not right"
    print 'Press ^C to exit'

def show_catchphrase():  # Display an animation on the LED matrix
    picked = random.choice(cp.ANSWERS.keys()) # Pick random animation from file
    for i in range(3):
        for x in cp.ANSWERS[picked]:
            if running:
               uh.set_pixels(x) # display a frame from animation
               uh.show()
               time.sleep(0.25) #pause before next frame
        time.sleep(1) # pause before we play animation again
    return picked

GPIO.setmode(GPIO.BCM) #set GPIO numbering to BCM
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set these pins as inputs
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#set callback functions that are run when button pressed
GPIO.add_event_detect(21,GPIO.FALLING,callback = b21pressed,bouncetime=300)
GPIO.add_event_detect(16,GPIO.FALLING,callback = b16pressed,bouncetime=300)
try:
        running = True # use this to stop animation when button pressed
        picked = 'blank'
        picked = show_catchphrase()
        signal.pause() #stops the code from exiting
except KeyboardInterrupt: # catch ^c
        exit() #exit the code
