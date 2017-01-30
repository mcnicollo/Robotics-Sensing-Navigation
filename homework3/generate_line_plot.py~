import sys
import lcm
import matplotlib.pyplot as plt

from exlcm import gps_data

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

lat_list = []
long_list = []


for event in log:
    if event.channel == "GPS":
        msg = gps_data.decode(event.data)
	lat_list.append(msg.latitude)
	long_list.append(msg.longitude)


plt.plot(lat_list,long_list,'-o')
plt.axis([min(lat_list),max(lat_list),min(long_list),max(long_list)])
plt.show()
