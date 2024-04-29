class CircularQueue:
    
    def __init__(self, capacity = 9):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.queue = [None] * capacity
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity 
            self.queue[self.rear] = e
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        
    def display(self):
        i = self.front
        while i != self.rear:
            i = (i + 1) % self.capacity
            print(self.queue[i], end=' ')
        print()
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front+1) % self.capacity]
    
if __name__ == "__main__":
    
    Q = CircularQueue()
    Q.enqueue('A')
    Q.enqueue('D')
    Q.enqueue('E')
    Q.enqueue('C')
    Q.enqueue('B')
    Q.display()
    print()
    
    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    print('Dequeue --> ', Q.dequeue())
    Q.display()    
    print()
    
    print('Peek --> ', Q.peek())
    Q.display()
    print()
    
    Q.enqueue('G')
    Q.enqueue('T')
    Q.enqueue('M')
    Q.enqueue('P')
    Q.display()
    print()