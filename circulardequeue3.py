from CircularQueue import *
class circulardequeue(CircularQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)
        
    def isEmpty(self):
        return super().isEmpty()
    
    def isFull(self):
        return super().isFull()
    
    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
    def addRear(self, e):
        self.enqueue(e)
        
    def deleteFront(self):
        self.dequeue()
    
    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity 
            return e
        
    def getFront(self):
        self.peek()
        
    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        
        else:pass
        
if __name__ == "__main__":
    
    import random
    
    DQ = circulardequeue()
    for i in range(4):
        DQ.addFront(random.randint(65, 90))
    DQ.display()
    
    for i in range(4):
        DQ.addRear(random.randint(65, 90))
    DQ.display()
    
    DQ.deleteRear()
    DQ.display()