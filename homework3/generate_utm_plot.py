import sys
import lcm
import matplotlib.pyplot as plt

from exlcm import gps_data

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

utm_x_list = []
utm_y_list = []


for event in log:
    if event.channel == "GPS":
        msg = gps_data.decode(event.data)
	utm_x_list.append(msg.utm_X)
	utm_y_list.append(msg.utm_y)


plt.plot(utm_x_list,utm_y_list,'ro')
plt.axis([min(utm_x_list),max(utm_x_list),min(utm_y_list),max(utm_y_list)])
plt.show()
