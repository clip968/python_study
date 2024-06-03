N = 100

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def insertItem(self, item):
        self.heapSize += 1
        self.heap[self.heapSize] = item
        self.upHeap()
    
    def upHeap(self):
        i = self.heapSize # i <- 11이 들어감 말단 노드
        item = self.heap[i] # item <- 8 이 들어감
        
        while(i != 1) and (item > self.heap[i // 2]):
            self.heap[i] = self.heap[i // 2]
            i //= 2
        
        self.heap[i] = item
        
    def removeItem(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1
        self.downHeap()
        
        return item
    
    def downHeap(self):
        item = self.heap[1]
        parent = 1
        child = 2
        
        while child <= self.heapSize: # child가 heapsize가 될 수도 있음
            # if도 같이 쓰는 이유는 형재 노드를 비교 해야 하기 때문
            if (child < self.heapSize) and (self.heap[child + 1] > self.heap[child]):
                child += 1
                
            if item >= self.heap[child]:
                break
            
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2
            
        self.heap[parent] = item
               
if __name__ == "__main__":
    H = MaxHeap()
    data = [7, 3, 5, 6, 4, 9, 2, 3, 1, 2]
    
    for e in data:
        H.insertItem(e)
        print('Heap :', H.heap[1:H.heapSize + 1])
        
    print()
    
    print('[%d] is deleted ' % H.removeItem())
    print('Heap :', H.heap[1:H.heapSize + 1])