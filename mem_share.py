def set_chunk(self, memslice):
    self.buf[memshare.offset:] = memslice.data

def make_slices(self, buf, slice_count):
    slice_size = self.buf.size() / slice_count

    slices = []
    for i in range(slice_count):
        offset = data_start + (slice_size * i)
        head  = {"head_size": SLICE_HEAD_SIZE,
                 "scene_size": self.scene_size,
                 "data_size": slice_size,
                 "offset": offset}
        scene = self.buf[offset:(offset + self.scene_size)]
        data  = self.buf[offset:(offset + slice_size)]
        slices.append(MemSlice(head, scene, data))

    return slices
