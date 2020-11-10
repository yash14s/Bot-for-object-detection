import RPi.GPIO as GPIO
LF=18
LB=23
RF=24
RB=25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.output(LF , 0)
GPIO.output(RF , 0)
GPIO.output(LB, 0)
GPIO.output(RB, 0)
print("Setup done")

while(True):
    key = input()
    if(key=='a' or key=='A'):
        GPIO.output(LF , 0)
        GPIO.output(LB , 0)
        GPIO.output(RF , 1)
        GPIO.output(RB , 0)
        print("Left")

    elif(key=='d' or key=='D'):
        GPIO.output(LF , 1)
        GPIO.output(LB , 0)
        GPIO.output(RF , 0)
        GPIO.output(RB , 0)
        print("Right")

    elif(key=='w' or key=='W'):
        GPIO.output(LF , 1)
        GPIO.output(LB , 0)
        GPIO.output(RF , 1)
        GPIO.output(LB , 0)
        print("Forward")

    elif(key=='s' or key=='S'):
        GPIO.output(LF , 0)
        GPIO.output(LB , 1)
        GPIO.output(RF , 0)
        GPIO.output(RB , 1)
        print("Reverse")
    
    elif(key=='q' or key=='Q'):
        print("Quit")
        break

    else:
        GPIO.output(LF , 0)
        GPIO.output(LB , 0)
        GPIO.output(RF , 0)
        GPIO.output(RB , 0)
        print("Stop")






