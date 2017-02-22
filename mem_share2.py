import subprocess, os, socket

MEMSLICE_HEADER = 16
SENDIP = 'localhost'
#'192.168.2.20'
#192.168.2.50
SENDPORT = 2001
#2002

def set_chunk(self, buf, memslice):
    buf[memslice.head["offset"]:] = memslice.data

def make_slices(self, buf, static, slice_count):
    slice_size = buf.len / slice_count
    slices = []
    for i in range(slice_count):
        buf_offset = (slice_size * i)
        head  = {"head": MEMSLICE_HEADER,
                 "static": static.len,
                 "data": buf.len,
                 "offset": buf_offset}
        data = buf[offset:(offset + slice_size)]
        slices.append(MemSlice(head, static, data))
    return slices

class MemSlice:

    def from_bytestream(self,out):
        #send recieved bytestream out to cluster manager
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes(out,'utf-8'), (SENDIP, SENDPORT))
        #s.shutdown()
        #s.close()
        

    def __init__(self, data = None):
        while True:
            if data is not None:
                self.data = data
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                print('waiting...')
                s.bind(('', 2001))
                (self.data, addr) = s.recvfrom(4096)
                print('done')
                #s.shutdown()
                #s.close()
                #self.to_bytestream()
                print(self.data)
                s.shutdown(SHUT_RDWR)
                s.close()


    def to_bytestream(self):
        proc = subprocess.Popen(['./RayTrace'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        std_out = proc.communicate(bytearray(self.data))
        self.from_bytestream(repr(std_out))
		
MemSlice()