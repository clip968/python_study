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
visited = [False * len(vertex)]

def rDFS(visited, v):
    visited[v] = True
    print(vertex[v], end=' ')
    
    for v in AdjVer[v]:
        if visited[v] == False:
            rDFS(visited, v)

if __name__ == "__main__":
    visited = [False] * len(vertex) # 방문 기록
    print('rDFS(A) : ', end='')
    rDFS(visited, 0)