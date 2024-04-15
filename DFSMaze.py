from Arraystack import Arraystack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(x, y):
    if 0 <= x < SIZE and 0 <= y < SIZE:
        if map[x][y] == '0' or map[x][y] == 'x':
            return True
    
    return False

def DFS():
    print('DFS : ')
    S = Arraystack(100)
    S.push((1, 0))
    
    while not S.isEmpty():
        pos = S.pop()
        print(pos, end=' -> ')
        (x, y) = pos
        if (map[x][y] == 'x'):
            return True
        else:
            map[x][y] = '.'
            if isValidPos(x - 1, y): S.push((x - 1, y))
            if isValidPos(x + 1, y): S.push((x + 1, y))
            if isValidPos(x, y - 1): S.push((x, y - 1))
            if isValidPos(x, y + 1): S.push((x, y + 1))
            
        S.display()
    
    return False

if __name__ == "__main__":
    
    result = DFS()
    
    if result:
        print('Success')
    else:
        print('Fail')
        