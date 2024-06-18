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
        
        
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        # 이미 정렬된 경우 루프를 조기에 종료하기 위한 플래그
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 두 요소를 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # 만약 내부 루프에서 요소가 교환되지 않았다면 리스트가 정렬된 상태임
        if not swapped:
            break
            
    return arr
    
    
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
    bubbleSort(L)
    print("Bubble :", L)
    print()