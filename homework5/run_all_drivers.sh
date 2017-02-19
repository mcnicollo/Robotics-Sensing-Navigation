#!bin/bash
IMU_Port=/dev/ttyUSB1
GPS_Port=/dev/ttyUSB0
export DISPLAY=:0
make
make lcm-spy
pushd ../lcm-spy/
./runspy.sh &
popd
sudo gps_driver.py ${GPS_Port} &
sudo imu_driver.py ${IMU_Port} & 
lcm-logger logs/imu_gps_log -i
