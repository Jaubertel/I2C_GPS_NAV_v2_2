#!/usr/bin/env python

# Simple script to setup UBLOX NEO 6M GPS to use with I2C_NAV

import serial
import string
import math
import time
import sys

comPort = '/dev/tty.usbserial-DUT-01'  #default com port
comPortBaud = 38400
#comPortBaud = 57600
#comPortBaud = 9600 

init = False 
init = True

save = False
save = True

prog = \
'\xB5\x62\x06\x01\x03\x00\xF0\x05\x00\xFF\x19' + \
'\xB5\x62\x06\x01\x03\x00\xF0\x03\x00\xFD\x15' + \
'\xB5\x62\x06\x01\x03\x00\xF0\x01\x00\xFB\x11' + \
'\xB5\x62\x06\x01\x03\x00\xF0\x00\x00\xFA\x0F' + \
'\xB5\x62\x06\x01\x03\x00\xF0\x02\x00\xFC\x13' + \
'\xB5\x62\x06\x01\x03\x00\xF0\x04\x00\xFE\x17' + \
'\xB5\x62\x06\x01\x03\x00\x01\x02\x01\x0E\x47' + \
'\xB5\x62\x06\x01\x03\x00\x01\x03\x01\x0F\x49' + \
'\xB5\x62\x06\x01\x03\x00\x01\x06\x01\x12\x4F' + \
'\xB5\x62\x06\x01\x03\x00\x01\x12\x01\x1E\x67' + \
'\xB5\x62\x06\x16\x08\x00\x03\x07\x03\x00\x51\x08\x00\x00\x8A\x41' + \
'\xB5\x62\x06\x08\x06\x00\xC8\x00\x01\x00\x01\x00\xDE\x6A'

save_to_epprom = '\xB5\x62\x06\x09\x0D\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x04\x1E\xAC'

save_to_all_devices = '\xB5\x62\x06\x09\x0D\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x17\x31\xBF'

ser = None
try:
    ser = serial.Serial(port=comPort,baudrate=comPortBaud, timeout=0.1)
    print("Serial port '" + comPort + "' opened!")

    if init:

        if save:
            #prog += save_to_epprom
            prog += save_to_all_devices

        print 'Initialze UBLOX GPS ...'
        time.sleep(0.2)
        for c in prog:
            #print 'Sending 0x%02x ...' % ord(c)
            ret = 0
            while (ret != 1):
                time.sleep(0.005)
                ret = ser.write(c)

        ser.write("$PUBX,41,1,0003,0001,38400,0*26\r\n")
        #ser.write("$PUBX,41,1,0003,0001,57600,0*2D\r\n")
        print 'Done!'

    print 'Reading ...'
    while True:
        if( ser.isOpen() ):
            while( ser.inWaiting() > 0 ):
                line = ser.read()
                sys.stdout.write(line)

except serial.SerialException, e:
    print("Failed to open serial port '" + comPort + "'")
    print e
    if( ser is not None and ser.isOpen() ):
        ser.close()

if( ser is not None and ser.isOpen() ):
    ser.close()

