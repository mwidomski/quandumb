import Connector

class ClusterManager:
    filename = "config.config"

    def create_connectors(self):
        configfile = open(self.filename, "r")
        connectorList = []
        
        while True:
            sliceAddress = configfile.readline()
            if sliceAddress == "":
                break
            sliceIp, slicePort = sliceAddress.split(":")
            connectorList.append(Connector(sliceIp,int(slicePort)))
        return connectorList
            
    def __init__(self):
        #read config file and parse slice's ip and port
        connectorList = self.create_connectors()
