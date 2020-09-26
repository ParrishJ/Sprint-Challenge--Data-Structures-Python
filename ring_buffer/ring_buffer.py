class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.pop_order = 0
        self.push_order = 0 

    def append(self, item):
        
        if len(self.storage) == self.capacity:
            self.storage.pop(self.pop_order)
            self.pop_order += 1
            if self.pop_order == self.capacity:
                self.pop_order = 0
            self.storage.insert(self.push_order, item)
            self.push_order += 1
            if self.push_order == self.capacity:
                self.push_order = 0
        #if storage is full, pop oldest item, append new item to front
        else:
            self.storage.append(item)

    def get(self):
        return self.storage


""" rb = RingBuffer(3)
rb.append('a')
rb.append('b')
rb.append('c')
rb.append('d')
rb.append('e')
rb.append('f')
rb.append('g')
rb.append('h')


rb.get() """


    # first in, first out (queue)