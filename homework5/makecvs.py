import sys
import lcm
import csv

from exlcm import gps_message
from exlcm import imu_message

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

imucount = 0
gpscount = 0

data = []
time = []
magx = []
magy = []

for event in log:
#    print(event.channel)
    if event.channel == "GPS_Channel":
	#print(event.channel)
#	try:
        msg = gps_message.decode(event.data)

            #print("Message:")
            #print("   timestamp   = %s" % str(msg.timestamp))
      	    #print("   gpstime    = %s" % str(msg.gpstime))
            #print("   latitude    = %s" % str(msg.latitude))
            #print("   longitude = %s" % str(msg.longitude))
            #print("   altitude   = %s" % str(msg.altitude))
            #print("   easting    = %s" % str(msg.easting))
            #print("   northing = %s" % str(msg.northing))
        imucount = imucount + 1
            #print("")

 #       except:

#	    print("Did not work")
    elif event.channel == "IMU":
        #print(event.channel)
        msg = imu_message.decode(event.data)
        #print("Message:")
        #print("   timestamp   = %s" % str(msg.timestamp))
        #print("   yaw    = %s" % str(msg.yaw))
        #print("   pitch    = %s" % str(msg.pitch))
        #print("   roll = %s" % str(msg.roll))
        #print("   magx   = %s" % str(msg.magx))
        #print("   magy    = %s" % str(msg.magy))
        #print("   magz = %s" % str(msg.magz))
        #print("   accelx   = %s" % str(msg.accelx))
        #print("   accely    = %s" % str(msg.accely))
        #print("   accelz = %s" % str(msg.accelz))
        #print("   gyrox   = %s" % str(msg.gyrox))
        #print("   gyroy    = %s" % str(msg.gyroy))
        #print("   gyroz = %s" % str(msg.gyroz))
	magx.append(msg.magx)
	magy.append(msg.magy)
	data.append(msg.accelx)
	time.append(msg.timestamp)

	gpscount = gpscount + 1

with open('magx.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(magx)
with open('magy.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(magy)

print("Total imu points: " + str(imucount))
print("Total gps points: " + str(gpscount))
