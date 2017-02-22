import subprocess
import os

MEMSLICE_HEADER = 16

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

    def from_bytestream(self,head):
        #TODO - Passback from RayTrace
        return None

    def __init__(self, data = None):
        if data is not None:
            self.data = data
        #else:
         #  from_bytestream(head);

    def to_bytestream(self):
        proc = subprocess.Popen(['python','rayt.py'], stdin=subprocess.PIPE)
        proc.communicate(bytearray(self.data));

MemSlice(bytes("a23","utf-8")).to_bytestream()
