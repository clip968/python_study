def selectionSort(L):
    n = len(L)
    
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if L[j] < L[least]:
                least = j
        L[least], L[j] = L[j], L[least]
        
def insertionSort(L):
    n = len(L)
    
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

def bubbleSort(L):
    n = len(L)
    
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j+1], L[j]
                flag = True
        
        if not flag:
            break
    
    return L