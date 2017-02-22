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

    def __init__(self, head , static = None, data = None):
        if data is not None:
            self.head = head
            self.static = static
            self.data = datastream
        else:
            from_bytestream(head);

    
    def from_bytestream(self):
        #TODO
        return None

    def to_bytestream(self):
        byte = bytearray()
        headers = ["head", "static", "offset", "data"]
        for head in headers:
            byte = byte.join(bytearray(self.head[head]))
        byte = byte.join(bytearray(self.static))
        byte = byte.join(bytearray(self.data))
        return byte
