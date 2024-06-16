class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedCircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def isEmpty(self):
        return self.tail == None
    
    def enqueue(self, data):
        node = Node(data, None)
        # 노드가 혼자일 때 insert or delete 하면 빈 노드가 되는데 여기서 insert를 해서 잘 되면 ok
        # 과제할 때 확인해야할 부분
        
        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
            # 새로 들어온 노드가 self.tail이 갖고 있던 다음 노드의 주소를 받아오고, 
            # 내 전에 있던 노드, 즉 self.tail의 다음 노드 값이 현재 새로 생긴 노드로 변경
            # 마지막으로 tail의 본체를 node로 옮겨준다
        self.size += 1
        
    def dequeue(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next
            data = q.data
            if p == q:
                self.tail == None
            else:
                p.next = q.next
            self.size -= 1
            return data
        else:
            print('No Element')            
        
    def display(self):
        if self.isEmpty():
            print('No Element')
            return
        
        p = self.tail.next #첫번째 노드를 가리킴
        for i in range(self.size):
            print('[%s] -> ' %p.data, end='')
            p = p.next
            
        print('\b\b\b   ')
    
if __name__ == "__main__":
    Q = LinkedCircularQueue()
    Q.enqueue('A'); Q.display()
    Q.enqueue('C'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('D'); Q.display()
    Q.dequeue(); Q.display()
    print('[%s] is deleted.' % Q.dequeue()); Q.display()
    