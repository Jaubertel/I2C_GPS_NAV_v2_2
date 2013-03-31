I2C_GPS_NAV_v2_2
================

1. Better sonar support
2. Optical flow sensor

LED
---
- start up
1. two blinks: optical flow sensor detected
2. three blinks: serial traffic detected
3. five blinks: both serial and optical flow sensor detected

- running time
1. one blink every two seconds: no valid gps frame in last five seconds, could be checksum/baudrate/config error
2. one blick every one second: no gps fix in last five seconds
3. two blink every one second: 2d fix
4. three blink every one second: 3d fix

