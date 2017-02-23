import sys
import lcm
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

from scipy import integrate
from scipy import optimize
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
yaw = []
easting = []
northing = []
gyroz = []

for event in log:
    if event.channel == "GPS_Channel":
#	try:
        msg = gps_message.decode(event.data)
        imucount = imucount + 1
	easting.append(msg.easting)
	northing.append(msg.northing)

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
	time.append(event.timestamp)
	accx.append(msg.accelx)
	accy.append(msg.accely)
	magy.append(msg.magy)
	magx.append(msg.magx)
	gyroz.append(msg.gyroz)
	yaw.append(msg.yaw)

	gpscount = gpscount + 1


basetime = min(time)
realtime = []
for times in time:
	realtime.append(times -basetime)
time = realtime
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


#print(integratedyaw)
modx = []
mody = []
for m in magx:
    #modx.append(m-.005)
    el = m-.005
    ma = math.cos(-0.7) #+ math.sin(-0.7)
    fi = el * ma
    #print(fi)
    #fi = math.sqrt(fi)
    modx.append(fi)

for m in magy:
    #mody.append(m-.255)
    el = m-.255
    ma = 1#(-1 * math.sin(-0.7) + math.cos(-0.7))
    fi = el * ma
    #fi - math.sqrt(fi)
    mody.append(fi)
print('modx min: ' + str(min(modx)))
print('modx max: ' + str(max(modx)))
print('mody min: ' + str(min(mody)))
print('mody max: ' + str(max(mody)))

fig = plt.figure()
gr = fig.add_subplot(111)

#Pre-Calibration mag
#gr.plot(magx, magy, 'ro')
#gr.set_title('Pre-Calibration')
#gr.set_xlabel('MagX')
#gr.set_ylabel('MagY')


#Post-Calibration mag
#gr.plot(modx, mody, 'ro')
#plt.xlim(min(modx),max(modx))
#plt.ylim(min(mody),max(mody))
#gr.set_title('Post-Calibration')
#gr.set_xlabel('MagX')
#gr.set_ylabel('MagY')


#GPS Route
#gr.plot(easting, northing, 'ro')
#gr.set_title('GPS Route')
#gr.set_xlabel('Easting')
#gr.set_ylabel('Northing')


#Yaw from IMU
gr.plot(time, yaw, color = "r")
gr.set_title('IMU Yaw')
gr.set_xlabel('Time')
gr.set_ylabel('Yaw')


#Yaw from IMU VS Calculated
#gr.plot(time, yaw, color = "r")
#gr.plot(time, integratedyaw, color = "b")
#gr.set_title('IMU Yaw vs Calculated Yaw')
#gr.set_xlabel('Time')
#gr.set_ylabel('Yaw')





plt.show()
