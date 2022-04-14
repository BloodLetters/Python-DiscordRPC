import sys
import datetime

def getSecond():
    now = datetime.datetime.now()
    return str(now.second)

def getMinute():
    now = datetime.datetime.now()
    return str(now.minute)

def getHour():
    now = datetime.datetime.now()
    return str(now.hour)
