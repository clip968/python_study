from itertools import chain

def count_one(num):
    result = 0
    for i in num:
        if i == '1':
            result += 1
    return result

def compare(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '-'
        else:
            result += a[i]
            
    return result

def is_valid(a, b):
    diff_count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_count += 1
            
            if diff_count > 1:
                return False
   
    return diff_count == 1

def find_pi(data, start, end, used):
    pi = dict()
    
    
    for j in data[start]:
        for k in data[end]:
            if j != k:
                if is_valid(j, k):
                    a = compare(j, k)
                    b = count_one(a)
                    if b not in pi:
                        pi[b] = []
                    if a not in pi[b]:
                        pi[b].append(a)
                        used.add(j)
                        used.add(k)
                    elif a in pi[b]:
                        used.add(j)
                        used.add(k)
                        continue
                        
    return pi

def Find_EPI(minterm, pi):
    for i in range(len(minterm)):
        if (pi[i] != '-' and minterm[i] != pi[i]):
            return False
    return True

def solution(minterms):
    numberCnt = {}
    number_binary = []
    length = minterms[0]
    minterms = minterms[2:]
    for minterm in minterms:
        a = bin(minterm)
        number_binary.append(a[2:].zfill(length))
    
    for number in number_binary:
        b = count_one(number)
        if b not in numberCnt:
            numberCnt[b] = []
        numberCnt[b].append(number)
    pi = numberCnt
    while True:
        new_pi = dict()
        used = set()
        pi_key = list(pi.keys())
        
        for i in range(len(pi_key)-1):
            a = find_pi(pi, pi_key[i], pi_key[i + 1], used)
            
            new_pi.update(a)
        if new_pi == pi:
            break
        
        if new_pi == {}:
            break
        for key in pi_key:
            for minterm in pi[key]:
                if minterm not in used:
                    b = count_one(minterm)
                    if b not in new_pi:
                        new_pi[b] = []
                    new_pi[b].append(minterm)
        pi = new_pi
        
    merge_pi = list(chain.from_iterable(pi.values()))
    sorted_implicants = sorted(merge_pi, key=lambda implicant: implicant.replace('-', '2'))
    
    epi = set()
    temp = []
    
    for i in range(len(number_binary)):
        temp = []
        for j in range(len(sorted_implicants)):
            if (Find_EPI(number_binary[i], sorted_implicants[j])):
                temp.append(j)
        if len(temp) == 1:
            epi.add(temp[-1])
    
    sorted_implicants.append("EPI")
    for i in epi:
        sorted_implicants.append(sorted_implicants[i])
        
    return sorted_implicants
    
    