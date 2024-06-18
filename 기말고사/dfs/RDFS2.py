vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 노드
#          0    1    2    3    4    5    6    7
AdjVer = [   # 인접 리스트(간선)
    [1, 2],
    [0, 3],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6, 7],
    [3],
    [4, 7],
    [4, 6]]

from queue import LifoQueue


def iDFS(v):
    s = LifoQueue()  # stack
    s.put(v)

    while not s.empty():
        v = s.get()
        s.put(v)  # peek

        if visited[v] == False: # 방문
            visited[v] = True
            print(vertex[v], end=' ')

        flag = True
        for v in AdjVer[v]:
            if visited[v]==False:
                s.put(v)
                flag = False
                break

        if flag==True:
            s.get()

if __name__ == "__main__":
    visited = [False] * len(vertex) # 방문기록
    print("iDFS(A) : ", end = '')
    iDFS(0)