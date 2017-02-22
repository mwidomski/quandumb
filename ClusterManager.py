import threading
import socket
import select
import Connector
import mem_share as MemShare

class ClusterManager:
    filename = "config.config"

    def __init__(self):
        print("debug: clusterManager created")

    def createConnectors(self):
        configfile = open(self.filename, "r")
        connectorList = []
        
        while True:
            sliceAddress = configfile.readline()
            if sliceAddress == "":
                break
            sliceIp, slicePort = sliceAddress.split(":")
            connectorList.append(Connector(sliceIp,int(slicePort)))
        return connectorList
            
    def main(self):
        #read config file and parse slice's ip and port
        connectorList = self.createConnectors()

        #set up the shared memory
        memShare = MemShare()

        #read from memshares to connectors
        slices = memShare.make_slices(len(connectorList))

        for i in range(len(connectorList)):
            connectorList[i].send_slice(slices[i])

        #read from connectors to memshare
        for i in range(len(connectorList)):
            memShare.set_chunk(connectorList[i].get_slice())

ClusterManager().main()
