#
# File created by Leonardo Cencetti on 2/22/2020
#
import json
import socket

import select


class UdpSocket:
    def __init__(self, localAddress='127.0.0.1', localPort=20001, bufferSize=1024, bind=True):
        self.localAddressPair = (localAddress, localPort)
        self.bufferSize = bufferSize

        self.hasToken = False
        self.sendTimestamp = 0
        self.recvTimestamp = 0

        # Create a datagram socket
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # self.UDPServerSocket.setblocking(True)
        # Bind to address and ip
        if bind:
            self.UDPServerSocket.bind(self.localAddressPair)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def sendData(self, data, targetPair):
        bytesToSend = json.dumps(data).encode()
        self.UDPServerSocket.sendto(bytesToSend, targetPair)

    def recvData(self):
        socketReady = select.select([self.UDPServerSocket], [], [], 10)
        if socketReady[0]:
            bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
            clientMessage = bytesAddressPair[0]
            clientPair = bytesAddressPair[1]
            data = json.loads(clientMessage)
            return data, clientPair
        else:
            return None, None
