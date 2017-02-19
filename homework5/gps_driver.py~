#!/usr/bin/env python
# -*- coding: utf-8 -*-
# for USB GPS

import sys
import lcm
import time
import serial
import utm
from exlcm import gps_message


class Gps(object):
    def __init__(self, port_name):
        self.port = serial.Serial(port_name, 4800, timeout=2.)  # 9600-N-8-1
        self.lcm = lcm.LCM()
	self.packet = gps_message()
        while True:
            print 'GPS: Initialization'
            line = self.port.readline()
            try:
	        vals = line.split(",")
            except:
                vals = 0
            if len(vals) == 0:
                time.sleep(0.2)
                self.port.flush()
            else:
                break

    def readloop(self):
        while True:
            	line = self.port.readline()
            #try:
		vals = line.split(',')
		if vals[0] == "$GPGGA":


			self.packet.timestamp = int(vals[1])
			self.packet.latitude = float(vals[2])
			self.packet.longitude = float(vals[4])
			self.packet.altitude = float(vals[9])
			if vals[3] == "S" :
				self.packet.latitude = -1 * self.packet.latitude
			if vals[5] == "W" :
				self.packet.longitude = -1 * self.packet.longitude
			utm_coordinates = utm.from_latlon(self.packet.latitude/100, self.packet.longitude/100)
			self.packet.utm_X = float(utm_coordinates[0])
			self.packet.utm_y = float(utm_coordinates[1])

			print("timestamp: ", self.packet.timestamp)
		
			self.lcm.publish("GPS", self.packet.encode())
		
		else:
			line = 1
            #except:
                #print 'ERROR (' + line + ')'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s <serial_port>\n" % sys.argv[0]
        sys.exit(0)
    mygps = Gps(sys.argv[1])
    mygps.readloop()
