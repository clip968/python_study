class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DListType:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def addFront(self, data):
        node = DListNode(data, None, self.front)

        if self.size == 0:
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

        self.size += 1


    def addRear(self, data):
        node = DListNode(data, self.rear, None)

        if self.size == 0:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def addPos(self, pos, data):
        node = DListNode(data, None, None)
        # 인덱스는 1부터 시작
        if pos == 1:
            self.addFront(data)
        elif pos > self.size:
            self.addRear(data)
        else:
            p = self.front
            for i in range(1, pos):
                p = p.next

            node.prev = p.prev
            node.next = p

            p.prev.next = node
            p.prev = node

            self.size += 1

    def deleteFront(self):
        if self.size != 0:
            p = self.front
            data = p.data
            self.front = p.next

            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.size -= 1
            return data

    def deleteRear(self):
        if self.size != 0:
            p = self.rear
            data = p.data
            self.rear = p.prev

            if self.rear == None:
                self.prev = None
            else:
                self.rear.next = None
            self.size -= 1
            return data


    def display(self):
        p = self.front
        while p!=None:
            print("[%c] <-> " % p.data, end='')
            p = p.next
        print("\b\b\b\b    ")

if __name__ == "__main__":
    DL = DListType()
    DL.addFront('A'); DL.addFront('B'); DL.display()
    DL.addRear('C'); DL.addRear('D'); DL.display()
    DL.addPos(3, 'E'); DL.display()

    print("[%c] is deleted : " % DL.deleteFront(), end=''); DL.display()
    print("[%c] is deleted : " % DL.deleteRear(), end=''); DL.display()