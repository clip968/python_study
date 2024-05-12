def count_one(num):
    return bin(num).count('1')

def find_pi(data):
    pi = {}
    for i in data:
        for j in data:
            diff = int(i, 2) ^ int(j, 2)
            one_diff = bin(diff).count('1')
            if one_diff == 1:
                if count_one(int(i, 2)) not in pi:
                    pi[count_one(int(i, 2))] = []
                pi[count_one(int(i, 2))].append((i, j))
                    
    return pi

def solution(minterms):
    numberCnt = {}
    for minterm in minterms:
        b = count_one(minterm)
        if b not in numberCnt:
            numberCnt[b] = []
        numberCnt[b].append(bin(minterm)[2:].zfill(3))
    pi = []
    
    for nums in sorted(numberCnt.keys()):
        c = numberCnt[nums]
        pis = find_pi(c)
        pi.extend(pis.items())
        
    result = []
    for group, minterms in sorted(pi):
        for minterm in minterms:
            result.append('1' * group + minterm.replace('0', '-').replace('1', '1'))
    
    return result

minterms = [3, 6, 0, 1, 2, 5, 6, 7]
result = solution(minterms)
print(result)
