def set_chunk(self, memslice):
    self.buf[memshare.offset:] = memslice.data

def make_slices(self, buf, slice_count):
    slice_size = self.buf.size() / slice_count

    slices = []
    for i in range(slice_count):
        offset = data_start + (slice_size * i)
        head  = {"head": SLICE_HEAD_SIZE,
                 "scene": self.scene_size,
                 "data": slice_size,
                 "offset": offset}
        scene = self.buf[offset:(offset + self.scene_size)]
        data  = self.buf[offset:(offset + slice_size)]
        slices.append(MemSlice(head, scene, data))

    return slices

class MemSlice:

    def __init__(self, head, datastream):
        self.head = head
        self.scene = scene
        self.data = datastream

    def to_bytestream:
        byte = bytearray()
        headers = ["head", "scene", "data", "offset"]
        for head in headers:
            byte = byte.join(bytearray(self.head[head]))
        byte = byte.join(bytearray(self.data))
        return byte
