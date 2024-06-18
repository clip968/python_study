import random

def selectionSort(L):
    n = len(L)
    
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if L[j] < L[least]:
                least = j
        L[j], L[least] = L[least], L[j]

def sequential_search(A, key):
    low = 0
    high = len(A) - 1
    for i in range(low, high + 1):
        if key == A[i]:
            return i
    
    return None

def rBinarySearch(A, key, low, high):
    if low > high:
        return -1
    mid = (high + low) // 2
    
    if key == A[mid]:
        return mid
    
    elif key < A[mid]:
        return rBinarySearch(A, key, low, mid - 1)
    else:
        return rBinarySearch(A, key, mid + 1, high)
    
def iBinarySearch(A, key, low, high):
    low = 0
    high = len(A)
    while(low <= high):
        mid = (low + high) // 2
        
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return -1

def interplation_search(A, key):
    low = 0
    high = len(A) - 1
    
    while low<=high and key>=A[low] and key <= A[high]:
        if low == high:
            if A[low] == key:
                return low
            return -1
        
        pos = low + ((key - A[low]) * (high - low) // (A[high] - A[low]))
        if A[pos] == key:
            return pos
        elif A[pos] < key:
            low = pos + 1
        else:
            high = pos - 1