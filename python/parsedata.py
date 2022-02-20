import time

def parseGNZDA(ID, data):
    print('Length of data: {}'.format(len(data)))
    if len(data) != 6:
        gpsTime = NULL
        gpsDay = NULL
        gpsMonth = NULL
        gpsYear = NULL
    elif len(data) == 6:
        gpsTime = ['Time', data[0]]
        gpsDay = ['Day', data[1]]
        gpsMonth = ['Month', data[2]]
        gpsYear = ['Year', data[3]]
    return(gpsTime,gpsDay,gpsMonth,gpsYear)
    
def parseGNRMC(ID, data):
    try:
        print(data)
        print(data[2])
        print(type(data[2]))
        DD = int(float(data[2])/100)
        SS = float(data[2]) - DD * 100
        latitude = DD + SS/60
        
        DD = int(float(data[4])/100)
        SS = float(data[4]) - DD * 100
        longitude = DD + SS/60
    except:
        print('no')
    
    return(latitude,longitude)
        
    
    
    
    
    
def noData(ID,data):
    return('no data')

def parseNMEA(ID,data):
    if ID == 'GNZDA':
        parseGNZDA(ID,data)
    else:
        noData(ID,data)
        #return('no data')


