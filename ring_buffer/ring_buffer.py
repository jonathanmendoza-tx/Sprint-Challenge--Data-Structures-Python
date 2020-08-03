class RingBuffer:
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.storage = []
    	self.last_index = 0

    def append(self, item):
    	if len(self.storage) < self.capacity:
    		self.storage.append(item)
    		self.last_index += 1

    	else:
    		if self.last_index == self.capacity:
    			self.last_index = 0

    		self.storage[self.last_index] = item

    		self.last_index += 1
        

    def get(self):
        return self.storage