vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import LifoQueue

visited = [False] * len(vertex)

def iDFS(v):
    S = LifoQueue()
    S.put(v)
    
    while not S.empty():
        v = S.get()
        S.put(v)
        
        if visited[v] == False:
            visited[v] = True  
            print(vertex[v], end=' ')
            
        flag = True
        for i in AdjVer[v]:
            if visited[i] == False:
                S.put(i)
                flag = False
                break
            
        if flag == True:
            S.get()
            
if __name__ == "__main__":
    print('iDFS(A) : ', end='')
    iDFS(0)