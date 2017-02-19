#!/usr/bin/env python
# -*- coding: utf-8 -*-
# for USB GPS

import sys
import lcm
import time
import serial
import utm
from exlcm import gps_data


class Gps(object):
    def __init__(self, port_name):
        self.port = serial.Serial(port_name, 4800, timeout=2.)  # 9600-N-8-1
        self.lcm = lcm.LCM()
	self.packet = gps_data()
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
			self.packet.lat_bearing = vals[3]
			self.packet.longitude = float(vals[4])
			self.packet.long_bearing = vals[5]
			self.packet.altitude = float(vals[9])
			if self.packet.lat_bearing == "S" :
				self.packet.latitude = -1 * self.packet.latitude
			if self.packet.long_bearing == "W" :
				self.packet.longitude = -1 * self.packet.longitude
			utm_coordinates = utm.from_latlon(self.packet.latitude/100, self.packet.longitude/100)
			self.packet.utm_X = float(utm_coordinates[0])
			self.packet.utm_y = float(utm_coordinates[1])

			print("timestamp: ", self.packet.timestamp)
			print("latitude: ", self.packet.latitude)
			#print("lat_bearing: ",  self.packet.lat_bearing)
			print("longitude: ",  self.packet.longitude)
			#print("long_bearing: ",  self.packet.long_bearing)
			print("altitude: ",  self.packet.altitude)
			print("gps_data: ", self.packet)
			#print("gps_data_encode: ", self.packet.encode())
			print("utm_X", self.packet.utm_X)
			print("utm_y", self.packet.utm_y)
		
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
