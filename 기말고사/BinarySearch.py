import random
from SelectionSort import *

def sequential_search(A, key):
    low = 0
    high = len(A) - 1
    for i in range(low, high+1):
        if A[i] == key:
            return i
    
    return None

def rBinarySearch(A, key, low, high):
    if(low > high): return -1
    
    mid = (low + high) // 2
    print(A[mid], end=' ')
    
    if key == A[mid]: 
        return mid
    
    elif key < A[mid]:
        return rBinarySearch(A, key, low, mid - 1)
    else:
        return rBinarySearch(A, key, mid + 1, high)

def iBinarySearch(A, key):
    low = 0
    high = len(A)
    while(low <= high):
        mid = (low + high) // 2
        print(A[mid], end=' ')
        
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def interplation_Search(A, key):
    low = 0
    high = len(A) - 1
    
    while low <= high and key >= A[low] and key <= A[high]:
        if low == high:
            if A[low] == key:
                return low
            return -1
        
        pos = low + ((key - A[low]) * (high - low)) // (A[high] - A[low]) 
        
        if A[pos] == key:
            return pos
        elif A[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
            
if __name__ == "__main__":
    A = []
    for i in range(15):
        A.append((random.randint(1, 100)))
    
    selectionSort(A)
    print('A[] = ', A)
    
    key = int(input('Input Search key : '))
    print('rBinary Search : %d' % rBinarySearch(A, key, 0, len(A)-1))
    
    print('iBinary Search : %d' % iBinarySearch(A, key))
    