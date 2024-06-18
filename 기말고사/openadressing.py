M = 13
table = [0] * M

def hashFn(key):
    return key % M

def getLinear(v, i):
    return(v + i) % M

def getQuadratic(v, i):
    return (v + i * i) % M

def hashFn2(key):
    return 11 - (key % 11)

def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M

def search(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        
        print('[%d] ' % table[b], end='')
        
        if table[b] == 0:
            return 0
        
        elif table[b] == key:
            return table[b]
        
        else:
            i += 1
            
def delete(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        
        print('[%d] ' % table[b], end='')
        
        if table[b] == 0:
            print('No key to delete')
            return
        
        elif table[b] == key:
            table[b] = 0
            return
        
        else:
            i += 1
            
def insert(key):
    v = hashFn(key)
    i = 0
    
    while i< M:
        b = getLinear(v, i)
        
        print('[%d] ', end='')
        
        if table[b] == 0:
            table[b] = key
            return
            
        else:
            i += 1

def display():
    print()
    print('Buket   key')
    print('           ')
    
    for i in range(M):
        print('HT[%2d] : %2d' % (i, table[i]))
        
if __name__ == '__main__':
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print('h(%2d) = %2d' % (d, hashFn(d)))
        insert(d)
        print(table)
    
    display()
    print()
    print('Search(46) --> ', search(46))
    print('Search(46) --> ', search(39))
    
    delete(60); display()
    print('Search(46) --> ', search(46))
