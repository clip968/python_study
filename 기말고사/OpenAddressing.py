# 개방 주소법(선형, 이차, 이중 해싱이 포함되어 있음)

M = 13
table = [0] * M

def hashFn(key):
    return key % M

# 선형 조사법
def getLinear(v, i): 
    return (v + i) % M

def hashFn2(key):
    return 11 - (key % 11)

# 이차 조사법
def getQuadratic(v, i):
    return (v + i*i) % M

# 이중 해싱법
def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M

def search(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)
        
        print('[%d] ' % table[b], end='')
        
        if table[b] == 0:
            return 0
        elif table[b] == key:
            return table[b]
        else:
            i += 1
            
    return 0
            
def delete(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)
        
        print('[%d] ' % table[b], end='')
        
        if table[b] == 0:
            print("No Key to Delete")
            return 
        elif table[b] == key:
            table[b] = 0
            return
        else:
            i += 1
            
    return 0

def insert(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)
        if table[b] == 0:
            table[b] = key
            return 
        else:
            i += 1

def display():
    print()
    print('Bucket   Key')
    print('============')
    
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
    # delete를 사용해버리면 기존에 46이 들어갈 자리에 60이 있었기 때문에 60이 있던 자리가 0으로 바뀌었으니
    # search 함수를 돌리면 0이 등장하게 된다.
    # 따라서 원래 있다가 delete로 지운 것은 -1이나 다른 숫자로 대체하여 구분을 해줘야 한다.