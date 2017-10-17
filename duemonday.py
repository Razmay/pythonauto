#from bbpystepper import Stepper
#find battety cord and solder cord to connect to H Bridge 
# connect GND of H bridge to beaglebone

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
#out1 is redwire to motor out2 is black wire to motor out3 is red to other motor
ADC.setup()
# indictorpin
GPIO.setup("P8_15", GPIO.OUT)
#leftmotor
GPIO.setup("P8_11", GPIO.OUT)#in1
GPIO.setup("P8_12", GPIO.OUT)#in2
PWM.start("P8_13",0)#ena

#rightmotor
GPIO.setup("P8_15", GPIO.OUT)#in3
GPIO.setup("P8_16", GPIO.OUT)#in4
PWM.start("P8_19",0)#enb

def forward():
    GPIO.output("P8_11",GPIO.HIGH)
    GPIO.output("P8_15",GPIO.HIGH)
    GPIO.output("P8_12",GPIO.LOW)
    GPIO.output("P8_16",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",50)
    PWM.set_duty_cycle("P8_19",50)
    
def stop():
    GPIO.output("P8_11",GPIO.HIGH)
    GPIO.output("P8_15",GPIO.HIGH)
    GPIO.output("P8_12",GPIO.LOW)
    GPIO.output("P8_16",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",0)
    PWM.set_duty_cycle("P8_19",0)

def back():
    GPIO.output("P8_11",GPIO.LOW)
    GPIO.output("P8_15",GPIO.LOW)
    GPIO.output("P8_12",GPIO.HIGH)
    GPIO.output("P8_16",GPIO.HIGH)
    PWM.set_duty_cycle("P8_13",50)
    PWM.set_duty_cycle("P8_19",50)

def leftforward():
    GPIO.output("P8_11",GPIO.HIGH)
    GPIO.output("P8_12",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",50)

def leftback():
    GPIO.output("P8_11",GPIO.LOW)
    GPIO.output("P8_12",GPIO.HIGH)
    PWM.set_duty_cycle("P8_13",50)

def rightforward():
    GPIO.output("P8_15",GPIO.HIGH)
    GPIO.output("P8_16",GPIO.LOW)
    PWM.set_duty_cycle("P8_19",50)

def rightback():
    GPIO.output("P8_15",GPIO.LOW)
    GPIO.output("P8_16",GPIO.HIGH)
    PWM.set_duty_cycle("P8_19",50)    

 
while 1:
    frontval = ADC.read("P9_40")# ADC ULTRASOUNIC
    backval = ADC.read("P9_39")
    Fvol = frontval *  1.8/0.0064
    Bvol = backval *  1.8/0.0064
    answer = raw_input("what would you like to do:")
    
    if answer =='park':
         forward()
         
         if Fvol,Bvol  <= 300: #foward until distance ping for ultrasonic
             stop()
             time.sleep(.1)
             forward()
             time.sleep(1)#time to travel one car lenght(seconds)
             stop()
             rightback()
             time.sleep(1)#time until 45 degree turn
             stop()
             
             
            
             
             
             
             
             
             
        
        
        
         
         
         
         
    elif answer == 'stop':
         print "ok "
         PWM.stop("P8_13")
         PWM.stop("P8_19")
         PWM.cleanup()
         GPIO.output("P8_10", GPIO.LOW)
         GPIO.output("P8_11", GPIO.LOW)
         GPIO.output("P8_12", GPIO.LOW)
         GPIO.output("P8_15", GPIO.LOW)
         GPIO.output("P8_16", GPIO.LOW)
         GPIO.cleanup()
         break
    elif answer == 'test':
         forward()
         time.sleep(5)
         stop()
         time.sleep(1)
         back()
         time.sleep(5)
         stop()
         time.sleep(1)
         
         
         
        
         
         
         
     
         
         