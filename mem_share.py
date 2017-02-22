import posix_ipc
import mmap
import sys
import quandumb

WINDOW_SIZE = 112
HEAD_OFFSET = 32
SLICE_HEAD_SIZE = 16

class MemShare(Object):

    def __init__(self, memory_size = WINDOW_SIZE ):
        self.size = memory_size
        descriptor = posix_ipc.SharedMemory("/tmp/pi_shm", O_CREAT, self.size)
        self.buf = mmap.mmap(self.descriptor.fd, self.descriptor.size)
        descriptor.close
        
        self.head_size = int(self.buf[0:3])
        self.scene_size = int(self.buf[4:7])
        self.data_size = int(self.buf[8:11])
        self.data_start = int(self.head_size + self.scene_size)


    def delete(self):
        if self.buf is not None:
            self.buf.unlink()

    def set_chunk(self, memslice):
        self.buf[memshare.offset:] = memslice.data

    def make_slices(self, slice_count):
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
            slices.append(quandimb.MemSlice(head, scene, data))

        return slices
