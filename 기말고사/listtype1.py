class listnode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class listtype:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isempty(self):
        return self.head == None    
    
    def insertFirst(self, data):
        node = listnode(data, self.head)
        self.head = node
        self.size += 1
        
    def getNode(self, pos):
        p = self.head
        
        for i in range(1, pos - 1):
            p = p.next
        
        return p
    
    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
            
        else:
            if(pos <= self.size + 1):
                p = self.getNode(pos)
                node = listnode(data, p.next)
                p.next = node
                self.size += 1
            else:
                print("invalid position")
                
    def deleteFirst(self):
        if not self.isempty():
            p = self.head
            self.head = p.next
            self.size -= 1
            return p.data
        else:
            print("Empty")
            
    def delete(self, pos):
        if not self.isempty():
            if pos == 1:
                self.deleteFirst()
            else:
                if(pos <= self.size):
                    p = self.getNode(pos)
                    p1 = self.getNode(pos-1)
                    p1.next = p.next
                    return p.data
                else:
                    print("invalid data")
        else:
            print("empty!")
            return
        
    def display(self):
        p = self.head
        
        while p!= None:
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        
        print('\b\b\b   ')
                
if __name__ == "__main__":
    L = listtype()
    
    L.insertFirst('A'); L.insertFirst('B'); L.display()
    L.insert(2, 'C'); L.insert(1, 'D'); L.insert(5, 'E'); L.display()
    L.insert(7, 'E')
    print('[%s] is deleted.' % L.deleteFirst()); L.display()
    print('[%s] is deleted.' % L.delete(3)); L.display()