from ListNode import ListNode

class LinkedStack:
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
        Stack_node = ListNode(data, self.head)
        Stack_node.next = self.head
        self.size += 1
        self.head = Stack_node
        
    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("Empty!")
            
    def display(self):
        p = self.head
        
        while p != None:
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        
        print('\b\b\b   ')

if __name__ == "__main__":
    a = LinkedStack()
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
    
    