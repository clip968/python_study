capacity = 100
array = [None] * capacity
size = 0

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print('Overflow Or Invalid Position')
        
def display():
    for i in range(size):
        print(array[i], end=' ')
    print()
def findItem(e):
    for i in range(size):
        if array[i] == e:
            return i
    
    return -1
        
def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i + 1]
        size -= 1
        return e
    else:
        print('Underflow Or Invalid Position')
        
if __name__ == "__main__":
    insert(0, 'A')
    insert(1, 'B')
    insert(1, 'C')
    display()
    
    insert(2, 'D')
    insert(3, 'E')
    display()
    
    print(delete(3))
    display()
    
    e = input('Input item to delete : ')
    idx = findItem(e)
    if idx != -1:
        delete(idx)
        display()
        