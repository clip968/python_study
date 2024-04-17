class ArraySet:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        
    def isFull(self):
        return self.capacity == self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def contains(self, e):
        for i in range(self.size):
            if e == self.array[i]:
                return True
        return False
        
    def insert(self, e):
        if not self.isFull() and not self.contains(e):
            self.array[self.size] = e
            self.size += 1
            
    def delete(self, e):
        for i in range(self.size):
            if e == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                
    def union(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
            
        for i in range(setB.size):
            setC.insert(setB.array[i])
            
        return setC
    
    def intersection(self, setB):
        setC = ArraySet()
        
        for i in range(setB.size):
            if setB.array[i] in self.array:
                setC.insert(setB.array[i])
        
        return setC
    
    def difference(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            if self.array[i] not in setB.array:
                setC.insert(self.array[i])
        
        return setC
    
    def __eq__(self, setB):
        
        if setB.size == self.size:
            for i in range(self.size):
                if self.array[i] not in setB.array:
                    return False
            
            return True
        
        else: return False
    
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
        
if __name__ == "__main__":
    
    S = ArraySet()
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(40)
    S.display()
    
    T = ArraySet()
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(30)
    T.display()
    
    print(S == T)
    S.union(T).display()
    S.intersection(T).display()
    S.difference(T).display()
        