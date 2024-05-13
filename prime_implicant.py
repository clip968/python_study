def count_one(num):
    result = 0
    for i in num:
        if i == '1':
            result += 1
    return result

def find_pi(data):
    pi = {}
    for i in data:
        for j in data:
            if i != j:
                diff = int(i) ^ int(j)
                one_diff = bin(diff).count('1')
                if one_diff == 1:
                    if count_one(i) not in pi:
                        pi[count_one(i)] = []
                    pi[count_one(i)].append((i, j))
                    
    return pi

def solution(minterms):
    numberCnt = {}
    number_binary = []
    for minterm in minterms:
        a = bin(minterm)
        number_binary.append(a[2:].zfill(3))
    
    for number in number_binary:
        b = count_one(number)
        if b not in numberCnt:
            numberCnt[b] = []
        numberCnt[b].append(number)
    pi = []
    
    for nums in sorted(numberCnt.keys()):
        c = numberCnt[nums]
        pis = find_pi(c)
        pi.extend(pis.items())
        
    result = []
    for group, minterms in sorted(pi):
        for minterm in minterms:
            result.append(f"{group*'1'}{minterm.replace('0', '-').replace('1', '1')}")
    
    return result

minterms = [3, 6, 0, 1, 2, 5, 6, 7]
result = solution(minterms)
print(result)
