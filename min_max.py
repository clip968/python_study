def find_min_max(A):
    min = A[0]  
    max = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
        if max < A[i]:
            max = A[i]
    
    return (min, max)
#나 자신이 실행하면 해당 코드를 실행함. 즉 import 된 상황에서 실행되진 않음.
if __name__ == '__main__':
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    (x, y) = find_min_max(data)
    print("(min, max) = ", (x, y))
    