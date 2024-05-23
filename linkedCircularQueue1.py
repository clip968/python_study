from ListNode import *

class LinkedCircularQueue1:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, data):
        CircularQueue = ListNode(data, self.front)
        
        if self.isEmpty():
            self.front = CircularQueue
            self.rear = CircularQueue
        else:
            self.rear.next = self.front
            self.rear = CircularQueue
        
    def dequeue(self, data):
        if not self.