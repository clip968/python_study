from collections import deque
def solution(priorities, location):
    maximum = max(priorities)
    array = [0] * (len(priorities))
    cnt = 0
    stack = 0
    while priorities:
        for i in priorities:
            if i == maximum:
                cnt += 1
                array[priorities.index(i)] = cnt
                priorities.remove(i)
    return array[location]

print(solution([2,1,3,2], 2))