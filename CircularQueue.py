
class MyCircularQueue:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = self.head
        self.queue = [None]*self.size

    def enqueue(self, value):
        # check if the Queue is full
        if self._isfull():
            return "Queue is full"
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
        else:
            # increment the tail pointer
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = value

    def dequeue(self):
        # check if the queue is empty
        if self._isempty():
            return "Queue is empty"
        elif self.head == self.tail:
            val = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return val
        else:
            # update the head pointer
            val = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return val
        
    def _isfull(self):
        return  (self.tail + 1) % self.size == self.head

    def _isempty(self):
        return (self.head == -1) and (self.tail == -1)
    
    def show(self):
        if self._isempty():
            return "Queue is empty"
        elif self.head <= self.tail:
            return self.queue[self.head:self.tail+1]
        else:
            return self.queue[self.head:] + self.queue[:self.tail+1]
