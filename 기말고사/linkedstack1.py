class Listnode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class linked_stack:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def pop(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            print("Empty!")
            
    def push(self, data):
        stack_node = Listnode(data, self.head)
        stack_node.next = self.head
        self.size += 1
        self.head = stack_node
        
    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else: 
            print("Empty!")
            
    def display(self):
        p = self.head
        
        while p != None:
            print('[%d] -> ' %(p.data), end='')
            p = p.next
            
        print('\b\b\b   ')
        
if __name__ == "__main__":
    a = linked_stack()
    a.push(12)
    a.display()
    a.push(2)
    a.display()
    a.push(3)
    a.display()
    
    print(a.peek())
    print(a.pop())
    
    a.push(31)
    a.display()
    
    
