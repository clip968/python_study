class ArrayList_1:
    
    def __init__ (self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.size == self.capacity:
            return True
        else:
            return False
        
    def delete(self, pos):
        if not self.isFull() and 0 <= pos < self.size:
            e = self.array[pos]
            
            for i in range(pos, self.size):
                self.array[i] = self.array[i+1]
                
            self -= 1
            return e
        
        return print('Error')
    
    def insert(self, pos, e):
        if not self.isEmpty() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.size += 1
            self.array[pos] = e
        
        return print("StackOverflow")
    
    def display(self):
        
        for i in range(self.size):
            print(self.array[i], end=' ')
            
        print()
    
    def findItem(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
            
        return -1
    
    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        
        else:pass
        
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        
        else:None
        
        
            