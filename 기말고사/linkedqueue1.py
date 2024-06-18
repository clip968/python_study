class listnode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class linkedqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.front == None
        
    def enqueue(self, data):
        circularqueue = listnode(data, self.rear)
        
        if self.isEmpty():
            self.front = circularqueue
            self.rear = circularqueue
            self.size += 1
            
        else:
            self.rear.next = circularqueue
            self.rear = circularqueue
            self.size += 1
            
    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            self.size -= 1
        
        if self.front == None:
            self.rear = None
        
        return data
    
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            print('Empty!')
    
    def display(self):
        if self.isEmpty():
            print('EMpty!')
            return
        
        p = self.front
        for i in range(self.size):
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        print('\b\b\b   ')
        
if __name__ == "__main__":
    queue = linkedqueue()
    
    queue.enqueue(2); queue.display()
    queue.enqueue(23); queue.display()
    queue.enqueue(4); queue.display()
    queue.enqueue(5); queue.display()
    queue.enqueue(6); queue.display()
    
    print(queue.dequeue()); queue.display()
    print(queue.dequeue()); queue.display()
    print(queue.peek())
        
        