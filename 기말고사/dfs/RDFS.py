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
def rDFS(visited, v):
    visited[v] = True
    print(vertex[v], end=' ')

    for v in AdjVer[v]:
        if visited[v] == False:
            rDFS(visited, v)

if __name__ == "__main__":
    visited = [False] * len(vertex) # 방문기록
    print("rDFS(A) : ", end = '')
    rDFS(visited, 0)