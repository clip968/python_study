class Arrayset:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
        
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
    
    def union(self, setB):
        setC = Arrayset()
        
        for i in range(self.size):
            setC.insert(self.array[i])
            
        for i in range(setB.size):
            setC.insert(setB.array[i])
        
        return setC
    
    def intersection(self, setB):
        setC = Arrayset()
        
        for i in range(setB.size):
            if setB.array[i] in self.array:
                setC.insert(setB.array[i])

        return setC
    
    def difference(self, setB):
        setC = Arrayset()
        
        for i in range(self.size):
            if self.array[i] not in setB.array:
                setC.insert(self.array[i])
        
        return setC
    
    def __eq__(self, setB):
        
        if self.size == setB.size:
            for i in range(self.size):
                if self.array[i] not in setB.array:
                    return False
            return True
        
        else:
            return False
        
        
if __name__ == '__main__':
    S = Arrayset()
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(40)
    S.display()
    
    T = Arrayset()
    T.insert(40)
    T.insert(30)
    T.insert(20)
    T.insert(10)
    T.display()
    
    print(S == T)
    # S.union(T).display()
    # S.intersection(T).display()
    # S.difference(T).display()
    # 교집합, 차집합 연산
    # print(S == T) : 연산자 중복
    