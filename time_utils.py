#
# File created by Leonardo Cencetti on 2/22/2020
#
import time


class TimeSync:
    def __init__(self):
        self.timeDelta = 0
        self.currentTime = 0
        self.latency = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def getCurrentTime(self):
        self.currentTime = time.time()
        return self.currentTime

    def getTimeDelta(self, hostTime, sentTime):
        self.latency = (self.getCurrentTime() - sentTime) / 2
        self.timeDelta = self.currentTime - hostTime - self.latency
        # print('\t\t[Latency]\t', self.latency)
        # print('\t\t[Raw Delta]\t', self.timeDelta)
        return self.timeDelta
