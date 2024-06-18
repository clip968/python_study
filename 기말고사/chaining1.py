class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
M = 13

class HashTable:
    def __init__(self):
        self.table = [None] * M
        
    
    def hashFn(self, key):
        return (key % M)
    
    def insert(self, key):
        b = self.hashFn(key)
        node = Node(key, self.table[b])
        node.next = self.table[b]
        self.table[b] = node
        
    def display(self):
        for i in range(M):
            print('HT[%2d] : ' % i, end='')
            n = self.table[i]
            
            if n == None:
                print()
                
            else:
                while n != None:
                    print(n.data, end=' ')
                    n = n.next
                print()
                
    def delete(self, key):
        b = self.hashFn(key)
        n = self.table[b]
        
        if n == None:
            print('아무것도 없어용')
            return

        if n.data == key:
            self.table[b] = n.next
            
        else:
            prev = n
            n = n.next
            while n is not None:
                if n.data == key:
                   prev.next = n.next
                   return
                prev = n
                n = n.next 
    def search(self, key):
        b = self.hashFn(key)
        n = self.table[b]
        
        if n == None:
            return False
        
        elif n.data == key:
            return True
        
        else:
            while n != None:
                if n.data == key:
                    return True
                n = n.next
        
        return False
if __name__ == "__main__":
    # import random
    
    HT = HashTable()
    
    # for i in range(20):
    #     HT.insert(random.randint(10, 99))
    
    # HT.display()
    # HT.delete(25)
    # HT.display()
    HT.insert(10)
    HT.insert(20)
    HT.insert(30)
    HT.insert(40)
    HT.insert(50)
    HT.insert(37)
    HT.display()
    print()
    HT.delete(37)
    HT.display()
    print(HT.search(50))
    print()