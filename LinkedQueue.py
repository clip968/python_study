from Listnode import *

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, data):
        CircularQueue = ListNode(data, self.rear)
        
        if self.isEmpty():
            self.front = CircularQueue
            self.rear = CircularQueue
            self.size += 1
        else:
            self.rear.next = CircularQueue
            self.rear = CircularQueue
            self.size += 1
        
    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            self.size -= 1

        if self.front == None:
            self.rear = None
        
        return data
    
    def display(self):
        if self.isEmpty():
            print('No Element')
            return
        
        p = self.front #첫번째 노드를 가리킴
        for i in range(self.size):
            print('[%s] -> ' %p.data, end='')
            p = p.next
            
        print('\b\b\b   ')
        
if __name__ == "__main__":
    queue = LinkedQueue()
    
    queue.enqueue(2); queue.display()
    queue.enqueue(23); queue.display()
    queue.enqueue(4); queue.display()
    queue.enqueue(5); queue.display()
    queue.enqueue(6); queue.display()
    
    print(queue.dequeue()); queue.display()
    print(queue.dequeue()); queue.display()