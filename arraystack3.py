class arraystack:
    def __init__(self):
        self.capacity = 0
        self.top = -1
        self.stack = list(map(int, input().split()))
        
        for i in self.stack:
            self.capacity += 1
        
    def isFull(self):
        return self.top == self.capacity - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print("stackoverflow")
            
    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print("empty!")
            
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        
    def sortedPush(self, e):
        if not self.isFull() or self.peek() < e:
            self.push(e)
        else:
            curr = self.pop()
            self.sortedPush(e)
            self.push(curr)
        
    def display(self):
        for i in self.stack:
            print(i, end=' ')
    

if __name__ == "__main__":
    
    S = arraystack()
    
    S.display()
    print(S.capacity)