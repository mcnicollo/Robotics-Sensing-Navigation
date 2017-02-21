import sys
import lcm
import csv
import matplotlib.pyplot as plt
import numpy as np

from scipy import integrate
from exlcm import gps_message
from exlcm import imu_message

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)
log = lcm.EventLog(sys.argv[1], "r")
imucount = 0
gpscount = 0
time = []
accx = []
accy = []
magy = []
magx = []
gyroz = []

for event in log:
    if event.channel == "GPS_Channel":
#	try:
        msg = gps_message.decode(event.data)
        imucount = imucount + 1

    elif event.channel == "IMU":
        msg = imu_message.decode(event.data)
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
	time.append(msg.timestamp)
	accx.append(msg.accelx)
	accy.append(msg.accely)
	magy.append(msg.magy)
	magx.append(msg.magx)
	gyroz.append(msg.gyroz)

	gpscount = gpscount + 1


velocity = integrate.cumtrapz(accx, time,initial=0)
#displacement = integrate.cumtrapz(velocity, time, initial = 0)

nmagy = []
for num in magy:
    nmagy.append(num * -1)

# get yaw data
correctedyaw = np.arctan2(nmagy, magx)
integratedyaw = integrate.cumtrapz(gyroz, time, initial = 0)

# use low pass filter
yaw = 0.98 * integratedyaw + 0.02*correctedyaw

wx = correctedyaw * velocity

comparison = yaw - wx
print(wx)

#print(integratedyaw)

#plt.plot(time, data, 'ro')

#plt.show()


