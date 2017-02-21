#!/usr/bin/env python
# -*- coding: utf-8 -*-
# for VectorNav IMU sensor

import sys
import lcm
import time
import serial
import utm

from exlcm import imu_message
#import imu_message

class IMU(object):
        def __init__(self, port_name):
                self.port = serial.Serial(port_name, 115200, timeout=1.)
                print 'Connected to:'+ self.port.portstr

                self.lcm = lcm.LCM("udpm://?ttl=1")
                self.packet = imu_message()
                print 'IMU: Initializing IMU'
		time.sleep(2)
		self.port.write('$VNTAR*5F\n')
		time.sleep(2)
		print 'Initialization complete, IMU tared'


        def readloop(self):
                while True:
                        line = self.port.readline()
                        while not line.startswith('$VNYMR'):
                                line = self.port.readline()
			try:
				print(line)
                        	yawst, pitchst, rollst, magxst, magyst, magzst, accelxst, accelyst, accelzst, gyroxst, gyroyst, gyrozst = line.replace('$VNYMR','').strip().split('*')[0].split(',')[1:13]

        	                self.packet.yaw = float(yawst)
	                        self.packet.pitch = float(pitchst)
                	        self.packet.roll = float(rollst)
                        	self.packet.magx = float(magxst)
                        	self.packet.magy = float(magyst)
                        	self.packet.magz = float(magzst)
                        	self.packet.accelx = float(accelxst)
				self.packet.accely = float(accelyst)
				self.packet.accelz = float(accelzst)
				self.packet.gyrox = float(gyroxst)
				self.packet.gyroy = float(gyroyst)
				self.packet.gyroz = float(gyrozst)
                        	self.lcm.publish("IMU", self.packet.encode())
			except:
				print("Data failed for some reason")
#           except:
#                 print 'GPS ERROR (' + line + ')'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s <serial_port>\n" % sys.argv[0]
        sys.exit(0)
    myimu = IMU(sys.argv[1])
    myimu.readloop()


