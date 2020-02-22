#
# File created by Leonardo Cencetti on 2/22/2020
#
import threading

import winsound

from time_utils import TimeSync
from udpSocket import UdpSocket


def beep(clock):
    while True:
        if clock.getCurrentTime() % 2 < 0.001:
            T1 = threading.Thread(target=winsound.PlaySound, args=('beep.wav', winsound.SND_ASYNC,))
            T1.start()


def start():
    with UdpSocket(localAddress='0.0.0.0', localPort=20001, bufferSize=1024) as Socket:
        with TimeSync() as pySync:
            # Listen for incoming data
            T1 = threading.Thread(target=beep, args=(pySync,))
            T1.start()
            while True:
                data, addressPair = Socket.recvData()
                if data:
                    timestamp = pySync.getCurrentTime()
                    msgFromServer = {"timestamp": timestamp}
                    Socket.sendData(msgFromServer, addressPair)
                    # Sending a reply to client
                    clientMsg = "[Server] Message from Client: {}".format(data)
                    print(clientMsg)


if __name__ == '__main__':
    start()
