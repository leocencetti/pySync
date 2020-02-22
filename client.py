#
# File created by Leonardo Cencetti on 2/22/2020
#
import os
import threading
from time import sleep

from gaussianFilter import GaussianFilter
from time_utils import TimeSync
from udpSocket import UdpSocket

serverAddressPair = ("192.168.2.101", 20001)

tempThread = None


def beep(clock, gFilter):
    while True:

        if (clock.getCurrentTime() - gFilter.mean) % 2 < 0.0001:
            T1 = threading.Thread(target=os.system, args=('play-audio beep.mp3',))
            T1.start()


def start():
    with UdpSocket(bufferSize=1024, bind=False) as Socket:
        with TimeSync() as pySync:
            with GaussianFilter(10) as gFilter:
                T1 = threading.Thread(target=beep, args=(pySync, gFilter,))
                T1.start()
                while True:
                    timestamp = pySync.getCurrentTime()
                    msgFromClient = {"timestamp": timestamp}
                    # Send to server using created UDP socket
                    Socket.sendData(msgFromClient, serverAddressPair)
                    data, addressPair = Socket.recvData()
                    if data:
                        gFilter.update(pySync.getTimeDelta(data['timestamp'], timestamp))
                        # gFilter.mean = pySync.getTimeDelta(data['timestamp'], timestamp)
                        # gFilter.mean = 0
                        print("[Client] Delta: {} s".format(gFilter.mean))

                        sleep(5)


if __name__ == '__main__':
    start()
