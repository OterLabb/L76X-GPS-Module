# -*- coding:utf-8 -*-

import time
import l76x
import time
import math
from parsedata import *


x=l76x.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Set_Baudrate(115200)

x.L76X_Send_Command(x.SET_POS_FIX_400MS);

#Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

time.sleep(2)
x.L76X_Exit_BackupMode();
x.L76X_Send_Command(x.SET_SYNC_PPS_NMEA_ON)

#x.L76X_Send_Command(x.SET_STANDBY_MODE)
#time.sleep(10)
#x.L76X_Send_Command(x.SET_NORMAL_MODE)
#x.config.StandBy.value(1)
#print(x.data)
#print(dir(x))
while (1):
    oter = x.L76X_Gat_GNRMC()
    #print(oter)
    str2 = oter.decode('UTF-8').splitlines() # returns a list having splitted elements
    #print(str2)
    for i in range(0,len(str2)):
        #print(str2[i])
        str3 = str2[i].split(',')
        #print(str3[0])
        #print(i)
        ID = str3[0].replace('$','')
        Data = str3[1:]
            
        '''if str3[0] == '$GNZDA':
            gpsTime = str3[1]
            gpsDay = str3[2]
            gpsMonth = str3[3]
            gpsYear = str3[4]
        if str3[3] == '$GNGGA':
            latitude = str3[1]'''
        if ID == 'GNZDA':
            newdata = parseGNZDA(ID,Data)
        elif ID == 'GNRMC':
            newdata2 = parseGNRMC(ID,Data)
        else:
            newdata = 'not gnzda'
            newdata2 = 'not gnrmc'
            
        #newdata = parseNMEA(ID,Data)
    print(newdata)
    print(newdata2)
    print(time.time())
    print()
    #print('Year: {} Month: {} Day: {} Time: {}'.format(gpsYear,gpsMonth,gpsDay,gpsTime))
    #print('Latitude: {}'.format(latitude))
    #print(ID, Data)
    if len(str2) > 5:
        print('Long one', len(str2))
    time.sleep(5)
