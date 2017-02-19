import sys
import lcm

from exlcm import gps_data

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

for event in log:
    if event.channel == "GPS":
        msg = gps_data.decode(event.data)

        print("Message:")
        print("   timestamp   = %s" % str(msg.timestamp))
        print("   latitude    = %s" % str(msg.latitude))
        print("   longitude = %s" % str(msg.longitude))
        print("   altitude   = %s" % str(msg.altitude))
        print("   utm_x    = %s" % str(msg.utm_X))
        print("   utm_y = %s" % str(msg.utm_y))

        print("")
