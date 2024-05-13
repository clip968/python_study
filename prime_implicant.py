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
def find_pi(data, start, end):
    pi = set()
    used = set()
    
    for j in data[start]:
        for k in data[end]:
            if j != k:
                if is_valid(j, k):
                    pi.add(compare(j, k))
                    used.add(j)
                    used.add(k)
        
                    
    return pi, used

def Quine_Mccluskey(minterms):
    numberCnt = {}
    number_binary = []
    length = minterms[0]
    minterms = minterms[1:]
    for minterm in minterms:
        a = bin(minterm)
        number_binary.append(a[2:].zfill(length))
    
    for number in number_binary:
        b = count_one(number)
        if b not in numberCnt:
            numberCnt[b] = []
        numberCnt[b].append(number)
    pi = []
    
    for i in range(0, len(numberCnt.keys())-1):
        a, b = find_pi(numberCnt, i, i + 1)
        pi.extend(a)
    v = set()
    pi2 = []
    piv = pi
    
    for i in range(len(piv)):
        for j in range(len(piv)):
            if is_valid(piv[i], piv[j]):
                v.add(compare(piv[i], piv[j]))
                b.add(piv[i])
                b.add(piv[j])
    pi2.extend(v)
     
    if pi2 == []:
        sorted_implicants = sorted(pi, key=lambda implicant: implicant.replace('-', '2'))
        return sorted_implicants

    return pi2

minterms = [3, 6, 0, 1, 2, 5, 6, 7]
result = Quine_Mccluskey(minterms)
print(result)
