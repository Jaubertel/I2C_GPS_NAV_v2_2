I2C_GPS_NAV_v2_2
================

1. Better sonar support
2. Optical flow sensor

LED
---
- start up
two blinks: optical flow sensor detected
three blinks: serial traffic detected
five blinks: both serial and optical flow sensor detected

- running time
one blink every two seconds: no valid gps frame in last five seconds, could be checksum/baudrate/config error
one blick every one second: no gps fix in last five seconds
two blink every one second: 2d fix
three blink every one second: 3d fix

