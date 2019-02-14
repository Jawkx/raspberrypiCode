import RPi.GPIO as GPIO
import time
import smbus
import time
bus = smbus.SMBus(1)
address = 0x04

GPIO .setmode(GPIO.BCM)
distance = 100
TRIG = 21
ECHO = 20


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def writeNumber(value):
    bus.write_byte(address, value)
    #bus.write_byte(address_2, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    # number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number

stop_distance = input ('Enter stop distance:')
data_list = list('G')

for i in data_list:
    	#Sends to the Slaves 
        writeNumber(int(ord(i)))
	time.sleep(.1)

writeNumber(int(0x0A))

while distance > stop_distance :
        
        GPIO.output(TRIG,True)
        time.sleep(0.0001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == False:
                start = time.time()

        while GPIO.input(ECHO) == True:
                end = time.time()

        sig_time = end - start

        #cm:
        distance = sig_time / 0.000058 

        print('Distance: {} cm'.format(distance))

        
data_list = list('S')

for i in data_list:
    	#Sends to the Slaves 
        writeNumber(int(ord(i)))
	time.sleep(.1)

writeNumber(int(0x0A))
GPIO.cleanup()
