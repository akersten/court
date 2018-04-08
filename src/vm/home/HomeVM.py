import platform, socket, os

from datetime import timedelta
from random import random


def getUptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds)).split(".")[0]

    return uptime_string


class HomeVM:
    time = ""
    hostname = platform.node()
    uptime = ""

    def __init__(self, vall):
        self.time = random()
        self.uptime = getUptime()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.fqdn = socket.getfqdn()

        self.cpu_util = str(round(
            float(os.popen('''grep 'cpu ' /proc/stat | awk '{u=($2+$4)*100/($2+$4+$5)} END {print u }' ''').readline()),
            2))
        tot_m, used_m, free_m = map(str, os.popen('free -t -m').readlines()[-1].split()[1:])

        self.mem_used = used_m
        self.mem_total = tot_m

        self.mem_util = str(round(float(used_m) / float(tot_m) * 100, 2))

        self.top_mems = [list(filter(None, x.split(" "))) for x in
                         os.popen('ps -eo pid,cmd,comm,%mem --sort=-%mem').readlines()[1:6]]
        self.top_cpus = [list(filter(None, x.split(" "))) for x in
                         os.popen('ps -eo pid,cmd,comm,%cpu --sort=-%cpu').readlines()[1:6]]
