def printStep(L, idx):
    print('   Step %d : ' %idx, end='')
    print(L)
    

def selectionSort(L):
    n = len(L)
    
    for i in range(n-1):
        least = i
        for j in range(i + 1, n):
            if L[j] < L[least]:
                least = j
        L[i], L[least] = L[least], L[i]
        # printStep(L, i + 1)
        
def insertionSort(L):
    n = len(L)
    
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j + 1] = key
        #printStep(L, i) 
        
def BubbleSort(L):
    n = len(L)
    
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if(L[j] > L[j + 1]):
                L[j] , L[j + 1] = L[j + 1], L[j]
                bChanged = True
        if not bChanged:
            break
        # printStep(L, i)
    
    
if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    
    L = list(data)
    print("before : ", L)
    selectionSort(L)
    print("Selection :", L)
    print()
    
    L = list(data)
    print("before : ", L)
    insertionSort(L)
    print("Insertion :", L)
    print()
    
    L = list(data)
    print("before : ", L)
    BubbleSort(L)
    print("Bubble :", L)
    print()