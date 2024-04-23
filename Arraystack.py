class Arraystack:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('StackOverFlow')
        
    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('Empty!')
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty!')
    # 재귀함수를 통한 스택 정렬
    # 시험 전에 무조건 한 번은 보고 들어갈 것
    def sortedPush(self, e):
        if(self.isEmpty() or e > self.peek()):
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)
            
    def display(self):
        print(self.stack[:self.top+ 1])
        

if __name__ == '__main__':
    
    S = Arraystack(10)
    
    data = [5, 3, 8, 1, 2, 7]
    
    for d in data:
        S.sortedPush(d)
        S.display()
    
    print(S.pop())
    S.display()
    
    print(S.peek())
    S.display()