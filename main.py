import os
import time
from Printrun.printrun.printcore import printcore
from Printrun.printrun import gcoder
import random
import time
import sys
from pubnub import Pubnub


pubnub = Pubnub(publish_key="pub-c-ca28baa7-6cad-4d4a-be94-c5c734a2a66a", subscribe_key="sub-c-cbcf32a6-1f74-11e7-bd07-02ee2ddab7fe")


def download_gcode(message, channel):
    print(message)
    os.system('sudo wget '+message+' -O '+'sample.gcode')
    time.sleep(30)
    print_gcode('sample.gcode')
    
def print_gcode(op_file):
	print('preparing file for print')
	p=printcore('/dev/ttyUSB0',250000)
	print('conected to printer successfully') 
	gcode=[i.strip() for i in open(op_file)] 
	gcode = gcoder.LightGCode(gcode)
	p.startprint(gcode) 
	#p.disconnect() 
  
  
def error(message):
    print("ERROR : " + str(message))
  
def receive_from_cloud(channel):
	pubnub.subscribe(channels=channel, callback=download_gcode, error=error)


receive_from_cloud('my_channel')
