class DlistNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
        
class DlistType:
    def __init__(self):
        self.rear = self.front = None
        self.size = 0
        
    def isempty(self):
        return self.front == self.rear == None
        
    def addFront(self, data):
        node = DlistNode(data, None, self.front)
        
        if self.size == 0:
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
            
        self.size += 1
    
    def addRear(self, data):
        node = DlistNode(data, self.rear, None)
        
        if self.size == 0:
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node
        
        self.size += 1
    
    def getNode(self, pos):
        p = self.front
        
        for i in range(1, pos):
            p = p.next
        
        return p
    
    def addPos(self, pos, data):
        node = DlistNode(data, None, None)
        if pos == 1:
            self.addFront(data)
        elif pos > self.size:
            self.addRear(data)
        else:
            p = self.getNode(pos)
            node.prev = p.prev
            node.next = p
                
            p.prev.next = node
            p.prev = node
                
            self.size += 1
    
    def deleteFront(self):
        if not self.isempty():
            data = self.front.data
            self.front = self.front.next
            
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            
            self.size -= 1
            return data
        else:
            print("empty!")
            
        
    def deleteRear(self):
        if not self.isempty():
            data = self.rear.data
            self.rear = self.rear.prev
            
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            self.size -= 1
            return data
        else:
            print("empty!")
            return None
    
    def deletePos(self, pos):
        if not self.isempty():
            if pos == 1:
                data = self.deleteFront()
                return data
            elif pos == self.size:
                data = self.deleteRear()
                return data
            else:
                p = self.getNode(pos)
                p1 = self.getNode(pos - 1)
                
                data = p.data
                p1.next = p.next
                self.size -= 1
                return data
            
        else:
            print('Empty!')
            return None

    def display(self):
        p = self.front
        
        while p != None:
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        
        print('\b\b\b\b    ')

if __name__ == "__main__":
    DL = DlistType()
    DL.addFront('A'); DL.addFront('B'); DL.display()
    DL.addRear('C'); DL.addRear('D'); DL.display()
    DL.addPos(3, 'E'); DL.display()

    print("[%c] is deleted : " % DL.deleteFront(), end=''); DL.display()
    print("[%c] is deleted : " % DL.deleteRear(), end=''); DL.display()
    print("[%c] is deleted : " % DL.deletePos(3), end=''); DL.display()
