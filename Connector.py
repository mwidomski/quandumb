import socket
import MemSlice

BUF_SIZE = 1024

class Connector():

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send UDP datagram
    def send_slice(MemSlice chunk):
        self.udpSocket.sendto(chunk.to_bytestream(), (self.ip, self.port))
    
    #receive UDP datagram
    def get_slice():
        return MemSlice.from_bytestream(self.udpSocket.recv(BUF_SIZE))