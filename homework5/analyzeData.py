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


oyaw = yaw
basetime = min(time)
realtime = []
for times in time:
	realtime.append(times -basetime)
time = realtime
velocity = integrate.cumtrapz(accx, time,initial=0)
#displacement = integrate.cumtrapz(velocity, time, initial = 0)

nmagy = []
for num in magy:
    nmagy.append(num * -1.0)

# get yaw data
correctedyaw = np.arctan2(nmagy, magx)
heading = correctedyaw
integratedyaw = integrate.cumtrapz(gyroz, time, initial = 0)

print("max nmagy: " + str(max(nmagy)))
print("min nmagy: " + str(min(nmagy)))
print("max magy: " + str(max(magy)))
print("mix magy: " + str(min(magy)))
print("max heading: " + str(max(heading)))
print("mix heading: " + str(min(heading)))


# use low pass filter
yaw = 0.98 * integratedyaw + 0.02*correctedyaw
wx = correctedyaw * velocity

# gyro z times x velocity
xvel = integrate.cumtrapz(accx, time, initial = 0)
gzxv = (gyroz * xvel)/10000000




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
#gr.plot(time, yaw, color = "r")
#gr.set_title('IMU Yaw')
#gr.set_xlabel('Time')
#gr.set_ylabel('Yaw')


#Yaw from IMU VS Calculated
#gr.plot(time, yaw, color = "r")
#gr.plot(time, integratedyaw, color = "b")
#gr.set_title('IMU Yaw vs Calculated Yaw')
#gr.set_xlabel('Time')
#gr.set_ylabel('Yaw')


# Problem 1: compare y acceleration vs gyroz times x velocity
#gr.plot(time, gzxv, color = "r")
#gr.plot(time, accy, color = "b")
#gr.set_title('Y Acc Vs. GyroZ*X Velocity')
#gr.set_xlabel('Time')
#gr.set_ylabel('Acceleration')


# Problem 2: 
ev = []
nv = []
xvel = integrate.cumtrapz(accx, time, initial = 0)

noyaw = []
for v in oyaw:
	noyaw.append(-1*v)

for v,head in zip(xvel,noyaw):
	ev.append(v*math.cos(math.radians(head)))
	nv.append(v*math.sin(math.radians(head)))
xcoord = []
ycoord = []
x = 0
y = 0

edis = integrate.cumtrapz(ev, time, initial = 0)
ndis = integrate.cumtrapz(nv, time, initial = 0)

edis2 = []
ndis2 = []
for e,n in zip(edis,ndis):
	e = (e*math.cos(-.5104))-(n*math.sin(-.5104))
	n = (n*math.cos(-.5104))+(e*math.sin(-.5104))
	e = e/(.0786/.0415)
	edis2.append(e)
	ndis2.append(n)


gr.plot(edis2, ndis2, color = "r")
gr.set_title('IMU Path')
gr.set_xlabel('Easting')
gr.set_ylabel('Northing')
plt.show()
