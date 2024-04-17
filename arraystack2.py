class ArrayStack:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.top = -1
        self.array=[None] * self.capacity   
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: print('StackOverFlow')
        
    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.top -= 1
            return e
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("empty")
            
    def sortedStack(self, e):
        if not self.isFull() and e > self.peek():
            self.push()
        else:
            tmp = self.pop()
            self.sortedStack(e)
            self.push(tmp)
            
    def display(self):
        return self.array[self.top::-1]          
        