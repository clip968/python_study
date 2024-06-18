class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class linkedcircularqueue:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def isEmpty(self):
        return self.tail == None    
    
    def enqueue(self, data):
        node = Node(data, None)
        
        if self.isEmpty():
            node.next = node
            self.tail = node
            self.size += 1
        
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
            self.size += 1
    
    def dequeue(self):
        if not self.isEmpty():
            p = self.tail
            data = p.next.data
            if p == p.next:
                self.tail == None
                
            else:
                p.next = p.next.next
            
            self.size -= 1
            return data
        else:
            print('Empty!')
            
    def display(self):
        if self.isEmpty():
            print("Empty!")
            return
        
        p = self.tail.next
        for i in range(self.size):
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        
        print('\b\b\b   ')

if __name__ == "__main__":
    Q = linkedcircularqueue()
    Q.enqueue('A'); Q.display()
    Q.enqueue('C'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('D'); Q.display()
    Q.dequeue(); Q.display()
    print('[%s] is deleted.' % Q.dequeue()); Q.display()
            
    