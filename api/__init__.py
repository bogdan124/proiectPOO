#!/usr/bin/env python
from datetime import datetime
import serial
from extern import query
import time

class readDataArduino():

    def __init__(self,port,baud_rate):
        self.ser=serial.Serial(port,baud_rate)

    def readData(self):
        b = self.ser.readline()
        str2 = b.decode()
        self.save = str2.split(" ")
        return self.save

    def getLat(self):
        return self.save[0]

    def getLon(self):
        return self.save[1]

    def getAltitude(self):
        return self.save[2]

    def getSpeedMs(self):
        return self.save[3]

    def getSatelliteNumber(self):
        return self.save[4]

    def getPulse(self):
        return self.save[5]


class sendDbDataGPS():

    def __init__(self,pulse,lat,lon,satellites,speed,altitude,user_id):
        self.pulse=pulse
        self.lat=lat
        self.lon=lon
        self.satellites=satellites
        self.speed=speed
        self.altitude=altitude
        self.date=datetime.today().strftime('%Y-%m-%d')
        self.user_id=1


    def putData(self):
        sql="INSERT INTO user_data(pulse,lat,lon,satellites,speed,altitude,date,user_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        query(sql,"insert",[self.pulse, self.lat,self.lon,self.satellites,self.speed,self.altitude,self.date,self.user_id])

data=readDataArduino("COM5",9600)
while True:
    time.sleep(5)
    data.readData()
    send=sendDbDataGPS(data.getPulse(),data.getLat(),data.getLon(),data.getSatelliteNumber(),data.getSpeedMs(),data.getAltitude(),1)
    send.putData()