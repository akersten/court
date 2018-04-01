import platform

from datetime import timedelta
from random import random

def getUptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds)).split(".")[0]

    return uptime_string


class MenuVM:
    time = ""
    hostname = platform.node()
    uptime = ""

    vall = ""

    def __init__(self, vall):
        self.time = random()
        self.uptime = getUptime()
        self.vall = vall
