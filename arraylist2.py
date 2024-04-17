class ArrayList:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        
    def isFull(self):
        if self.size == self.capacity:
            return True
    
    def isEmpty(self):
        if self.size == 0:
            return True
        
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
    
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
    
    def findItem(self, e):
        if not self.isEmpty():
            for i in range(self.size):
                if e == self.array[i]:
                    return i
                
    def peek(self):
        return self.array[self.size]
                
            