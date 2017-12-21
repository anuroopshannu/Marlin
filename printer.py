import os
import time
from Printrun.printrun.printcore import printcore
from Printrun.printrun import gcoder
import random
import time
import sys
#import iothub_client_python
from azure_iot_sdks.python.device.samples.iothub_client import *
from azure_iot_sdks.python.device.samples.iothub_client_args import *
import azure_iot_sdks.python.device.samples.iothub_client_sample as ics

def receive_from_cloud():
	 ics.iothub_client_sample_run_receive()
         
        
	

def download_stl_from_cloud(url,stl_file):
	os.system('sudo wget '+url+' -O '+stl_file)
	time.sleep(30)
        stl_to_gcode(stl_file,op_file)

def stl_to_gcode(stl_file,op_file):
	os.system('sudo slic3r '+stl_file+' '+'--layer-height 0.2 --output '+op_file)
	time.sleep(30)
        #print_gcode(op_file)

def print_gcode(op_file):
	p=printcore('/dev/ttyUSB2',250000) 
	gcode=[i.strip() for i in open(op_file)] 
	gcode = gcoder.LightGCode(gcode)
	p.startprint(gcode) 
	p.disconnect() 

stl_file='input.stl'
op_file='output.gcode'
url='https://storekmit.blob.core.windows.net/blobcontainer/STLFile'

receive_from_cloud()



