from Listnode import Listnode

class ListType:
    def __init__(self):
         self.head = None
         self.size = 0
         
    def isEmpty(self):
         return self.head == None
     
     #insertLast가 필요한 조건은 TailPointer가 존재할 경우
     #다만 단순연결 리스트에서는 insertLast가 의미가 없음
     #원형 연결 리스트에서는 insertFirst와 insertLast가 모두 의미가 있음. 
     
    def insertFirst(self, data):
         node = ListNode(data, self.head)
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
                
                node = ListNode(data, p.next)
                p.next = node
                self.size += 1
            else:
                print('Invalid Position')
                
    def display(self):
        p = self.head
        
        while p != None:
            print('[%s] -> ' %(p.data), end='')
            p = p.next
        
        print('\b\b\b   ')
        
if __name__ == "__main__":
    L = ListType()
    
    L.insertFirst('A'); L.insertFirst('B'); L.display()
    L.insert(2, 'C'); L.insert(1, 'D'); L.insert(5, 'E'); L.display()
    L.insert(7, 'E')
     
     