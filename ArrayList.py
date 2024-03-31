class ArrayList:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else:
            print('Overflow Or Invalid Position')
            
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def findItem(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        
        return -1
        
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print('Underflow Or Invalid Position')
            
    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e
            
        else:pass
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        
        else:None
            
if __name__ == "__main__":
    L1 = ArrayList(50)
    L1.insert(0, 10)
    L1.insert(0, 20)
    L1.insert(1, 30)
    
    
    print(L1.delete(0))
    L1.display()
    
    
        
    
        