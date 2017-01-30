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
        print("   position    = %s" % str(msg.latitude))
        print("   orientation = %s" % str(msg.longitude))
        print("   timestamp   = %s" % str(msg.altitude))
        print("   position    = %s" % str(msg.utm_X))
        print("   orientation = %s" % str(msg.utm_y))

        print("")
